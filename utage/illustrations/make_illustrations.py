"""Generate the flat context illustrations used in the LP (deep blue earth-tone palette).

Writes one SVG per scene into the output directory; render them to PNG with
headless Chromium (see render_illustrations.sh).
"""
import sys, os

NAVY = "#1F3A52"; STEEL = "#2E5A73"; TEAL = "#4F7F91"; MIST = "#D8E3E9"
PALE = "#E7EDF0"; SAND = "#F5F2EC"; SAND2 = "#E9E1D3"; OCHRE = "#A8834F"
OCHRE_L = "#D9C3A0"; WHITE = "#FFFFFF"; INK = "#2F3A45"

W, H = 600, 450

def svg(body, bg=SAND):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="36"/></clipPath></defs>'
            f'<g clip-path="url(#c)"><rect width="{W}" height="{H}" fill="{bg}"/>{body}</g></svg>')

def leaf_plant(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M0,0 C-30,-40 -10,-90 0,-110 C10,-90 30,-40 0,0Z" fill="{TEAL}"/>'
            f'<path d="M0,0 C-55,-20 -70,-60 -62,-80 C-40,-70 -15,-40 0,0Z" fill="{STEEL}"/>'
            f'<path d="M0,0 C55,-20 70,-60 62,-80 C40,-70 15,-40 0,0Z" fill="{STEEL}"/>'
            f'<path d="M-28,0 h56 l-8,48 h-40z" fill="{OCHRE}"/></g>')

def laptop(x, y, s=1.0, screen=MIST):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="0" y="0" width="200" height="130" rx="10" fill="{NAVY}"/>'
            f'<rect x="10" y="10" width="180" height="110" rx="4" fill="{screen}"/>'
            f'<path d="M-25,130 h250 l-15,16 h-220z" fill="{STEEL}"/></g>')

def cup(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M0,0 h44 l-5,46 h-34z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
            f'<path d="M44,10 c16,0 16,22 -2,22" fill="none" stroke="{NAVY}" stroke-width="3"/>'
            f'<path d="M12,-10 c-6,-8 6,-14 0,-22 M28,-10 c-6,-8 6,-14 0,-22" fill="none" stroke="{TEAL}" stroke-width="3" stroke-linecap="round"/></g>')

def lines(x, y, n, w, gap=16, color=TEAL, h=6):
    return "".join(f'<rect x="{x}" y="{y+i*gap}" width="{w*(0.6 if i==n-1 else 1)}" height="{h}" rx="3" fill="{color}"/>' for i in range(n))

SCENES = {}

# 1. Working freely: window with sky, laptop, coffee, plant
SCENES["01_free_work"] = svg(
    f'<rect x="60" y="50" width="250" height="200" rx="14" fill="{MIST}"/>'
    f'<circle cx="240" cy="110" r="28" fill="{OCHRE_L}"/>'
    f'<path d="M60,215 q60,-60 120,-20 q50,-40 130,10 v35 h-250z" fill="{TEAL}" opacity=".55"/>'
    f'<rect x="60" y="50" width="250" height="200" rx="14" fill="none" stroke="{NAVY}" stroke-width="6"/>'
    f'<line x1="185" y1="50" x2="185" y2="250" stroke="{NAVY}" stroke-width="5"/>'
    f'<rect x="0" y="330" width="{W}" height="120" fill="{SAND2}"/>'
    + laptop(250, 200) + cup(130, 285) + leaf_plant(500, 285, 1.0) +
    f'<g transform="translate(270,222)">{lines(0,0,4,110,18,STEEL,7)}</g>')

# 2. AI + human editor: chat bubble with sparkle, document with editing pen
SCENES["02_ai_editor"] = svg(
    f'<rect x="250" y="70" width="230" height="300" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
    f'<g transform="translate(280,110)">{lines(0,0,9,170,26,MIST,9)}</g>'
    f'<rect x="280" y="188" width="120" height="9" rx="4" fill="{OCHRE_L}"/>'
    f'<path d="M282,268 q30,-14 60,0 t60,0" fill="none" stroke="{OCHRE}" stroke-width="4" stroke-linecap="round"/>'
    f'<g transform="translate(455,250) rotate(35)"><rect x="-10" y="-90" width="20" height="120" rx="4" fill="{OCHRE}"/>'
    f'<path d="M-10,30 h20 l-10,24z" fill="{NAVY}"/><rect x="-10" y="-90" width="20" height="18" fill="{NAVY}"/></g>'
    f'<path d="M60,90 h150 a20,20 0 0 1 20,20 v80 a20,20 0 0 1 -20,20 h-100 l-30,30 v-30 h-20 a20,20 0 0 1 -20,-20 v-80 a20,20 0 0 1 20,-20z" fill="{STEEL}"/>'
    f'<path d="M135,120 l9,24 24,9 -24,9 -9,24 -9,-24 -24,-9 24,-9z" fill="{WHITE}"/>'
    f'<path d="M182,118 l4,10 10,4 -10,4 -4,10 -4,-10 -10,-4 10,-4z" fill="{OCHRE_L}"/>'
    f'<circle cx="110" cy="320" r="46" fill="{MIST}"/><circle cx="110" cy="305" r="18" fill="{NAVY}"/>'
    f'<path d="M78,350 a32,30 0 0 1 64,0z" fill="{NAVY}"/>')

