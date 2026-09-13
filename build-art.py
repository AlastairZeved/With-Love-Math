# Full README art pass: chapter header plates on the graph-paper ground +
# designed diagrams (drift, doors, commands, pillars, loop cycle, two-axis map,
# layers, WONDER anchor, portability split). Dark + light for every asset.
# Reuses the EB Garamond / DejaVu glyph-to-path tooling from the banner pipeline.
import os, subprocess

A = "/home/aboveaveragerob/With-Love-Math/.github/assets"
os.makedirs("build", exist_ok=True)
for name in ("Regular", "Italic"):
    src = os.path.expanduser(f"~/with-love-math-showcase/fonts/EBGaramond-{name}.ttf")
    subprocess.run(["fonttools", "ttLib.woff2", "decompress", "-o", f"build/EBGaramond-{name}.ttf", src], check=True)
subprocess.run(["fonttools", "ttLib.woff2", "decompress", "-o", "build/DejaVuSansMono.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"], check=True)

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

_F = {}
def _font(key):
    paths = {"ser": "build/EBGaramond-Regular.ttf", "ita": "build/EBGaramond-Italic.ttf",
             "mono": "build/DejaVuSansMono.ttf"}
    if key not in _F:
        _F[key] = TTFont(paths[key])
    return _F[key]

def glyph(key, ch):
    f = _font(key)
    gs = f.getGlyphSet()
    g = gs[f.getBestCmap()[ord(ch)]]
    pen = SVGPathPen(gs); g.draw(pen)
    bp = BoundsPen(gs); g.draw(bp)
    return pen.getCommands(), (bp.bounds or (0, 0, 0, 0)), g.width / f["head"].unitsPerEm

def text(text_, size, key="ser", fill="#fff", x=0, y=0, anchor="start", opacity=None, tracking=0):
    f = _font(key)
    widths = {c: glyph(key, c)[2] * size for c in set(text_)}
    total = sum(widths[c] for c in text_) + tracking * max(len(text_) - 1, 0)
    if anchor == "middle": x -= total / 2
    elif anchor == "end": x -= total
    out = [] if not (opacity is not None and float(opacity) < 1) else ['<g opacity="%s">' % opacity]
    cx = x
    for ch in text_:
        d, _, _ = glyph(key, ch)
        if d.strip():
            sc = size / f["head"].unitsPerEm
            out.append(f'<g transform="translate({cx:.2f},{y:.2f}) scale({sc:.5f},{-sc:.5f})"><path d="{d}" fill="{fill}"/></g>')
        cx += widths[ch] + tracking
    if opacity is not None and float(opacity) < 1: out.append('</g>')
    return "".join(out), total

def wrap_lines(text_, size, key, max_w):
    sp = glyph(key, " ")[2] * size
    lines, cur, w = [], [], 0.0
    for word in text_.split(" "):
        ww = sum(glyph(key, c)[2] * size for c in word) + (sp if cur else 0)
        if cur and w + ww > max_w:
            lines.append(" ".join(cur)); cur, w = [word], ww - sp
        else:
            cur.append(word); w += ww
    if cur: lines.append(" ".join(cur))
    return lines

def wrapped(text_, size, key, fill, x, y0, lh, max_w, anchor="middle", opacity=None):
    out, y = "", y0
    for ln in wrap_lines(text_, size, key, max_w):
        s, _ = text(ln, size, key, fill, x, y, anchor, opacity)
        out += s; y += lh
    return out, y

# ── palettes ─────────────────────────────────────────────────
DARK = dict(gold="#c9a227", gold_hi="#f0d878", gold_dim="#8a6f1f", text="#e8e3da",
            sub="#9a938a", dim="#6b6455", card="#0f0f13", card_stroke="#2a2a30",
            node="#101014", node_gold="#171309", node_stroke="#6b6455",
            base="#0a0a0c", grid="#c9a227", glyph_a="#26262c", glyph_b="#413a22",
            ghost_op="0.10", op_lo=0.35, op_hi=0.55)
