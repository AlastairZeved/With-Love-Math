#!/usr/bin/env python3
"""Render README.md the way GitHub would (GFM-ish) in both color schemes.

Writes build/render/{light,dark}-full.png plus named detail crops, so the
verification screenshots show what a reader actually sees.
"""
import os, re, subprocess, json
import markdown
from PIL import Image

REPO = "/home/aboveaveragerob/With-Love-Math"
OUT = f"{REPO}/build/render"
os.makedirs(OUT, exist_ok=True)

md = open(f"{REPO}/README.md", encoding="utf8").read()

# ── GitHub parses markdown INSIDE <details> blocks; python-markdown does not.
#    Convert each details' inner markdown ourselves and stash it behind a
#    placeholder so the outer pass cannot re-mangle it. ──
DETAILS = []

def stash_details(m):
    block = m.group(0)
    lm = re.match(r'(?s)(<details[^>]*>\s*<summary>.*?</summary>)(.*)(</details>)', block)
    if not lm:
        return block
    head, inner, tail = lm.group(1), lm.group(2), lm.group(3)
    inner_html = markdown.markdown(inner.strip(),
                                   extensions=['tables', 'fenced_code', 'sane_lists'], output_format='html5')
    idx = len(DETAILS)
    DETAILS.append(head + inner_html + tail)
    return f'@@DETAILS{idx}@@'

md = re.sub(r'(?s)<details[^>]*>.*?</details>', stash_details, md)

# ── render GFM-ish HTML; keep <picture> markup intact so color-scheme works ──
html = markdown.markdown(md, extensions=['tables', 'fenced_code', 'sane_lists', 'md_in_html'],
                         output_format='html5')
for i, block in enumerate(DETAILS):
    html = html.replace(f'@@DETAILS{i}@@', block)
    html = html.replace(f'<p>@@DETAILS{i}@@</p>', block)
html = html.replace('src=".github/assets/', f'src="{REPO}/.github/assets/')
html = html.replace('srcset=".github/assets/', f'srcset="{REPO}/.github/assets/')

# ── GitHub alert callouts: python-markdown leaves "> [!IMPORTANT]" as a plain
#    blockquote with the literal marker; GitHub renders a titled callout box. ──
ALERT_COLORS = {"NOTE": "#0969da", "TIP": "#1a7f37", "IMPORTANT": "#8250df",
                "WARNING": "#9a6700", "CAUTION": "#cf222e"}
ALERT_LABEL = {"NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important",
               "WARNING": "Warning", "CAUTION": "Caution"}

def alert(m):
    kind, inner = m.group(1), m.group(2)
    inner = inner.strip()
    # the marker itself is the first line of the blockquote's first paragraph
    inner = re.sub(r'^\s*<p>\s*\[!' + kind + r'\]\s*', '<p>', inner, count=1)
    color = ALERT_COLORS[kind]
    return (f'<div class="alert" style="border-left:4px solid {color};padding:2px 16px;margin:16px 0">'
            f'<p style="font-weight:600;color:{color};margin:8px 0 4px">{ALERT_LABEL[kind]}</p>{inner}</div>')

html = re.sub(r'<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</blockquote>',
              alert, html, flags=re.S)

def page(body, scheme):
    if scheme == "dark":
        bg, fg, border, th, code = "#0d1117", "#e6edf3", "#3d444d", "#151b23", "#151b23"
    else:
        bg, fg, border, th, code = "#ffffff", "#1f2328", "#d1d9e0", "#f6f8fa", "#f6f8fa"
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
body {{ margin:0; padding:32px 40px; background:{bg}; color:{fg};
        font: 16px/1.6 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; max-width: 1012px; }}
h1 {{ font-size:30px; border-bottom:1px solid {border}; padding-bottom:10px; }}
h2 {{ font-size:24px; border-bottom:1px solid {border}; padding-bottom:8px; margin-top:28px; }}
h3 {{ font-size:19px; margin-top:22px; }}
img {{ max-width:100%; height:auto; }}
table {{ border-collapse:collapse; }} th,td {{ border:1px solid {border}; padding:6px 13px; }}
th {{ background:{th}; }}
code {{ background:{code}; padding:2px 5px; border-radius:5px; font:85% ui-monospace, monospace; }}
pre {{ background:{code}; padding:14px; border-radius:8px; overflow-x:auto; }}
pre code {{ background:none; }}
blockquote {{ border-left:3px solid {border}; margin:0; padding:0 16px; color:#8b949e; }}
summary {{ cursor:pointer; font-weight:600; }}
</style></head><body>{body}</body></html>'''

for scheme in ("light", "dark"):
    open(f"{OUT}/{scheme}.html", "w").write(page(html, scheme))

# ── screenshot both schemes, expand <details>, capture per-chapter offsets ──
js = '''
const { chromium } = require("playwright");
const fs = require("fs");
(async () => {
  const browser = await chromium.launch();
  const offsets = {};
  for (const scheme of ["light", "dark"]) {
    const page = await browser.newPage({ viewport: { width: 1092, height: 1200 },
                                         colorScheme: scheme === "dark" ? "dark" : "light" });
    await page.goto("file:///home/aboveaveragerob/With-Love-Math/build/render/" + scheme + ".html");
    await page.waitForTimeout(1200);
    await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
    await page.waitForTimeout(500);
    if (scheme === "light") {
      offsets.headings = await page.evaluate(() =>
        [...document.querySelectorAll('h1,h2')].map(h => ({ text: h.textContent.trim(),
                                                            y: Math.round(h.getBoundingClientRect().top + window.scrollY) })));
      offsets.height = await page.evaluate(() => document.body.scrollHeight);
    }
    await page.screenshot({ path: "/home/aboveaveragerob/With-Love-Math/build/render/" + scheme + "-full.png", fullPage: true });
    await page.close();
  }
  fs.writeFileSync("/home/aboveaveragerob/With-Love-Math/build/render/offsets.json", JSON.stringify(offsets, null, 1));
  console.log(JSON.stringify(offsets.headings));
  await browser.close();
})();
'''
os.makedirs(f"{REPO}/build/js", exist_ok=True)
open(f"{REPO}/build/js/render-both.js", "w").write(js)
subprocess.run(["node", f"{REPO}/build/js/render-both.js"], check=True)

# ── crops: one per chapter (heading y -> next heading y), both schemes ──
import json
bounds = json.load(open(f"{OUT}/offsets.json"))
heads = [h for h in bounds["headings"] if h["text"].startswith(("Plate ", "Contents", "Design notes"))]
H = bounds["height"]
labels = []
for i, h in enumerate(heads):
    top = h["y"] - 70 if i else 0
    bottom = heads[i + 1]["y"] - 70 if i + 1 < len(heads) else H
    label = h["text"].split("—")[0].strip().replace("Plate ", "plate-").replace(" ", "-").lower()
    if h["text"] == "Contents":
        label = "contents"
    if h["text"] == "Design notes":
        label = "design-notes"
    labels.append((label, top, bottom, h["text"]))
    print(f"  {label:16s} y {top}..{bottom}  ({bottom-top}px)  {h['text']}")
for scheme in ("light", "dark"):
    im = Image.open(f"{OUT}/{scheme}-full.png")
    w, h = im.size
    for label, top, bottom, _ in labels:
        im.crop((0, max(0, top), w, min(h, bottom))).save(f"{OUT}/{scheme}-{label}.png")
print("renders written to", OUT)
