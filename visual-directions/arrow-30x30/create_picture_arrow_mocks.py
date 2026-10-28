from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent / "picture-arrow-mocks"
ROOT.mkdir(exist_ok=True)

W, H = 1080, 1920
BOARD = 900
LEFT, TOP = 90, 280
CELL = BOARD / 30
BG, GRID, TEXT, MUTED = "#080D1A", "#1D2C48", "#F6F8FF", "#9FB2D4"
COLORS = ["#FF3D71", "#FFCE3A", "#25D9FF", "#A855F7", "#35E879", "#FF7B39"]

# Every item is one polyline: one blunt tail at points[0], one terminal head at points[-1].
# Coordinates are 30x30 grid cells. These are picture silhouettes, not filled blocks.
LEVELS = {
    "flame": [
        ([(14,24),(11,22),(12,18),(10,15),(12,11),(11,7)], 0),
        ([(15,25),(16,21),(14,18),(16,15),(15,11),(17,7)], 1),
        ([(12,25),(9,22),(9,19),(7,17),(8,13),(6,11)], 2),
        ([(18,25),(21,22),(21,19),(23,17),(22,13),(24,10)], 3),
        ([(13,26),(12,23),(13,20),(12,17),(13,14),(12,11)], 4),
        ([(17,26),(18,23),(17,20),(18,17),(17,14),(18,11)], 5),
        ([(10,24),(7,22),(6,19),(5,16)], 0),
        ([(20,24),(23,22),(24,19),(25,16)], 1),
    ],
    "butterfly": [
        ([(15,17),(12,15),(9,14),(6,11),(5,7)], 0),
        ([(14,18),(11,18),(8,17),(5,14),(4,12)], 1),
        ([(14,20),(11,21),(8,22),(6,25)], 2),
        ([(15,21),(12,24),(9,26),(7,28)], 3),
        ([(16,17),(19,15),(22,14),(25,11),(26,7)], 4),
        ([(17,18),(20,18),(23,17),(26,14),(27,12)], 5),
        ([(17,20),(20,21),(23,22),(25,25)], 0),
        ([(16,21),(19,24),(22,26),(24,28)], 1),
        ([(15,15),(15,12),(15,9)], 2),
        ([(16,22),(16,25),(16,28)], 3),
    ],
    "brain": [
        ([(14,17),(11,16),(9,14),(9,11),(11,9),(10,6)], 0),
        ([(14,16),(12,13),(13,10),(12,7),(14,5)], 1),
        ([(14,18),(11,19),(10,22),(11,25),(9,27)], 2),
        ([(15,18),(14,21),(15,24),(14,27)], 3),
        ([(16,17),(19,16),(21,14),(21,11),(19,9),(20,6)], 4),
        ([(16,16),(18,13),(17,10),(18,7),(16,5)], 5),
        ([(16,18),(19,19),(20,22),(19,25),(21,27)], 0),
        ([(15,18),(16,21),(15,24),(16,27)], 1),
        ([(15,15),(15,12),(15,9),(15,6)], 2),
        ([(15,20),(15,23),(15,26)], 3),
    ],
    "rocket": [
        ([(15,25),(12,22),(12,18),(13,14),(15,9)], 0),
        ([(16,25),(19,22),(19,18),(17,14),(15,9)], 1),
        ([(14,23),(10,22),(8,24),(6,26)], 2),
        ([(17,23),(21,22),(23,24),(25,26)], 3),
        ([(15,20),(13,18),(14,15),(15,12)], 4),
        ([(16,20),(18,18),(17,15),(15,12)], 5),
        ([(14,26),(13,28)], 2),
        ([(17,26),(18,28)], 3),
    ],
    "leaf": [
        ([(15,26),(12,23),(9,20),(7,16),(6,12),(7,8)], 0),
        ([(16,26),(19,23),(22,20),(24,16),(25,12),(24,8)], 1),
        ([(15,25),(15,21),(15,17),(15,13),(15,9)], 2),
        ([(13,23),(10,21),(8,18),(7,14)], 3),
        ([(18,23),(21,21),(23,18),(24,14)], 4),
        ([(12,20),(10,17),(10,13),(11,10)], 5),
        ([(19,20),(21,17),(21,13),(20,10)], 0),
        ([(14,24),(12,27)], 1),
        ([(17,24),(19,27)], 2),
    ],
}

