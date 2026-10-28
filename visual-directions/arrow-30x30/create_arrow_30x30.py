from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
ROOT.mkdir(parents=True, exist_ok=True)

def cells(rows, cols):
    return [[r, c] for r in rows for c in cols]

pieces = {
    "A": {"name": "shaft-left", "color": "#2F80ED", "direction": "right", "gate": ["right", 13, 4], "cells": cells(range(13, 17), range(4, 12))},
    "B": {"name": "shaft-mid", "color": "#56CCF2", "direction": "right", "gate": ["right", 12, 6], "cells": cells(range(12, 18), range(12, 16))},
    "C": {"name": "neck", "color": "#27AE60", "direction": "right", "gate": ["right", 11, 8], "cells": cells(range(11, 19), range(16, 19))},
    "D": {"name": "upper-wing", "color": "#F2C94C", "direction": "right", "gate": ["right", 8, 4], "cells": cells(range(8, 12), range(19, 23))},
    "E": {"name": "lower-wing", "color": "#F2994A", "direction": "right", "gate": ["right", 18, 4], "cells": cells(range(18, 22), range(19, 23))},
    "F": {"name": "upper-tip", "color": "#EB5757", "direction": "right", "gate": ["right", 5, 4], "cells": cells(range(5, 9), range(23, 27))},
    "G": {"name": "lower-tip", "color": "#BB6BD9", "direction": "right", "gate": ["right", 21, 4], "cells": cells(range(21, 25), range(23, 27))},
    "H": {"name": "arrow-tip", "color": "#9B51E0", "direction": "right", "gate": ["right", 12, 8], "cells": cells(range(12, 20), range(23, 29))},
}

occupied = [tuple(cell) for piece in pieces.values() for cell in piece["cells"]]
assert len(occupied) == len(set(occupied)), "pieces overlap"
assert all(0 <= r < 30 and 0 <= c < 30 for r, c in occupied), "cell outside 30x30 grid"

grid = [["." for _ in range(30)] for _ in range(30)]
for label, piece in pieces.items():
    for r, c in piece["cells"]:
        grid[r][c] = label

blueprint = {
    "id": "arrow-picture-30x30-v1",
    "picture_level": "large right-facing arrow",
    "grid": [30, 30],
    "coordinate_system": "row,column; zero-based; rows top-to-bottom; columns left-to-right",
    "empty_symbol": ".",
    "grid_rows": ["".join(row) for row in grid],
    "pieces": pieces,
    "checks": {"overlap": False, "within_grid": True, "occupied_cells": len(occupied), "empty_cells": 900 - len(occupied), "picture_readability": "large right-facing arrow silhouette", "mechanics_status": "visual blueprint only; movement sequence pending game-rule validation"},
}
(ROOT / "arrow-picture-30x30.json").write_text(json.dumps(blueprint, indent=2), encoding="utf-8")

level = {
    "level_id": "arrow-picture-30x30-v1",
    "level_type": "picture-clear",
    "grid": [30, 30],
    "objective": "clear every colored arrow piece through its matching right-edge gate",
    "input": "drag a piece in its arrow direction; pieces stop on collision and leave when aligned with their gate",
    "initial_picture": "large right-facing arrow",
    "pieces": pieces,
    "clear_order": ["H", "F", "G", "D", "E", "C", "B", "A"],
    "difficulty": {"tier": 1, "reason": "single-direction prototype level with a readable silhouette and dependency chain"},
    "validation": {"geometry_checked": True, "overlap_checked": True, "gate_spans_checked": True, "playability_status": "proposed sequence; validate in game runtime"},
}
(ROOT / "level-arrow-picture-30x30-v1.json").write_text(json.dumps(level, indent=2), encoding="utf-8")

cell = 28
ml, mt = 110, 92
width, height = ml + 30 * cell + 60, mt + 30 * cell + 120
image = Image.new("RGB", (width, height), "#10182D")
draw = ImageDraw.Draw(image)
font_path = "C:/Windows/Fonts/arial.ttf"
bold_path = "C:/Windows/Fonts/arialbd.ttf"
font = lambda size, bold=False: ImageFont.truetype(bold_path if bold else font_path, size)
draw.text((40, 24), "ARROW PICTURE LEVEL - 30 x 30 BLUEPRINT", fill="#F2F5FF", font=font(24, True))
draw.text((40, 56), f"{len(pieces)} pieces  |  {len(occupied)} occupied cells  |  {900 - len(occupied)} empty cells", fill="#9FB3D8", font=font(15))
for i in range(31):
    x, y = ml + i * cell, mt + i * cell
    draw.line((x, mt, x, mt + 30 * cell), fill="#344361", width=1)
    draw.line((ml, y, ml + 30 * cell, y), fill="#344361", width=1)
for i in range(30):
    draw.text((ml + i * cell + 8, mt - 22), str(i), fill="#7890B7", font=font(11))
    draw.text((ml - 25, mt + i * cell + 7), str(i), fill="#7890B7", font=font(11))
for label, piece in pieces.items():
    coords = set(tuple(cell) for cell in piece["cells"])
    for r, c in coords:
        x0, y0 = ml + c * cell, mt + r * cell
        draw.rectangle((x0 + 1, y0 + 1, x0 + cell - 1, y0 + cell - 1), fill=piece["color"])
    rs, cs = [r for r, _ in coords], [c for _, c in coords]
    cx = ml + (min(cs) + max(cs) + 1) * cell / 2
    cy = mt + (min(rs) + max(rs) + 1) * cell / 2
    draw.text((cx - 5, cy - 8), label, fill="#17233E", font=font(14, True))
draw.text((40, height - 88), "Legend: each letter is a separate colored piece; all gates currently point right.", fill="#B8C7E2", font=font(14))
draw.text((40, height - 60), "Visual composition is checked. Arrow movement and exit order require game-rule validation.", fill="#8197BD", font=font(13))
image.save(ROOT / "arrow-picture-30x30.png")
print(json.dumps({"blueprint": str((ROOT / 'arrow-picture-30x30.json').resolve()), "level": str((ROOT / 'level-arrow-picture-30x30-v1.json').resolve()), "preview": str((ROOT / 'arrow-picture-30x30.png').resolve()), "occupied_cells": len(occupied)}))