LIGHT = dict(gold="#8a6f1f", gold_hi="#b98f1d", gold_dim="#a08420", text="#241f12",
             sub="#6b6350", dim="#6b6350", card="#fbf8f0", card_stroke="#ded3b6",
             node="#faf8f0", node_gold="#fbf3d9", node_stroke="#8a7b52",
             base="#f8f5ec", grid="#b89a3f", glyph_a="#c9bd97", glyph_b="#b3a678",
             ghost_op="0.14", op_lo=0.22, op_hi=0.38)

W = 1560  # plate width

_symcache = {}
def _sym_paths():
    if not _symcache:
        for i, ch in enumerate("&1234567890"):
            key = "ser" if ch == "&" else "ita"
            d, _, _ = glyph(key, ch)
            _symcache[i] = f'<path id="gly{i}" d="{d}"/>'
    return "".join(_symcache[i] for i in range(11))

def ground_defs(P, gid, w, h):
    import random
    rng = random.Random(11)
    MINOR, MAJOR = 24, 120
    CH = "&1234567890"
    cols, rows = 26, 8
    cw, chh = w / cols, h / rows
    uses = []
    for r in range(rows):
        for c in range(cols):
            ch = CH[(r * cols + c) % len(CH)]
            gx = c * cw + rng.uniform(-cw * 0.3, cw * 0.3)
            gy = r * chh + rng.uniform(-chh * 0.25, chh * 0.25) + chh * 0.55
            gs_ = rng.uniform(15, 26) if ch == "&" else rng.uniform(12, 20)
            op = rng.uniform(P["op_lo"], P["op_hi"])
            fill = P["glyph_a"] if (r + c) % 2 else P["glyph_b"]
            idx = CH.index(ch)
            for dy in (0, -h, h):
                yy = gy + dy
                if -40 < yy < h + 40:
                    for dx in (0, w):
                        if -60 < gx + dx < w + 60:
                            uses.append(
                                f'<use href="#gly{idx}" transform="translate({gx+dx:.2f},{yy:.2f}) '
                                f'scale({gs_/1000:.5f},{-gs_/1000:.5f})" fill="{fill}" opacity="{op:.3f}"/>')
    grid = []
    x = 0
    while x <= w:
        sw = 1.4 if x % MAJOR == 0 else 1
        o = 0.16 if x % MAJOR == 0 else 0.10
        grid.append(f'<path d="M{x} 0 V{h}" stroke="{P["grid"]}" stroke-width="{sw}" opacity="{o}"/>')
        x += MINOR
    y = 0
    while y <= h:
        sw = 1.4 if y % MAJOR == 0 else 1
        o = 0.16 if y % MAJOR == 0 else 0.10
        grid.append(f'<path d="M0 {y} H{w}" stroke="{P["grid"]}" stroke-width="{sw}" opacity="{o}"/>')
        y += MINOR
    margin = (f'<line x1="{w-64}" y1="0" x2="{w-64}" y2="{h}" stroke="{P["grid"]}" stroke-width="1.4" opacity="0.28"/>'
              f'<line x1="{w-58}" y1="0" x2="{w-58}" y2="{h}" stroke="{P["grid"]}" stroke-width="0.7" opacity="0.16"/>')
    holes = "".join(f'<circle cx="{w-61}" cy="{yy}" r="4" fill="{P["base"]}" stroke="{P["grid"]}" stroke-width="1" opacity="0.5"/>'
                    for yy in (60, h/2, h-60))
    pat = (f'<pattern id="{gid}" width="{w}" height="{h}" patternUnits="userSpaceOnUse">'
           f'<rect width="{w}" height="{h}" fill="{P["base"]}"/>' + "".join(uses) + "".join(grid) + margin + holes + '</pattern>')
    return f'<defs>{_sym_paths()}{pat}</defs>'

def ribbon_snippet(name, x, y):
    s = open(f"{A}/icons/{name}-ribbon.svg").read()
    return s.replace('<svg xmlns', f'<svg x="{x}" y="{y}" xmlns', 1)