# 3. Feelings at night: window with moon & stars, glowing heart
SCENES["03_heart_night"] = svg(
    f'<rect x="70" y="50" width="460" height="260" rx="18" fill="{NAVY}"/>'
    f'<circle cx="430" cy="120" r="34" fill="{OCHRE_L}"/><circle cx="446" cy="108" r="30" fill="{NAVY}"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{WHITE}" opacity=".8"/>' for x, y, r in [(130,100,3),(200,80,2),(260,130,3),(340,90,2),(170,170,2),(500,200,2)]) +
    f'<rect x="70" y="50" width="460" height="260" rx="18" fill="none" stroke="{STEEL}" stroke-width="8"/>'
    f'<line x1="300" y1="50" x2="300" y2="310" stroke="{STEEL}" stroke-width="6"/>'
    f'<rect x="0" y="340" width="{W}" height="110" fill="{SAND2}"/>'
    f'<circle cx="300" cy="230" r="80" fill="{OCHRE_L}" opacity=".35"/>'
    f'<path d="M300,280 C240,240 230,200 250,180 C268,162 292,170 300,190 C308,170 332,162 350,180 C370,200 360,240 300,280Z" fill="{OCHRE}"/>'
    + cup(120, 300, 0.9) +
    f'<rect x="400" y="320" width="110" height="20" rx="4" fill="{STEEL}"/><rect x="410" y="300" width="90" height="20" rx="4" fill="{TEAL}"/>')

# 4. The wave reaching Japan: stylised wave and paper plane arcing across
SCENES["04_wave"] = svg(
    f'<circle cx="470" cy="110" r="44" fill="{OCHRE_L}"/>'
    f'<path d="M80,170 q120,-90 260,-40 t200,-20" fill="none" stroke="{STEEL}" stroke-width="4" stroke-dasharray="10 10"/>'
    f'<g transform="translate(330,118) rotate(-12)"><path d="M0,0 l60,-22 -20,52 -12,-18z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
    f'<path d="M28,12 l32,-34" stroke="{NAVY}" stroke-width="3"/></g>'
    f'<path d="M0,450 V300 C80,240 150,230 210,270 C250,296 240,340 200,336 C230,300 180,280 150,300 C120,320 140,360 190,370 C260,384 320,300 400,290 C480,280 540,320 600,300 V450Z" fill="{STEEL}"/>'
    f'<path d="M0,450 V360 C100,330 170,380 260,370 C360,360 420,330 600,360 V450Z" fill="{NAVY}"/>'
    f'<path d="M150,300 c-14,10 -10,30 8,34 M200,272 c18,14 12,40 -10,40" fill="none" stroke="{WHITE}" stroke-width="4" stroke-linecap="round" opacity=".8"/>')

# 5. Words at work: mail, browser page, phone with SNS, presentation
SCENES["05_office_words"] = svg(
    f'<rect x="60" y="60" width="270" height="190" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
    f'<rect x="60" y="60" width="270" height="34" rx="12" fill="{NAVY}"/>'
    + "".join(f'<circle cx="{82+i*18}" cy="77" r="5" fill="{c}"/>' for i, c in enumerate([OCHRE_L, MIST, WHITE])) +
    f'<rect x="80" y="110" width="110" height="80" rx="6" fill="{MIST}"/>'
    f'<g transform="translate(205,115)">{lines(0,0,4,105,18,TEAL,7)}</g>'
    f'<rect x="80" y="205" width="230" height="10" rx="5" fill="{MIST}"/><rect x="80" y="225" width="150" height="10" rx="5" fill="{MIST}"/>'
    f'<rect x="380" y="70" width="150" height="100" rx="8" fill="{OCHRE}"/><path d="M380,74 l75,55 75,-55" fill="none" stroke="{WHITE}" stroke-width="5" stroke-linejoin="round"/>'
    f'<rect x="400" y="200" width="110" height="200" rx="18" fill="{NAVY}"/><rect x="410" y="218" width="90" height="160" rx="6" fill="{PALE}"/>'
    + "".join(f'<path transform="translate({430+i*28},{300})" d="M0,10 C-12,2 -12,-10 -4,-12 C0,-13 0,-8 0,-6 C0,-8 0,-13 4,-12 C12,-10 12,2 0,10Z" fill="{c}"/>' for i, c in enumerate([STEEL, OCHRE, TEAL])) +
    f'<rect x="425" y="240" width="60" height="40" rx="4" fill="{MIST}"/>'
    f'<rect x="90" y="290" width="240" height="110" rx="8" fill="{PALE}" stroke="{NAVY}" stroke-width="4"/>'
    + "".join(f'<rect x="{120+i*45}" y="{380-h}" width="28" height="{h}" fill="{c}"/>' for i, h in enumerate([30, 50, 66, 80]) for c in [STEEL if i < 3 else OCHRE]) +
    f'<line x1="210" y1="400" x2="210" y2="430" stroke="{NAVY}" stroke-width="5"/>')

