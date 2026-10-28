from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
OUT = ROOT / "mechanics-first-levels"
OUT.mkdir(exist_ok=True)

COLORS = ["#25D9FF", "#FF3D71", "#FFD83D", "#A855F7", "#32E875", "#FF7A2F"]

def centered_bands(widths, start_row=1):
    return [(start_row + i, (30 - width) // 2, (30 - width) // 2 + width) for i, width in enumerate(widths)]

# Dense horizontal arrow bands deliberately leave meaningful negative-space bands.
# Each piece is a single straight path with one right-facing terminal head.
LEVELS = {
    "flame": centered_bands([8, 12, 16, 20, 24, 28, 30, 30, 30, 28, 28, 28, 26, 26, 26, 24, 24, 24, 22, 22, 22, 20, 20, 18, 16, 14, 12, 10]),
    "tree": [(r, 0, 30) for r in range(3, 17)] + [(r, 4, 26) for r in range(17, 23)] + [(r, 11, 19) for r in range(23, 29)],
    "mountain": centered_bands([8, 12, 16, 20, 24, 28, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 28, 26, 26, 24, 24, 22, 22, 20, 20, 18, 18]),
    "rocket": [(r, 5, 25) for r in range(2, 7)] + [(r, 2, 28) for r in range(7, 12)] + [(r, 0, 30) for r in range(12, 20)] + [(r, 3, 27) for r in range(20, 26)] + [(r, 7, 23) for r in range(26, 29)],
    "cloud": [(r, 3, 27) for r in range(3, 7)] + [(r, 0, 30) for r in range(7, 20)] + [(r, 2, 28) for r in range(20, 25)] + [(r, 6, 24) for r in range(25, 29)],
}

def make_pieces(level_id: str, bands: list[tuple[int, int, int]]):
    pieces = []
    grid = [["." for _ in range(30)] for _ in range(30)]
    idx = 0
    for row, start, end in bands:
        cursor = start
        while cursor < end:
            length = min(8, end - cursor)
            if length < 3:
                break
            cells = [[row, c] for c in range(cursor, cursor + length)]
            pid = f"{level_id[:2].upper()}{idx:02d}"
            color = COLORS[idx % len(COLORS)]
            pieces.append({"id": pid, "shape": "line", "direction": "right", "color": color, "cells": cells})
            for rr, cc in cells:
                if grid[rr][cc] != ".":
                    raise ValueError(f"overlap at {rr},{cc}")
                grid[rr][cc] = pid
            idx += 1
            cursor += length + 1  # one-cell separation between pieces
    occupied = sum(cell != "." for row in grid for cell in row)
    return pieces, grid, occupied

def render(level_id, pieces, grid, occupied):
    cell = 24
    left, top = 72, 118
    width, height = left + 30 * cell + 40, top + 30 * cell + 90
    image = Image.new("RGB", (width, height), "#0B1020")
    draw = ImageDraw.Draw(image)
    font_path = "C:/Windows/Fonts/arial.ttf"
    bold_path = "C:/Windows/Fonts/arialbd.ttf"
    font = lambda size, bold=False: ImageFont.truetype(bold_path if bold else font_path, size)
    draw.text((32, 28), f"{level_id.upper()} — MECHANICS-FIRST BLUEPRINT", fill="#F5F7FF", font=font(22, True))
    draw.text((32, 62), f"30×30 grid  |  {len(pieces)} arrows  |  {occupied}/900 occupied cells ({occupied/900:.0%})", fill="#9EB2D5", font=font(14))
    for i in range(31):
        x, y = left + i * cell, top + i * cell
        draw.line((x, top, x, top + 30 * cell), fill="#273451", width=1)
        draw.line((left, y, left + 30 * cell, y), fill="#273451", width=1)
    for p in pieces:
        coords = p["cells"]
        color = p["color"]
        for r, c in coords:
            x, y = left + c * cell + 2, top + r * cell + 2
            draw.rounded_rectangle((x, y, x + cell - 4, y + cell - 4), radius=5, fill=color)
        r, c = coords[-1]
        cx, cy = left + c * cell + cell // 2, top + r * cell + cell // 2
        draw.polygon([(cx + 8, cy), (cx - 4, cy - 8), (cx - 4, cy + 8)], fill="#07101C")
    draw.text((32, height - 48), "Each colored run is one arrow: blunt tail → one terminal head. Gaps are intentional composition space.", fill="#AFC0DE", font=font(13))
    return image

for level_id, bands in LEVELS.items():
    pieces, grid, occupied = make_pieces(level_id, bands)
    blueprint = {
        "level_id": f"{level_id}-30x30-mechanics-v1",
        "grid": [30, 30],
        "purpose": "mechanics-first foundation for later picture composition",
        "occupancy": {"occupied_cells": occupied, "total_cells": 900, "ratio": round(occupied / 900, 3)},
        "pieces": pieces,
        "checks": {
            "overlap": False,
            "within_grid": True,
            "one_terminal_head_per_piece": True,
            "single_color_per_piece": True,
            "branches_or_loops": False,
            "picture_layer": "not applied yet",
        },
    }
    (OUT / f"{level_id}-30x30.json").write_text(json.dumps(blueprint, indent=2), encoding="utf-8")
    render(level_id, pieces, grid, occupied).save(OUT / f"{level_id}-30x30.png")

print(json.dumps({"output": str(OUT.resolve()), "levels": list(LEVELS), "files": len(LEVELS) * 2}))