def frame(w, h, inset=16, op=0.22):
    return f'<rect x="{inset}" y="{inset}" width="{w-2*inset}" height="{h-2*inset}" fill="none" stroke="{P["gold"]}" stroke-opacity="{op}" stroke-width="1"/>'

def corner_ticks(w, h, m=16, L=36):
    ds = [f"M {m} {m+L} L {m} {m} L {m+L} {m}", f"M {w-m-L} {m} L {w-m} {m} L {w-m} {m+L}",
          f"M {w-m} {h-m-L} L {w-m} {h-m} L {w-m-L} {h-m}", f"M {m+L} {h-m} L {m} {h-m} L {m} {h-m-L}"]
    return "".join(f'<path d="{d}" stroke="{P["gold"]}" stroke-width="2" fill="none" opacity="0.8"/>' for d in ds)

def wrap_svg(svg_str, w, h, label):
    return svg_str.replace('<svg xmlns',
        f'<svg role="img" aria-label="{label}" xmlns', 1)

def plate(title, num, icon, keyline, h=300):
    inner = []
    inner.append(text(num, 210, "ser", P["gold"], x=66, y=232, anchor="start", opacity=P["ghost_op"])[0])
    inner.append(text("PLATE", 15, "mono", P["gold"], x=372, y=84, opacity=0.9, tracking=6)[0])
    inner.append(f'<line x1="372" y1="100" x2="500" y2="100" stroke="{P["gold"]}" stroke-width="1" opacity="0.4"/>')
    inner.append(text(title, 52, "ser", P["text"], x=372, y=172)[0])
    inner.append(text(keyline, 23, "ita", P["sub"], x=372, y=226)[0])
    rb = ribbon_snippet(icon, 1408, (h - 64) // 2)
    body = "".join(inner)
    label = f"Plate {num} — {title}. {keyline}"
    svgd = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" '
            f'role="img" aria-label="{label}">'
            + ground_defs(P, f"g{num}", W, h)
            + f'<rect width="{W}" height="{h}" fill="url(#g{num})"/>'
            + frame(W, h) + corner_ticks(W, h)
            + body + rb + '</svg>')
    return svgd

def write_pair(name, svg_dark, svg_light):
    open(f"{A}/{name}.svg", "w").write(svg_dark)
    open(f"{A}/{name}-light.svg", "w").write(svg_light)
    print(name, len(svg_dark))

def art(name, h, body_fn, label):
    global P
    P = DARK
    d = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{label}">'
         + ground_defs(DARK, "g", W, h) + f'<rect width="{W}" height="{h}" fill="url(#g)"/>' + body_fn() + '</svg>')
    P = LIGHT
    l = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{label}">'
         + ground_defs(LIGHT, "g", W, h) + f'<rect width="{W}" height="{h}" fill="url(#g)"/>' + body_fn() + '</svg>')
    write_pair(name, d, l)

# ══ 1. drift diagram (Background) ═════════════════════════════
def drift():
    b = []
    b.append(f'<path d="M330 180 C 480 120, 560 250, 700 230 S 950 90, 1090 170 S 1230 240, 1280 165" '
             f'fill="none" stroke="{P["sub"]}" stroke-width="1.6" stroke-dasharray="2 7" stroke-linecap="round"/>')
    for (tx, ty) in [(470,158),(610,242),(760,196),(920,112),(1050,150),(1210,236)]:
        b.append(f'<circle cx="{tx}" cy="{ty}" r="3" fill="{P["dim"]}"/>')
    b.append(text("iterations · constraints · other people's opinions", 17, "ita", P["dim"], x=1000, y=76, anchor="middle")[0])
    b.append(f'<circle cx="330" cy="180" r="7" fill="{P["gold"]}"/>')
    b.append(f'<circle cx="330" cy="180" r="13" fill="none" stroke="{P["gold"]}" stroke-width="1" opacity="0.4"/>')
    b.append(f'<circle cx="1280" cy="180" r="9" fill="{P["node"]}" stroke="{P["node_stroke"]}" stroke-width="1.6"/>')
    b.append(text("where it arrived", 15, "mono", P["sub"], x=1280, y=225, anchor="middle")[0])
    b.append(f'<path d="M1268 196 C 1150 320, 480 320, 348 208" fill="none" stroke="{P["gold"]}" '
             f'stroke-width="2.2" stroke-dasharray="6 5"/>')
    b.append(f'<g transform="translate(344,206) rotate(-140)"><path d="M-9 -6 L9 0 L-9 6 Z" fill="{P["gold"]}"/></g>')
    b.append(text("R1 · traces every choice back to its origin", 17, "mono", P["gold"], x=800, y=338, anchor="middle")[0])
    b.append(f'<line x1="330" y1="116" x2="1280" y2="116" stroke="{P["gold"]}" stroke-width="1.6" opacity="0.75"/>')
    b.append(ribbon_snippet("loop-feel", 1225, 76))
    b.append(text("R2 · the feeling, named at the start and held constant", 17, "ita", P["gold_hi"], x=560, y=88, anchor="middle")[0])
    b.append(text("the origin", 15, "mono", P["gold"], x=300, y=248, anchor="middle")[0])
    return "".join(b)

