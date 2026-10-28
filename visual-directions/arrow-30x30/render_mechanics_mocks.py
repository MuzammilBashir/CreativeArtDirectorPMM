from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
SRC = ROOT / "mechanics-first-levels"
OUT = ROOT / "mechanics-first-levels"

W, H = 1080, 1920
BG = "#070B16"
BOARD = "#0B1222"
GRID = "#233552"
TEXT = "#F6F8FF"
MUTED = "#99AACC"

def font(size, bold=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("arialbd.ttf" if bold else "arial.ttf"), size)

def head(draw, x, y, size, color):
    draw.polygon([(x + size, y), (x, y - size * .62), (x, y + size * .62)], fill=color)

def render(path: Path, index: int):
    data = json.loads(path.read_text(encoding="utf-8"))
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    level_name = data["level_id"].split("-")[0].upper()
    pieces = data["pieces"]

    draw.text((72, 78), "ARROWS", fill=TEXT, font=font(44, True))
    draw.text((72, 132), f"LEVEL {index}", fill=MUTED, font=font(25, True))
    draw.text((790, 88), "♥  ♥  ♥", fill="#FF557D", font=font(33, True))
    draw.text((797, 140), "0 / %d CLEARED" % len(pieces), fill=MUTED, font=font(17, True))

    left, top, board = 75, 290, 930
    cell = board / 30
    draw.rounded_rectangle((left - 16, top - 16, left + board + 16, top + board + 16), radius=24, fill=BOARD, outline="#314A73", width=3)
    for i in range(31):
        x = left + i * cell
        y = top + i * cell
        draw.line((x, top, x, top + board), fill=GRID, width=1)
        draw.line((left, y, left + board, y), fill=GRID, width=1)

    first_id = pieces[0]["id"] if pieces else None
    for piece in pieces:
        color = piece["color"]
        selected = piece["id"] == first_id
        coords = piece["cells"]
        for r, c in coords:
            x0, y0 = left + c * cell + 2, top + r * cell + 2
            x1, y1 = left + (c + 1) * cell - 2, top + (r + 1) * cell - 2
            draw.rounded_rectangle((x0, y0, x1, y1), radius=7, fill=color)
            if selected:
                draw.rounded_rectangle((x0 - 2, y0 - 2, x1 + 2, y1 + 2), radius=9, outline="#FFFFFF", width=3)
        r, c = coords[-1]
        cx = left + (c + 0.5) * cell
        cy = top + (r + 0.5) * cell
        head(draw, cx + 5, cy, cell * .34, color)

    # Hand cursor on the highlighted first arrow.
    if pieces:
        r, c = pieces[0]["cells"][0]
        hx, hy = left + (c + .5) * cell, top + (r + .5) * cell
        draw.ellipse((hx - 22, hy - 22, hx + 22, hy + 22), fill="#FFFFFF", outline="#15233A", width=3)
        draw.line((hx + 12, hy + 12, hx + 56, hy + 62), fill="#FFFFFF", width=15)
        draw.line((hx + 12, hy + 12, hx + 56, hy + 62), fill="#DDE7F7", width=3)

    draw.text((72, 1320), "CLEAR THE BOARD", fill=TEXT, font=font(34, True))
    draw.text((72, 1372), "Tap an arrow with a clear path to the edge", fill=MUTED, font=font(22))
    card_y = 1490
    draw.rounded_rectangle((72, card_y, W - 72, card_y + 210), radius=24, fill="#121E38", outline="#2B4167", width=2)
    draw.text((110, card_y + 34), "BOARD PROGRESS", fill=MUTED, font=font(18, True))
    draw.text((110, card_y + 77), f"0 / {len(pieces)} arrows cleared", fill=TEXT, font=font(31, True))
    draw.rounded_rectangle((110, card_y + 142, W - 110, card_y + 169), radius=13, fill="#08101E")
    draw.rounded_rectangle((110, card_y + 142, 145, card_y + 169), radius=13, fill="#42D8FF")
    draw.text((72, 1800), f"{level_name.title()} picture foundation", fill="#B8C7E2", font=font(21))
    image.save(OUT / f"{path.stem}-mock.png")

for i, path in enumerate(sorted(SRC.glob("*.json")), start=1):
    render(path, i)
print("Rendered", len(list(SRC.glob("*-mock.png"))), "mocks")
