import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
level = json.loads((ROOT / "level-arrows-maze-30x30-v1.json").read_text(encoding="utf-8"))
W, H = 1080, 1920
image = Image.new("RGB", (W, H), "#111936")
draw = ImageDraw.Draw(image)
font = lambda n, b=False: ImageFont.truetype("C:/Windows/Fonts/" + ("arialbd.ttf" if b else "arial.ttf"), n)

draw.rounded_rectangle((48, 40, W - 48, H - 40), radius=38, fill="#182347", outline="#32446E", width=3)
draw.text((82, 92), "ARROWS", fill="#F4F7FF", font=font(42, True))
draw.text((82, 146), "LEVEL 1", fill="#9FB4DF", font=font(24, True))
draw.text((W - 330, 102), "♥  ♥  ♥", fill="#FF6B91", font=font(30, True))
draw.text((W - 310, 148), "3 MOVES LEFT", fill="#9FB4DF", font=font(18))

cell, board, left, top = 27, 810, 135, 360
draw.rounded_rectangle((left - 22, top - 22, left + board + 22, top + board + 22), radius=28, fill="#0C132B", outline="#3C4D78", width=4)
for i in range(31):
    x, y = left + i * cell, top + i * cell
    draw.line((x, top, x, top + board), fill="#25365D", width=1)
    draw.line((left, y, left + board, y), fill="#25365D", width=1)

def triangle(cx, cy, direction):
    s = 9
    if direction == "left": return [(cx-s, cy), (cx+s//2, cy-s), (cx+s//2, cy+s)]
    if direction == "right": return [(cx+s, cy), (cx-s//2, cy-s), (cx-s//2, cy+s)]
    if direction == "up": return [(cx, cy-s), (cx-s, cy+s//2), (cx+s, cy+s//2)]
    return [(cx, cy+s), (cx-s, cy-s//2), (cx+s, cy-s//2)]

for piece in level["pieces"]:
    coords = piece["cells"]
    for r, c in coords:
        x, y = left + c * cell + 2, top + r * cell + 2
        draw.rounded_rectangle((x, y, x + cell - 4, y + cell - 4), radius=6, fill=piece["color"])
    r0, c0 = coords[0]
    r1, c1 = coords[-1]
    r, c = (r0, (c0+c1)//2) if piece["direction"] in ("left", "right") else ((r0+r1)//2, c0)
    cx, cy = left + c * cell + cell//2, top + r * cell + cell//2
    draw.polygon(triangle(cx, cy, piece["direction"]), fill="#14203E")

first = level["clear_order"][0]
piece = next(p for p in level["pieces"] if p["id"] == first)
for r, c in piece["cells"]:
    x, y = left + c * cell + 1, top + r * cell + 1
    draw.rounded_rectangle((x, y, x + cell - 2, y + cell - 2), radius=7, outline="#FFFFFF", width=2)

draw.text((82, 1260), "FIND THE FREE ARROW", fill="#F4F7FF", font=font(32, True))
draw.text((82, 1312), "Tap an arrow with a clear path to the edge", fill="#AFC0E4", font=font(22))
card_y = 1450
draw.rounded_rectangle((82, card_y, W - 82, card_y + 210), radius=24, fill="#202E58", outline="#3C4D78", width=2)
draw.text((120, card_y + 32), "BOARD PROGRESS", fill="#94A9D4", font=font(18, True))
draw.text((120, card_y + 74), "0 / 15 arrows cleared", fill="#F4F7FF", font=font(30, True))
draw.rounded_rectangle((120, card_y + 135, W - 120, card_y + 162), radius=13, fill="#111936")
draw.rounded_rectangle((120, card_y + 135, 190, card_y + 162), radius=13, fill="#56CCF2")
draw.text((82, 1770), "A calm puzzle of order and timing", fill="#8095C0", font=font(20))
draw.text((82, 1810), "Tap to clear", fill="#6EE7B7", font=font(24, True))

out = ROOT / "mock-arrows-maze-30x30-v1.png"
image.save(out)
print(out.resolve())