# ══ 2. doors (Install routes) ═════════════════════════════════
def doors():
    routes = [
        ("Claude Code", "claude --plugin-dir ./With-Love-Math"),
        ("Hermes Agent", "hermes plugins install"),
        ("Codex", "plugin browser + marketplace"),
        ("Cursor", "Customize page, or ~/.cursor/plugins/local"),
        ("GitHub Copilot", "copilot plugin install / VS Code"),
        ("Pi Agent", "clone into ~/.pi/agent/skills/"),
        ("Any SKILL.md agent", "copy a skills/ folder"),
    ]
    b = []
    cw, chh, gap = 340, 150, 22
    x0, y0 = 66, 56
    for i, (agent, route) in enumerate(routes):
        r, c = divmod(i, 4)
        x = x0 + c * (cw + gap); y = y0 + r * (chh + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{chh}" rx="10" fill="{P["card"]}" stroke="{P["card_stroke"]}" stroke-width="1.4"/>')
        b.append(ribbon_snippet("install", x + 22, y + 22))
        b.append(text(agent, 26, "ser", P["text"], x=x + 104, y=y + 58)[0])
        lines = wrap_lines(route, 15, "mono", cw - 60)
        yy = y + 98
        for ln in lines:
            b.append(text(ln, 15, "mono", P["sub"], x=x + 24, y=yy)[0]); yy += 24
    b.append(text("clone once — every route starts from the same repository", 18, "ita", P["dim"], x=W/2, y=428, anchor="middle")[0])
    return "".join(b)

# ══ 3. commands (Usage) ═══════════════════════════════════════
def commands():
    cards = [
        ("/decide", "Run a decision through the full framework", "verdict: Aligned / Needs Revision"),
        ("/diagnose", "Audit an existing project against R1-R4", "prescription with first step"),
        ("/map", "Map a project onto the ten-position map", "filled map plus gaps"),
        ("/teach", "Teach the framework, adapted to the learner", None),
        ("/lexicon", "Define the framework's terms", None),
    ]
    b = []
    cw, gap = 276, 15
    x0 = (W - (5 * cw + 4 * gap)) / 2
    y0, chh = 64, 290
    for i, (cmd, does, out) in enumerate(cards):
        x = x0 + i * (cw + gap)
        b.append(f'<rect x="{x:.0f}" y="{y0}" width="{cw}" height="{chh}" rx="10" fill="{P["card"]}" stroke="{P["card_stroke"]}" stroke-width="1.4"/>')
        b.append(text("COMMAND", 12, "mono", P["dim"], x=x + 22, y=y0 + 34, tracking=3)[0])
        b.append(text(cmd, 27, "mono", P["gold"], x=x + 22, y=y0 + 72)[0])
        b.append(f'<line x1="{x+22:.0f}" y1="{y0+94}" x2="{x+cw-22:.0f}" y2="{y0+94}" stroke="{P["card_stroke"]}" stroke-width="1"/>')
        desc, yend = wrapped(does, 19, "ser", P["text"], x + cw / 2, y0 + 132, 27, cw - 44)
        b.append(desc)
        if out:
            yy = yend + 18
            for ln in wrap_lines(out, 14, "mono", cw - 44):
                b.append(text(ln, 14, "mono", P["sub"], x=x + 22, y=yy)[0]); yy += 21
        b.append(ribbon_snippet("usage", x + cw - 74, y0 + chh - 74))
    b.append(text("five doors, one house — the same procedures are reachable in words", 18, "ita", P["dim"], x=W/2, y=402, anchor="middle")[0])
    return "".join(b)

# ══ pillars — four parallel principle callouts ════════════════
def pillars():
    data = [
        ("r1-grounding", "R1", "Recursive Grounding", "Why am I doing this?", "Every decision traces back to its origin."),
        ("r2-invariant", "R2", "Emotion as Invariant", "What feeling must I preserve?", "A chosen feeling survives every iteration unchanged."),
        ("r3-unity", "R3", "Distinction Within Unity", "How do these parts make one whole?", "Parts stay individually legible while cohering."),
        ("r4-scale", "R4", "Scale the Invariance", "Does this work at every size?", "Integrity holds from 2-inch icon to 10-foot mural."),
    ]
    b = []
    cw, gap = 351, 18
    x0 = (W - (4 * cw + 3 * gap)) / 2
    y0, chh = 44, 348
    for i, (icon, tag, name, q, en) in enumerate(data):
        x = x0 + i * (cw + gap)
        b.append(f'<rect x="{x:.0f}" y="{y0}" width="{cw}" height="{chh}" rx="10" fill="{P["card"]}" stroke="{P["card_stroke"]}" stroke-width="1.4"/>')
        b.append(f'<rect x="{x:.0f}" y="{y0}" width="{cw}" height="6" rx="3" fill="{P["gold"]}" opacity="{0.9 if i==0 else 0.55}"/>')
        b.append(ribbon_snippet(icon, x + 24, y0 + 30))
        b.append(text(tag, 21, "mono", P["gold"], x=x + cw - 64, y=y0 + 62)[0])
        b.append(text(name, 27, "ser", P["text"], x=x + 24, y=y0 + 144)[0])
        b.append(text('"' + q + '"', 21, "ita", P["gold_hi"], x=x + 24, y=y0 + 186)[0])
        b.append(f'<line x1="{x+24:.0f}" y1="{y0+210}" x2="{x+cw-24:.0f}" y2="{y0+210}" stroke="{P["card_stroke"]}" stroke-width="1"/>')
        b.append(wrapped(en, 17, "ser", P["sub"], x + cw / 2, y0 + 246, 25, cw - 48)[0])
    return "".join(b)

# ══ loop cycle ════════════════════════════════════════════════
def loop():
    cx, cy, R = W / 2, 232, 156
    nodes = [("loop-why", "WHY", 90), ("loop-who", "WHO", 0), ("loop-feel", "FEEL", 270), ("loop-evoke", "EVOKE", 180)]
    b = []
    import math
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{P["gold"]}" stroke-width="1.6" opacity="0.4" stroke-dasharray="1 6" stroke-linecap="round"/>')
    for (ax, ay, rot) in [(cx + R*0.7071, cy - R*0.7071, 45), (cx + R*0.7071, cy + R*0.7071, 135),
                          (cx - R*0.7071, cy + R*0.7071, -135), (cx - R*0.7071, cy - R*0.7071, -45)]:
        b.append(f'<g transform="translate({ax:.1f},{ay:.1f}) rotate({rot})"><path d="M-9 -6 L9 0 L-9 6 Z" fill="{P["gold"]}" opacity="0.85"/></g>')
    r2 = R - 62
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r2}" fill="none" stroke="{P["gold"]}" stroke-width="1.3" stroke-dasharray="6 5" opacity="0.55"/>')
    b.append(f'<g transform="translate({cx:.1f},{cy - r2:.1f}) rotate(0)"><path d="M-9 -6 L9 0 L-9 6 Z" fill="{P["gold"]}"/></g>')
    b.append(text("∞", 44, "ser", P["gold"], x=cx, y=cy - 6, anchor="middle")[0])
    b.append(text("R1 · return to the origin", 14, "mono", P["sub"], x=cx, y=cy + 24, anchor="middle")[0])
    b.append(text("the loop is infinite; it always returns", 15, "ita", P["dim"], x=cx, y=cy + 50, anchor="middle")[0])
    for n, (icon, name, ang) in enumerate(nodes, 1):
        a = math.radians(ang)
        nx = cx + R * math.cos(a); ny = cy - R * math.sin(a)
        gold_node = icon == "loop-why"
        b.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="56" fill="{P["card"]}" stroke="{P["gold"] if gold_node else P["node_stroke"]}" stroke-width="{2.2 if gold_node else 1.4}"/>')
        b.append(ribbon_snippet(icon, nx - 24, ny - 46))
        b.append(text(name, 19, "mono", P["text"], x=nx, y=ny + 34, anchor="middle")[0])
        b.append(f'<circle cx="{nx+42:.1f}" cy="{ny-42:.1f}" r="12" fill="{P["node_gold"]}" stroke="{P["gold"]}" stroke-width="1.2"/>')
        b.append(text(str(n), 15, "mono", P["gold_hi"], x=nx + 42, y=ny - 37, anchor="middle")[0])
    return "".join(b)

