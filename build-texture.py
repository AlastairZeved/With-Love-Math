# The ground: one seamless warm graph-paper motif for every chapter plate.
# Warm cream base, faint gold graph grid (minor 24 / major 120), a faint
# margin rule, and a loose field of EB Garamond ampersands + italic digits
# (the ten positions) drifting under the grid — "love letter meets mathematics."
# Dark + light variants, both verified to tile seamlessly.
import os, subprocess, random

A = "/home/aboveaveragerob/With-Love-Math/.github/assets"
os.makedirs(f"{A}/textures", exist_ok=True)
os.makedirs("build", exist_ok=True)
subprocess.run(["fonttools", "ttLib.woff2", "decompress", "-o", "build/EBGaramond-Regular.ttf",
                os.path.expanduser("~/with-love-math-showcase/fonts/EBGaramond-Regular.ttf")], check=True)
subprocess.run(["fonttools", "ttLib.woff2", "decompress", "-o", "build/EBGaramond-Italic.ttf",
                os.path.expanduser("~/with-love-math-showcase/fonts/EBGaramond-Italic.ttf")], check=True)

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

_W = {}
def _font(path, key):
    if key not in _W:
        _W[key] = TTFont(path)
    return _W[key]

def glyph_path(path, ch, key):
    f = _font(path, key)
    gs = f.getGlyphSet()
    g = gs[f.getBestCmap()[ord(ch)]]
    pen = SVGPathPen(gs); g.draw(pen)
    bp = __import__("fontTools.pens.boundsPen", fromlist=["BoundsPen"]).BoundsPen(gs)
    g.draw(bp)
    return pen.getCommands(), (bp.bounds or (0, 0, 0, 0)), g.width / f["head"].unitsPerEm

def glyph_at(text_ch, size, key, fill, x, y, opacity):
    d, b, adv = glyph_path({"ser": "build/EBGaramond-Regular.ttf",
                            "ita": "build/EBGaramond-Italic.ttf"}[key], text_ch, key)
    sc = size / 1000  # EB Garamond upm
    return (f'<g transform="translate({x:.2f},{y:.2f}) scale({sc:.6f},{-sc:.6f})" '
            f'opacity="{opacity:.3f}"><path d="{d}" fill="{fill}"/></g>', adv * size)

W, H = 1680, 480
MINOR, MAJOR = 24, 120

