# Arrow Level Studio

Open `index.html` in a browser. No server or installation is required to use the studio.

The included sleeping red panda is an editable, flat-color SVG. Import another SVG or transparent PNG/WebP with the Source control. Select a grid, generate, play, and export the level as JSON or SVG. The two canvases compare the source image and actual arrow board.

## Movement contract

An arrow's cells are ordered tail to head. Its head moves along the final segment's cardinal direction, and its tail follows the existing path. A legal move requires the head's forward ray to be empty, including of its own body. This is NOT rigid translation of a bent piece. A future game runtime must use the same contract for these solver guarantees to apply.

## Generation and verification

The source is sampled into a square grid while preserving aspect ratio and transparency. Colors are quantized to limit antialiasing noise. Paths stay within one sampled color. Generation peels removable paths from the source mask, recording a possible removal order. It compares eight deterministic seeds and retains the best coverage.

Each arrow has one ordered path, no repeated cells, cardinal steps, and one direction derived from its last segment. The renderer draws precisely one terminal triangle and a rounded tail. Paths occupy distinct cells with visual spacing. Directly opposing, collinear arrowheads are disallowed, even when another piece lies between them.

A separate validator checks path geometry, bounds, source color, overlap, opposing heads, and solvability. Exported JSON includes its solution and metrics. The preview recomputes available arrows after every move. Because legal moves only remove occupied cells, a legal removal cannot introduce a new blocker.

## Coverage and limitations

Picture coverage = cells occupied by arrow paths / opaque sampled source cells. This is different from board occupancy and from the percentage of rendered pixels painted by thin strokes. Transparent gaps remain empty.

Cells that cannot be paired into a valid arrow are omitted and reported explicitly in JSON and the UI. Fine facial details may need a larger grid or source simplification. Grid selection is currently manual; the tool does not claim to find an objectively best resolution. Visual recognition is reviewed by a person, not certified by the solver. Two-cell arrows are permitted to preserve small details.

SVG imports are rendered by the browser; use self-contained SVGs with flat fills and no external dependencies. Raster imports should have transparent backgrounds. Uploaded files remain local in the browser.

## Project files

- `panda.svg`: editable source artwork.
- `engine.js`: deterministic generator, geometry validator, and independent clearing solver.
- `studio.js`: import, sampling, rendering, play controls, and exports.
- `panda-level-50.json`: generated and verified sample level.
- `panda-preview.png`: screenshot of the actual playable canvas.
- `build.cjs`: regenerates the embedded SVG source after editing `panda.svg`.
- `test.cjs`: engine tests, including alternate legal orders and invalid inputs.
- `check-browser.cjs`: browser rendering and interaction checks (uses installed Edge and the bundled Playwright runtime).

Run with Node: `node build.cjs` and `node test.cjs`. The browser check currently uses this workstation's bundled Playwright package path.