# ══ ten-position map — two axes ═══════════════════════════════
def themap():
    cx, cy = W / 2, 224
    b = []
    b.append(f'<line x1="130" y1="{cy}" x2="1430" y2="{cy}" stroke="{P["gold"]}" stroke-width="1.4" opacity="0.7"/>')
    b.append(f'<path d="M1430 {cy} L1416 {cy-7} L1416 {cy+7} Z" fill="{P["gold"]}"/>')
    b.append(f'<line x1="{cx}" y1="52" x2="{cx}" y2="396" stroke="{P["gold"]}" stroke-width="1.4" opacity="0.7"/>')
    b.append(f'<path d="M{cx} 396 L{cx-7} 382 L{cx+7} 382 Z" fill="{P["gold"]}"/>')
    b.append(text("the sequence you run", 15, "mono", P["gold_dim"], x=1424, y=cy - 74, anchor="end")[0])
    b.append(text("the depth it reads at", 14, "mono", P["gold_dim"], x=cx + 14, y=412, anchor="start")[0])
    xs = {1: 180, 2: 400, 3: 610, 4: 950, 5: 1155, 10: 1390}
    names = {1: ("P1", "State the Goal", "< 5 words"), 2: ("P2", "WHY", None), 3: ("P3", "WHO", None),
             4: ("P4", "FEEL", None), 5: ("P5", "EVOKE", None), 10: ("P10", "Find the Math", "the terminal move")}
    for p, x in xs.items():
        tag, nm, sub = names[p]
        terminal = p == 10
        goal = p == 1
        if goal:
            b.append(f'<rect x="{x-24}" y="{cy-24}" width="48" height="48" rx="6" fill="{P["node"]}" stroke="{P["node_stroke"]}" stroke-width="1.6"/>')
        else:
            r = 30 if terminal else 24
            b.append(f'<circle cx="{x}" cy="{cy}" r="{r}" fill="{P["node_gold"] if terminal else P["node"]}" stroke="{P["gold"] if terminal else P["node_stroke"]}" stroke-width="{2.4 if terminal else 1.5}"/>')
            if terminal:
                b.append(f'<circle cx="{x}" cy="{cy}" r="36" fill="none" stroke="{P["gold"]}" stroke-width="1" opacity="0.35"/>')
        # tag above the halo, name below it (clear of both)
        b.append(text(tag, 14, "mono", P["gold"], x=x, y=cy - 52, anchor="middle")[0])
        b.append(text(nm, 20, "ser", P["text"], x=x, y=cy + 70, anchor="middle")[0])
        if sub:
            b.append(text(sub, 14, "ita", P["dim"], x=x, y=cy + 94, anchor="middle")[0])
    vpos = [(95, "P7", "R2 · Emotion as Invariant"), (163, "P6", "R1 · Recursive Grounding"),
            (292, "P8", "R3 · Distinction Within Unity"), (360, "P9", "R4 · Scale the Invariance")]
    for y, tag, nm in vpos:
        b.append(f'<circle cx="{cx}" cy="{y}" r="24" fill="{P["node"]}" stroke="{P["node_stroke"]}" stroke-width="1.5"/>')
        b.append(text(tag, 14, "mono", P["gold"], x=cx, y=y + 5, anchor="middle")[0])
        # labels alternate sides to stay clear of the horizontal-line nodes
        if tag == "P8":
            # below-left diagonal: keeps clear of WHO (left) and FEEL (right) labels
            b.append(text(nm, 19, "ser", P["text"], x=cx - 30, y=y + 48, anchor="end")[0])
        else:
            b.append(text(nm, 19, "ser", P["text"], x=cx + 40, y=y + 7, anchor="start")[0])
    return "".join(b)

