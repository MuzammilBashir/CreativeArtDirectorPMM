# Board study 01 — evaluation

Verdict: structural drawing passes the listed geometry checks under explicit test rules. Not approved as a final ad mock or a verified reproduction of the source game.

## Evidence

- Exactly 8 columns and 8 rows, with a uniform 100-pixel cell pitch in the delivered drawing.
- Seven connected blocks, all defined on integer cells: two L triominoes, two straight triominoes, one straight domino, and two 2×2 squares.
- Yellow occupies columns 4–5, rows 4–5 (one-based coordinates).
- 22 occupied cells; four studs in a 2×2 arrangement per cell; 88 studs total.
- Seven matching-color gates. Each opening equals its block's full perpendicular span in the specified exit orientation. Gate sizes are not based on block area or longest dimension.
- No initial overlaps or out-of-board cells.
- Yellow's initial downward move fails because it intersects blue.
- A complete seven-exit sequence was checked at every one-cell translation, including partial passage outside the board. All crossed boundary cells must lie inside the correct gate interval. No collisions occur.

Sequence: blue left 5 cell lengths; green right 5; yellow down 5; cyan left 2; violet up 4; teal up 1; purple down 2. Distances include travel until the entire piece is outside. These are continuous drags with discrete collision checks, not 24 separate player gestures. This establishes existence of a solution, not uniqueness or minimality.

## Test conditions, not confirmed source-game rules

Axis-aligned translation, no rotation, matching-color exits only, full removal after crossing. Each block here has its own distinct color and gate, so shared-gate behavior is not tested. Actual source-game movement restrictions remain unverified.

## CAD critique

1. The drawing is sparse: 22/64 cells occupied (34.4%). It makes geometry easy to inspect but undersells the packed, trapped feeling in the reference. The next composition should increase meaningful obstruction without losing the two-block reveal.
2. Four peripheral pieces have independent exits. They demonstrate complete clearance but contribute little to the central puzzle. This is a weak challenge layout, not a compelling final level.
3. Cyan and teal are too similar, as are violet and purple. Gate matching is exact in the data but should be more distinct at small viewing sizes.
4. The flat square-edged bodies and outlined studs are drafting conventions. They do not satisfy the requested rounded glossy plastic, soft lighting, or material polish. No aesthetic approval is given.
5. A still cannot validate wiggles, blocked-move feedback, drag clarity, sounds, or the 20-second pacing. The revised all-blocks-clear objective also needs a storyboard adjustment after yellow exits.
6. Two blockers must be removed for the specified straight-down yellow path. Other routes and move orders have not been exhaustively searched; do not call that sequence forced.

Use this drawing as a measurable starting blueprint. Improve density and color separation, recheck the solution, then use the approved geometry as the reference for a style render. An ImageGen rendering must be checked again; geometry preservation is not guaranteed.