# 6. Spare-time work: desk lamp, laptop, calendar, moon outside
SCENES["06_night_desk"] = svg(
    f'<rect x="380" y="40" width="170" height="170" rx="12" fill="{NAVY}"/>'
    f'<circle cx="470" cy="110" r="28" fill="{OCHRE_L}"/><circle cx="484" cy="100" r="25" fill="{NAVY}"/>'
    f'<rect x="380" y="40" width="170" height="170" rx="12" fill="none" stroke="{STEEL}" stroke-width="6"/>'
    f'<rect x="70" y="60" width="150" height="140" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    f'<rect x="70" y="60" width="150" height="34" rx="10" fill="{STEEL}"/>'
    + "".join(f'<rect x="{86+(i%5)*26}" y="{106+(i//5)*24}" width="18" height="14" rx="3" fill="{OCHRE if i in (5,6,12,13) else MIST}"/>' for i in range(15)) +
    f'<rect x="0" y="330" width="{W}" height="120" fill="{SAND2}"/>'
    f'<path d="M150,330 v-80 l60,-70" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M190,160 l60,10 -20,50z" fill="{STEEL}"/><path d="M228,212 l60,70 -110,20z" fill="{OCHRE_L}" opacity=".45"/>'
    f'<rect x="120" y="322" width="64" height="12" rx="6" fill="{NAVY}"/>'
    + laptop(300, 200, 1.0, PALE) +
    f'<g transform="translate(320,222)">{lines(0,0,4,120,18,STEEL,7)}</g>')

# 7. Choosing your path: road forking into three under a sunrise
SCENES["07_crossroads"] = svg(
    f'<circle cx="300" cy="210" r="90" fill="{OCHRE_L}"/>'
    f'<path d="M0,230 q150,-40 300,0 t300,0 v220 h-600z" fill="{TEAL}" opacity=".6"/>'
    f'<path d="M0,270 q150,-30 300,0 t300,0 v180 h-600z" fill="{STEEL}"/>'
    f'<path d="M260,450 L290,270 h20 L340,450z" fill="{SAND}"/>'
    f'<path d="M290,330 L120,450 h60 L300,345z" fill="{SAND}"/>'
    f'<path d="M310,330 L480,450 h-60 L300,345z" fill="{SAND}"/>'
    f'<rect x="372" y="250" width="8" height="110" fill="{NAVY}"/>'
    f'<path d="M376,262 h70 l14,12 -14,12 h-70z" fill="{OCHRE}"/><path d="M376,296 h-70 l-14,12 14,12 h70z" fill="{NAVY}"/>'
    f'<path d="M376,330 h56 l12,10 -12,10 h-56z" fill="{WHITE}"/>')

# 8. Swipe files: stacked folders with a winning template card
SCENES["08_swipe_files"] = svg(
    f'<rect x="90" y="120" width="300" height="250" rx="14" fill="{STEEL}"/>'
    f'<path d="M90,134 a14,14 0 0 1 14,-14 h80 l20,22 h-114z" fill="{STEEL}"/>'
    f'<rect x="120" y="90" width="250" height="230" rx="10" fill="{MIST}" transform="rotate(-6 245 205)"/>'
    f'<rect x="140" y="80" width="250" height="250" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    f'<rect x="160" y="100" width="140" height="14" rx="7" fill="{NAVY}"/>'
    f'<g transform="translate(160,135)">{lines(0,0,3,200,22,MIST,9)}</g>'
    f'<rect x="160" y="210" width="90" height="70" rx="6" fill="{PALE}"/>'
    f'<g transform="translate(265,215)">{lines(0,0,3,100,20,TEAL,7)}</g>'
    f'<path d="M70,300 h340 a14,14 0 0 1 14,14 l-20,70 a14,14 0 0 1 -14,10 h-320 a14,14 0 0 1 -14,-14z" fill="{NAVY}"/>'
    f'<circle cx="470" cy="150" r="56" fill="{OCHRE}"/>'
    f'<path d="M444,150 l18,18 34,-36" fill="none" stroke="{WHITE}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M480,250 l8,20 22,2 -17,14 5,22 -18,-12 -18,12 5,-22 -17,-14 22,-2z" fill="{OCHRE_L}"/>')

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for name, s in SCENES.items():
        with open(os.path.join(out, name + ".svg"), "w") as f:
            f.write(s)
    print("\n".join(SCENES))