# ══ layers — four altitudes ═══════════════════════════════════
def layers():
    data = [
        ("I", "Design Philosophy", "physical, practical", 1370, 300),
        ("II", "Self-Help / Self-Love", "emotional, psychological", 1000, 226),
        ("III", "Math in Nature", "intellectual, structural", 640, 152),
        ("IV", "Esotericism", "spiritual, transcendent", 300, 80),
    ]
    cx, cy = W / 2, 216
    b = []
    for i, (rn, nm, sub, w_, h_) in enumerate(data):
        x = cx - w_ / 2; y = cy - h_ / 2
        op = [0.30, 0.45, 0.65, 1.0][i]
        b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w_}" height="{h_}" rx="14" fill="none" stroke="{P["gold"]}" stroke-width="{1.2 if i<3 else 1.8}" opacity="{op}"/>')
        # label sits just above the top edge, left-aligned with the rect
        ly = y - 14
        b.append(text(rn, 19, "ser", P["gold_hi"], x=x + 4, y=ly)[0])
        b.append(text(nm, 23, "ser", P["text"], x=x + 44, y=ly)[0])
        b.append(text("— " + sub, 19, "ita", P["dim"], x=x + 44 + len(nm) * 11.8 + 14, y=ly)[0])
    b.append(text("any element can be read at any layer — a good decision holds at all four", 18, "ita", P["dim"], x=W/2, y=412, anchor="middle")[0])
    return "".join(b)