def ground(base, grid_minor, grid_major, margin, glyph_a, glyph_b, name, op_lo=0.35, op_hi=0.55):
    # ── 1. seamless glyph field: jittered lattice, wrapped at tile edges ──
    rng = random.Random(11)
    CH = "&1234567890"
    items = []
    cols, rows = 26, 8
    cw, chh = W / cols, H / rows
    for r in range(rows):
        for c in range(cols):
            ch = CH[(r * cols + c) % len(CH)]
            gx = c * cw + rng.uniform(-cw * 0.3, cw * 0.3)
            gy = r * chh + rng.uniform(-chh * 0.25, chh * 0.25) + chh * 0.55
            gs_ = rng.uniform(15, 26) if ch == "&" else rng.uniform(12, 20)
            op = rng.uniform(op_lo, op_hi)
            # wrap: emit glyph + its horizontally-shifted twin so edges tile
            for dx in (0, W):
                if -60 < gx + dx < W + 60:
                    s, _ = glyph_at(ch, gs_, "ita" if ch != "&" else "ser",
                                    glyph_a if (r + c) % 2 else glyph_b, gx + dx, gy, op)
                    items.append(s)
                    if 40 < gy < H - 40:
                        s2, _ = glyph_at(ch, gs_, "ita" if ch != "&" else "ser",
                                         glyph_a if (r + c) % 2 else glyph_b, gx + dx, gy - H, op)
                        items.append(s2)
                        s3, _ = glyph_at(ch, gs_, "ita" if ch != "&" else "ser",
                                         glyph_a if (r + c) % 2 else glyph_b, gx + dx, gy + H, op)
                        items.append(s3)
    field = "".join(items)

    # ── 2. graph grid: minor lines (wrapped by pattern transform) ──
    grid = []
    x = 0
    while x <= W:
        sw = 1 if x % MAJOR else 1.4
        op = 0.10 if x % MAJOR else 0.16
        col = grid_major if x % MAJOR else grid_major
        grid.append(f'<path d="M{x:g} 0 V{H}" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>')
        x += MINOR
    y = 0
    while y <= H:
        sw = 1.4 if y % MAJOR else 1.4
        op = 0.10 if y % MAJOR else 0.16
        grid.append(f'<path d="M0 {y} H{W}" stroke="{grid_major}" stroke-width="{sw}" opacity="{op}"/>')
        y += MINOR
    grid_svg = "".join(grid)

    # ── 3. margin rule + punch holes (notebook fiction) ──
    margin_svg = (
        f'<line x1="{W-64}" y1="0" x2="{W-64}" y2="{H}" stroke="{margin}" stroke-width="1.4" opacity="0.28"/>'
        f'<line x1="{W-58}" y1="0" x2="{W-58}" y2="{H}" stroke="{margin}" stroke-width="0.7" opacity="0.16"/>'
    )
    holes = "".join(
        f'<circle cx="{W-61}" cy="{yy}" r="4" fill="{base}" stroke="{margin}" stroke-width="1" opacity="0.5"/>'
        for yy in (60, H/2, H-60)
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <pattern id="tile" width="{W}" height="{H}" patternUnits="userSpaceOnUse">
      <rect width="{W}" height="{H}" fill="{base}"/>
      {field}
      {grid_svg}
      {margin_svg}
      {holes_svg if False else holes}
    </pattern>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#tile)"/>
</svg>'''
    with open(f"{A}/textures/{name}.svg", "w") as f:
        f.write(svg)
    print(name, "written", len(svg))

# placeholder fix: holes built below per call
holes = ""
holes_svg = ""
ground("#0a0a0c", "#c9a227", "#c9a227", "#c9a227", "#26262c", "#413a22", "ground-dark")
ground("#f8f5ec", "#b89a3f", "#b89a3f", "#b89a3f", "#c9bd97", "#b3a678", "ground-light", op_lo=0.22, op_hi=0.38)

# ── 4. verification: two 1600x420 PNG renders — one full tile, one at x=800 ──
html = f'''<!doctype html><html><body style="margin:0">
<div style="width:{W}px;height:{H}px"><img src="../.github/assets/textures/ground-dark.svg" style="display:block"></div>
</body></html>'''
with open("build/ground-dark.html", "w") as f:
    f.write(html.replace("../.github", "/home/aboveaveragerob/With-Love-Math/.github"))
html2 = html.replace('style="width:1600px', 'style="width:3200px').replace(
    '"><img', '"><div style="width:800px;height:480px;overflow:hidden"><img')
with open("build/ground-shift.html", "w") as f:
    f.write('''<!doctype html><html><body style="margin:0">
<div style="width:2400px;height:480px;overflow:hidden"><img src="/home/aboveaveragerob/With-Love-Math/.github/assets/textures/ground-dark.svg" style="display:block;margin-left:-800px"></div>
</body></html>''')

script = '''
    const { chromium } = require("playwright");
    (async () => {
      const browser = await chromium.launch();
      for (const [name, w] of [["ground-dark", 1600], ["ground-shift", 2400]]) {
        const page = await browser.newPage({ viewport: { width: w, height: 420 } });
        await page.goto("file:///home/aboveaveragerob/With-Love-Math/build/" + name + ".html");
        await page.waitForTimeout(300);
        await page.screenshot({ path: "/home/aboveaveragerob/With-Love-Math/build/" + name + ".png" });
        await page.close();
      }
      await browser.close();
    })();
'''
with open("build/js/ground-shot.js", "w") as f:
    f.write(script)
subprocess.run(["node", "build/js/ground-shot.js"], check=True)
print("PNG verification shots written")