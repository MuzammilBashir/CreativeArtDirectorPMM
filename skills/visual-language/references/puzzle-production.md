# Puzzle production: block boards and arrow pictures

Recorded 2026-10-27. Scope: this project's internal puzzle prototypes and creative production. These findings establish implementation behavior and user visual preferences; they do not establish commercial-game equivalence, ad performance, or production approval.

## Choose the game family before the production method

| Decision | Block / matching-gate prototype | Arrow picture prototype |
| --- | --- | --- |
| Visual structure | Solid pieces, exact footprints, board frame, color-matched gates | Recognizable picture made entirely from separate thin orthogonal arrow paths |
| Geometry authority | Checked board JSON and movement routes | Source vector/color mask, generated ordered paths, validator and solution |
| Declared motion | Axis-aligned rigid sliding, no rotation, in-board repositioning, matching-color exits | Head advances in its final segment's direction; tail follows the existing path |
| Production approach | Solve the board, then apply the Block Out material/lighting benchmark and inspect render fidelity | Sample the picture, generate same-color paths, solve, then render directly from the validated data |
| Role of ImageGen | Concept and finish exploration; edited renders must be compared with exact geometry | Source-picture or style exploration; generated arrow geometry is not gameplay evidence |

Game family and tool choice are separate decisions. Code can render blocks, and image generation can explore an arrow picture's source art. Preserve the selected game's mechanics and visual language throughout.

## Arrow picture workflow

Use the existing [Arrow Level Studio](../../../arrow-level-studio/index.html) and [implementation documentation](../../../arrow-level-studio/README.md) when generating more examples. Preserve the accepted sleeping-panda direction: recognizable picture, meaningful color regions, and dense readable arrow paths. Do not substitute tiled bars, sparse abstract spokes, or diagonal polylines.

1. Start from an editable flat-color SVG or transparent source image. Preserve meaningful gaps and detached elements, such as smoke above fire or stars beside a rocket.
2. Sample at a suitable grid resolution. The studio offers 30, 50, 60, and 80 cells per side; selection is manual. Compare facial/detail readability rather than asserting that one resolution is always best.
3. Generate independent orthogonal paths within sampled color regions. Colors are quantized; fidelity is to the sampled palette, not exact original RGB. Each path has one blunt tail, one terminal head, no branching, no repeated cells, and no overlap with other paths.
4. Reject directly opposing collinear heads. Enforce the declared head-ray movement rule, including self-obstruction. Initially blocked pieces are allowed; permanent deadlocks are not.
5. Run the independent solver and replay clearing in the browser. Export the actual level JSON, solution, SVG render, and validation results together. A renderer must draw exactly one head from the path's final segment.
6. Review the rendered picture separately for recognition, spacing, phone readability, and visual head/tail clarity. Solver success does not establish these qualities or engaging difficulty.

The current generator peels legal paths from the source mask, compares eight deterministic seeds, then independently validates the resulting board. It does not implement the previously proposed reverse-insertion algorithm. Do not describe an unimplemented approach as a shipped guarantee.

## Measurements and limits

- Picture coverage: arrow-occupied cells divided by opaque sampled source cells.
- Board occupancy: arrow-occupied cells divided by all board cells.
- Stroke coverage: actual rendered arrow pixels; different from either cell metric.
- Omitted cells: source cells not converted into valid paths; explicitly report them.

Do not force a universal 70–80% board occupancy when the picture needs background or internal gaps. Current examples use roughly 88–93% picture coverage. These are observed results, not mandatory thresholds. Two-cell arrows are currently permitted; a strict minimum of three cells would require a generator change and renewed validation.

Verified sample evidence: [five-example validation report](../../../arrow-level-studio/examples/validation-report.json), [browser checks](../../../arrow-level-studio/export-examples.cjs), [engine tests](../../../arrow-level-studio/test.cjs), and [source/render comparison](../../../arrow-level-studio/examples/five-examples.png). Butterfly, rocket, fox, tropical fish, and sunflower passed full clearing at 50×50 and validation at 30×30. Their 50×50 picture coverage is 89.9–92.8%.

The current browser preview removes a legal piece immediately. It does not yet animate head-first travel. Animated ad proof needs an implemented and reviewed movement sequence. The generator does not prove optimal grid selection, optimal difficulty, source-game identity, or arbitrary-image recognizability.

## Block evidence and boundaries

Retain [Block Out style guidance](block-out-style.md). Preserve cells, concave notches, gate spans, matching colors, and required stud counts during style edits. Four studs per cell belongs to the existing prototype, not all block games.

The [block progress snapshot](../../../visual-directions/progress-2026-10-27/PROGRESS-2026-10-27.md) records five checked layouts, 54/64 occupied cells, 11 pieces, and full routes under the declared test mechanics. This is a recorded prior result, not a fresh test in this update. The same snapshot explicitly leaves commercial-source mechanics and production approval unresolved.

## Lessons from rejected work

- A visually promising sleeping-panda image retained invalid heads, color changes, and ambiguous paths. Preserve its art direction; use the code system for gameplay geometry.
- Earlier colored-bar and sparse diagonal-arrow mocks did not match the requested picture-arrow language. Historical descriptions calling them validated are not acceptance evidence.
- A high visual score cannot compensate for a failed mechanics check. Report geometry as pass/fail/unchecked with evidence, and visual quality as a separate judgment.
- A valid new prototype is not evidence that the advertised commercial game contains that level or mechanic. Label concept demonstrations accurately until source-game equivalence is verified.