# ══ WONDER anchor plate ═══════════════════════════════════════
def wonder():
    b = []
    b.append(frame(W, 330, inset=18))
    b.append(frame(W, 330, inset=26))
    b.append(corner_ticks(W, 330, m=18, L=40))
    b.append(ribbon_snippet("wonder", W/2 - 32, 44))
    b.append(text("WONDER", 84, "ser", P["gold_hi"], x=W/2, y=222, anchor="middle", tracking=10)[0])
    b.append(f'<rect x="{W/2-220}" y="244" width="440" height="2" fill="{P["gold"]}" opacity="0.6"/>')
    b.append(text("If a decision, design, or project does not evoke wonder, it has not yet passed.", 24, "ita", P["sub"], x=W/2, y=286, anchor="middle")[0])
    return "".join(b)

# ══ architecture — portability split ══════════════════════════
def architecture():
    b = []
    def card(x, w_, title, chips_rows):
        y0, h_ = 78, 290
        s = [f'<rect x="{x}" y="{y0}" width="{w_}" height="{h_}" rx="10" fill="{P["card"]}" stroke="{P["card_stroke"]}" stroke-width="1.4"/>']
        s.append(text(title, 16, "mono", P["gold"], x=x + 26, y=y0 + 40, tracking=2)[0])
        s.append(f'<line x1="{x+26}" y1="{y0+56}" x2="{x+w_-26}" y2="{y0+56}" stroke="{P["card_stroke"]}" stroke-width="1"/>')
        yy = y0 + 88
        for main, note in chips_rows:
            s.append(f'<rect x="{x+26}" y="{yy-24}" width="{w_-52}" height="46" rx="6" fill="{P["node"]}" stroke="{P["node_stroke"]}" stroke-width="1"/>')
            s.append(text(main, 18, "mono", P["text"], x=x + 42, y=yy + 6)[0])
            if note:
                s.append(text(note, 14, "ita", P["dim"], x=x + w_ - 30, y=yy + 6, anchor="end")[0])
            yy += 62
        return "".join(s)
    b.append(card(66, 690, "PORTABLE — every client reads these", [
        ("plugin.json", "Agent Plugins 1.0.0 manifest"),
        ("skills/", "decision-engine · diagnostic · tutor · lexicon"),
    ]))
    b.append(card(804, 690, "CLIENT-NAMESPACED — ignored if unimplemented", [
        ("com.anthropic.claude/", "commands · agents · hooks"),
        ("com.github.copilot/", "the same, in Copilot's formats"),
        (".codex-plugin · .cursor-plugin", "per-agent adapters"),
    ]))
    b.append(f'<line x1="772" y1="120" x2="788" y2="120" stroke="{P["gold"]}" stroke-width="1.4"/>')
    b.append(f'<line x1="780" y1="120" x2="780" y2="330" stroke="{P["gold"]}" stroke-width="1.4" stroke-dasharray="3 5"/>')
    b.append(f'<line x1="772" y1="330" x2="788" y2="330" stroke="{P["gold"]}" stroke-width="1.4"/>')
    b.append(text("one repository — the split is what keeps the package portable", 18, "ita", P["dim"], x=W/2, y=414, anchor="middle")[0])
    return "".join(b)

