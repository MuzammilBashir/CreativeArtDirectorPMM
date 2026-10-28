# Board study 03 — reference-informed interlocking layout

Reference 2 was reopened and visually examined for this revision. It contains a central cross, long L pieces, bars and squares, irregular empty pockets, and perimeter gates that do not simply sit in front of every matching block. This drawing uses that structural vocabulary without claiming to reproduce its exact level or verified game rules.

## Verified geometry and movement

- 8×8 uniform grid; 54 occupied cells and 10 empty cells (84.375% / 15.625%).
- 11 connected blocks: central yellow 2×2 square, cross, five-cell L, T, U, stair, P, four-cell L, S, six-cell L, and one 2×3 rectangle. Large repeated rectangles have been removed.
- Four studs per occupied cell: 216 total.
- Every block has its own matching-color gate. Gate spans match the block's full perpendicular span in its exit orientation. Gate intervals do not overlap.
- Yellow is initially blocked in all four translation directions.
- Zero blocks can exit immediately in one straight drag.
- Holding all other blocks fixed, only the orange L can reach its gate after repositioning within the board: left one cell, then up to exit. This is a single-piece reachability result, not a proof that every complete solution must start by removing orange; multi-piece repositioning was not exhaustively searched.
- All 11 blocks can be cleared. The saved solution was replayed cell by cell, checking collisions, boundaries and passage through each matching gate.

Test conditions: axis-aligned translation, no rotation, matching-color gates, and repositioning within the board before a straight exit. Partial-outside parking and re-entry were not explored. These conditions are not independently confirmed source-game rules.

## One checked solution

Distances are grid-cell lengths, including travel until the whole block leaves the board. Each line contains consecutive drags for one piece. The order is valid, not claimed shortest or mandatory.

| Piece | Moves |
|---|---|
| Orange long L | Left 1, up 4 to exit |
| Violet T | Left 1, up 1, left 4 to exit |
| Blue-grey rectangle | Up 1, left 2 to exit |
| Green P | Left 2, down 4 to exit |
| Indigo S | Left 4, down 6, left 3 to exit |
| Rose stair | Left 2, up 3 to exit |
| Lilac short L | Up 2, right 3 to exit |
| Blue cross | Up 2, right 3 to exit |
| Teal U | Up 1, right 3 to exit |
| Cyan L | Right 3, down 3 to exit |
| Yellow square | Down 5 to exit |

## CAD assessment

Shape variety, density and initial exit obstruction now meet the revised structural direction. Several blocks remain near a matching side of the board, but their gate is offset and their route is blocked; proximity alone does not grant an exit. Indigo's gate is on the opposite side, requiring substantial travel in this solution.

Remaining limitations: the checked route uses 23 straight drags, which is substantially more than the original two-block reveal. A shorter solution has not been established. Do not treat this as approval for the original 20-second storyboard. The drawing still uses flat drafting materials; final rounded plastic, color distinction at phone size, timing and animation remain unapproved.

Status: structurally validated test layout; suitable for reviewing the puzzle composition. Final ad approval withheld.
