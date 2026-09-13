# The icon family — one system: 48-unit grid, 2.4 stroke, round caps/joins,
# gold #c9a227 on dark / #8a6f1f on light, geometric marks (line + arc + rect),
# optional single filled accent. Deep Surfaces ribbon variants: 64x64 near-black
# plate, hairline gold inner stroke, mark centered at 48-unit scale.
import os, subprocess

A = "/home/aboveaveragerob/With-Love-Math/.github/assets/icons"
os.makedirs(A, exist_ok=True)

GOLD = "#c9a227"
INK = "#0a0a0c"

def svg(body, size=48, ribbon=False, extra=""):
    if ribbon:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="10" fill="{INK}"/>
  <rect x="4.5" y="4.5" width="55" height="55" rx="7" fill="none" stroke="{GOLD}" stroke-opacity="0.20" stroke-width="1"/>
  <g transform="translate(8,8)">{body}</g>{extra}
</svg>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">{body}{extra}</svg>'''

S = 'fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
def g(paths, c=GOLD, extra_fill=""):
    return f'<g {S.format(c=c)}>{paths}</g>'

# ── loop phases ─────────────────────────────────────────────
ICONS = {}

ICONS["loop-why"] = g(
    '<circle cx="20" cy="24" r="3.2" fill="{c}" stroke="none"/>'.format(c=GOLD) +
    '<path d="M27 15 A12.7 12.7 0 0 1 27 33"/><path d="M31.5 9 A20 20 0 0 1 31.5 39"/>'
)

ICONS["loop-who"] = g(
    '<circle cx="19" cy="16" r="6"/><path d="M8 38 C8 29 13 25 19 25 C25 25 30 29 30 38"/>'
    '<circle cx="33" cy="18" r="4.8"/><path d="M31 27.5 C36.5 27 41 30.5 41 37"/>'
)

ICONS["loop-feel"] = g(
    '<path d="M24 39 C14.5 30.5 10.5 22.5 15 16.5 C18.5 12 24 15 24 19.5 C24 15 29.5 12 33 16.5 C37.5 22.5 33.5 30.5 24 39 Z"/>'
)

ICONS["loop-evoke"] = g(
    '<circle cx="24" cy="24" r="4" fill="{c}" stroke="none"/>'.format(c=GOLD) +
    '<path d="M24 9 V15 M24 33 V39 M9 24 H15 M33 24 H39"/>'
    '<path d="M13.2 13.2 L17.4 17.4 M30.6 17.4 L34.8 13.2 M13.2 34.8 L17.4 30.6 M30.6 30.6 L34.8 34.8"/>'
)

# ── principles R1-R4 ────────────────────────────────────────
ICONS["r1-grounding"] = g(
    '<circle cx="24" cy="10" r="2.6" fill="{c}" stroke="none"/>'.format(c=GOLD) +
    '<path d="M24 13 V30"/><path d="M24 30 C18.5 33 15 37 13.5 42"/><path d="M24 30 C29.5 34 33 37 34.5 42"/>'
    '<path d="M24 22 C20 23.5 17.5 26 16.5 29.5"/>'
)

ICONS["r2-invariant"] = g(
    '<path d="M6 24 H14 M34 24 H42"/>'
    '<path d="M24 15 L30.5 24 L24 33 L17.5 24 Z"/>'
    '<circle cx="24" cy="24" r="1.6" fill="{c}" stroke="none"/>'.format(c=GOLD)
)

ICONS["r3-unity"] = g(
    '<circle cx="15.5" cy="24" r="8.5"/><circle cx="24" cy="24" r="8.5"/><circle cx="32.5" cy="24" r="8.5"/>'
)

ICONS["r4-scale"] = g(
    '<rect x="9" y="9" width="30" height="30" rx="2"/><rect x="17" y="17" width="14" height="14" rx="1.5"/>'
    '<circle cx="24" cy="24" r="2.4" fill="{c}" stroke="none"/>'.format(c=GOLD)
)

ICONS["find-math"] = g(
    '<path d="M13 15 H35"/><path d="M17.5 15 C17.5 24 16.5 30 14.5 35"/><path d="M30.5 15 C30.5 24 32 29 35 32 M30.5 24 H23"/>'
)

# ── verdicts ────────────────────────────────────────────────
ICONS["verdict-aligned"] = g(
    '<circle cx="24" cy="24" r="15"/><path d="M17 24.5 L22 29.5 L31.5 19"/>'
)

ICONS["verdict-revision"] = g(
    '<path d="M15 19.5 A11.5 11.5 0 0 1 34.5 21.5"/><path d="M35 15.5 L34.9 21.9 L28.5 21.4"/>'
    '<path d="M33 28.5 A11.5 11.5 0 0 1 13.5 26.5"/><path d="M13 32.5 L13.1 25.6 L19.5 26.6"/>'
)

# section icons that must exist for the ribbon set (kept from the existing family)
KEEP = ["showcase", "background", "install", "usage", "framework", "architecture", "wonder"]

for name in KEEP:
    ICONS[name] = open(f"{A}/{name}.svg").read().split(">", 1)[1].rsplit("</svg>", 1)[0]

for name, body in ICONS.items():
    with open(f"{A}/{name}.svg", "w") as f:
        f.write(svg(body))
    with open(f"{A}/{name}-ribbon.svg", "w") as f:
        f.write(svg(body, ribbon=True))
print("icons written:", len(ICONS), "x2 (plain + ribbon)")