# ── render everything under both palettes ─────────────────────
plates = [
    ("plate-00", "Watch the Showcase", "00", "showcase", "Sixty-four seconds: the four principles, the loop, and the invariant in motion."),
    ("plate-01", "Background", "01", "background", "Most work starts with a reason and a feeling, and then loses both."),
    ("plate-02", "Install", "02", "install", "No build step, no package manager, no runtime dependencies."),
    ("plate-03", "Usage", "03", "usage", "Five commands, stable and minimal; each dispatches to a skill or subagent."),
    ("plate-04", "The Framework", "04", "framework", "Four principles, one loop, one map, four layers, one invariant."),
    ("plate-05", "Architecture", "05", "architecture", "Four layers of packaging, each doing a distinct job."),
    ("plate-06", "Colophon", "06", "wonder", "Maintainers, contributing, license — the framework is meant to be passed on."),
]
for name, title, num, icon, keyline in plates:
    P = DARK
    d = plate(title, num, icon, keyline)
    P = LIGHT
    l = plate(title, num, icon, keyline)
    write_pair(name, d, l)

arts = [
    ("art-drift", drift, 380, "A decision drifts from its origin; R1 traces it back and R2 holds the feeling constant."),
    ("art-doors", doors, 470, "Seven install routes, one repository: Claude Code, Hermes Agent, Codex, Cursor, GitHub Copilot, Pi Agent, and any SKILL.md agent."),
    ("art-commands", commands, 440, "Five commands: /decide, /diagnose, /map, /teach, /lexicon."),
    ("art-pillars", pillars, 440, "The four principles: R1 Recursive Grounding, R2 Emotion as Invariant, R3 Distinction Within Unity, R4 Scale the Invariance."),
    ("art-loop", loop, 470, "The decisioning loop: WHY, WHO, FEEL, EVOKE, returning forever."),
    ("art-map", themap, 460, "The ten-position map as two axes: the sequence you run, and the depth it reads at."),
    ("art-layers", layers, 460, "The four layers: Design Philosophy, Self-Help and Self-Love, Math in Nature, Esotericism."),
    ("art-wonder", wonder, 330, "The invariant: WONDER. If a decision, design, or project does not evoke wonder, it has not yet passed."),
    ("art-architecture", architecture, 460, "The packaging split: portable content and client-namespaced content, side by side."),
]
for name, fn, h, label in arts:
    art(name, h, fn, label)
print("all plates + art written")