def fnt(n, bold=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("arialbd.ttf" if bold else "arial.ttf"), n)

def xy(cell):
    c, r = cell
    return LEFT + (c + .5) * CELL, TOP + (r + .5) * CELL

def arrowhead(draw, end, prev, color):
    ex, ey = xy(end); px, py = xy(prev)
    dx, dy = ex - px, ey - py
    mag = max((dx * dx + dy * dy) ** .5, 1)
    ux, uy = dx / mag, dy / mag
    s = 18
    bx, by = ex - ux * s, ey - uy * s
    nx, ny = -uy * 11, ux * 11
    draw.polygon([(ex + ux * 8, ey + uy * 8), (bx + nx, by + ny), (bx - nx, by - ny)], fill=color)

def render(name, paths, level_num):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((70, 68), "ARROWS", fill=TEXT, font=fnt(44, True))
    d.text((70, 122), f"LEVEL {level_num}", fill=MUTED, font=fnt(24, True))
    d.text((780, 78), "♥  ♥  ♥", fill="#FF557D", font=fnt(32, True))
    d.text((790, 130), f"0 / {len(paths)} CLEARED", fill=MUTED, font=fnt(17, True))
    d.rounded_rectangle((LEFT - 18, TOP - 18, LEFT + BOARD + 18, TOP + BOARD + 18), radius=24, fill="#0C1528", outline="#314A70", width=3)
    for i in range(31):
        x, y = LEFT + i * CELL, TOP + i * CELL
        d.line((x, TOP, x, TOP + BOARD), fill=GRID, width=1)
        d.line((LEFT, y, LEFT + BOARD, y), fill=GRID, width=1)
    for i, (points, color_idx) in enumerate(paths):
        color = COLORS[color_idx]
        pts = [xy(p) for p in points]
        d.line(pts, fill=color, width=15, joint="curve")
        d.ellipse((pts[0][0]-9, pts[0][1]-9, pts[0][0]+9, pts[0][1]+9), fill=color)
        arrowhead(d, points[-1], points[-2], color)
        if i == 0:
            d.line(pts, fill="#FFFFFF", width=3, joint="curve")
            d.ellipse((pts[0][0]-12, pts[0][1]-12, pts[0][0]+12, pts[0][1]+12), outline="#FFFFFF", width=3)
    d.text((70, 1290), "CLEAR THE PICTURE", fill=TEXT, font=fnt(34, True))
    d.text((70, 1342), "Tap an arrow when its path to the edge is free", fill=MUTED, font=fnt(22))
    d.rounded_rectangle((70, 1460, W-70, 1670), radius=24, fill="#121F39", outline="#2E456C", width=2)
    d.text((108, 1500), "BOARD PROGRESS", fill=MUTED, font=fnt(18, True))
    d.text((108, 1545), f"0 / {len(paths)} arrows cleared", fill=TEXT, font=fnt(31, True))
    d.rounded_rectangle((108, 1610, W-108, 1637), radius=13, fill="#07101F")
    d.rounded_rectangle((108, 1610, 143, 1637), radius=13, fill="#37D9FF")
    d.text((70, 1790), f"{name.title()} picture level", fill="#B8C7E2", font=fnt(21))
    im.save(ROOT / f"{name}-picture-mock.png")

for n, (name, paths) in enumerate(LEVELS.items(), start=1):
    render(name, paths, n)
print(f"Created {len(LEVELS)} picture mocks in {ROOT}")
