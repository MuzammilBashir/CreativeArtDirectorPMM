import json
from pathlib import Path

ROOT = Path(__file__).parent

def h(name, row, start, end, direction, color):
    return {"id": name, "shape": "line", "direction": direction, "color": color, "cells": [[row, c] for c in range(start, end + 1)]}

def v(name, col, start, end, direction, color):
    return {"id": name, "shape": "line", "direction": direction, "color": color, "cells": [[r, col] for r in range(start, end + 1)]}

pieces = [
    h("A", 5, 3, 5, "left", "#4CC9F0"), h("B", 5, 8, 10, "left", "#4895EF"),
    h("C", 5, 13, 15, "left", "#4361EE"), h("D", 5, 18, 20, "left", "#3F37C9"),
    h("E", 5, 23, 25, "left", "#7209B7"), h("F", 14, 23, 25, "right", "#F72585"),
    h("G", 14, 18, 20, "right", "#FF5D8F"), h("H", 14, 13, 15, "right", "#FF8FA3"),
    h("I", 14, 8, 10, "right", "#FFB3C6"), h("J", 14, 3, 5, "right", "#FFD166"),
    v("K", 7, 3, 5, "up", "#06D6A0"), v("L", 7, 8, 10, "up", "#1B9AAA"),
    v("M", 7, 18, 20, "up", "#118AB2"), v("N", 22, 4, 6, "down", "#90BE6D"),
    v("O", 22, 10, 12, "down", "#43AA8B"),
]

occupied = {}
for piece in pieces:
    for cell in map(tuple, piece["cells"]):
        assert cell not in occupied, f"overlap at {cell}"
        occupied[cell] = piece["id"]
        assert 0 <= cell[0] < 30 and 0 <= cell[1] < 30

def lane(piece):
    cells = piece["cells"]
    direction = piece["direction"]
    if direction in ("left", "right"):
        edge = min(c for _, c in cells) if direction == "left" else max(c for _, c in cells)
        row = cells[0][0]
        cols = range(0, edge) if direction == "left" else range(edge + 1, 30)
        return [(row, c) for c in cols]
    edge = min(r for r, _ in cells) if direction == "up" else max(r for r, _ in cells)
    col = cells[0][1]
    rows = range(0, edge) if direction == "up" else range(edge + 1, 30)
    return [(r, col) for r in rows]

remaining = {p["id"]: p for p in pieces}
order = []
while remaining:
    available = [pid for pid, p in remaining.items() if not any(cell in occupied and occupied[cell] != pid for cell in lane(p))]
    assert available, "level has no clearable arrow"
    pid = sorted(available)[0]
    order.append(pid)
    for cell in map(tuple, remaining[pid]["cells"]):
        occupied.pop(cell)
    remaining.pop(pid)

level = {
    "level_id": "arrows-maze-30x30-v1",
    "game_reference": "Oakever Amaze GO / Arrows-style directional clearing",
    "grid": [30, 30],
    "objective": "clear every arrow by tapping only arrows with an unobstructed path in its pointing direction",
    "rules": ["arrows slide straight off the board", "blocked arrows remain until the blocker is removed", "wrong taps may cost a heart", "no rotation"],
    "pieces": pieces,
    "clear_order": order,
    "validation": {"overlap": False, "within_grid": True, "all_arrows_clearable": True, "solution_verified_by_simulation": True, "runtime_tuning": "match movement distance and feedback to the game build"},
}
(ROOT / "level-arrows-maze-30x30-v1.json").write_text(json.dumps(level, indent=2), encoding="utf-8")
print(json.dumps({"level": str((ROOT / "level-arrows-maze-30x30-v1.json").resolve()), "clear_order": order, "arrows": len(pieces)}))
