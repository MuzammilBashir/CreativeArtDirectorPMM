# Visual Direction: Free the Yellow Block

## Document status

~~~yaml
visual_direction_id: free-the-yellow-block-v1
brief_id: free-the-yellow-block
status: visual-direction-ready
owner: Creative Art Director
format: mobile gameplay ad
duration: 20 seconds
source_references:
  - image-378.png
  - codex-clipboard-9f46f2ff-bc04-4a70-ab2e-83fc95b8b6c9.png
~~~

## 1. Creative interpretation

The ad should make the viewer understand:

1. The board contains multiple colored blocks, each with a matching exit gate.
2. The yellow block is the most visibly trapped and acts as the emotional hook.
3. Surrounding blocks create the obstacle and must also be cleared.
4. Deliberate moves open routes to multiple gates.
5. Yellow escapes at a key moment, then the full board clears.

The target block is yellow for this concept. Every colored block must have a matching gate. The board layout, block shapes, block sizes, gate locations, and exact solution order remain configurable until verified against the actual game.

## 2. Visual objective

Create a premium, colorful, tactile block-puzzle world that feels simple to understand but satisfying to manipulate.

The board must read immediately on a mobile screen. The viewer should never need to study the entire puzzle to understand the current move.

The visual priority is:

1. Yellow target block
2. Matching yellow gate and the other visible colored gates
3. Current obstacle
4. Finger input
5. Open routes and visible board-clearing progress
6. Supporting text and CTA

## 3. Art style

### Core style

- Stylized 3D casual-game art
- Chunky rounded blocks
- Soft bevels and rounded corners
- Glossy or semi-glossy plastic surfaces
- Friendly toy-like construction
- Clean top-down presentation
- Soft contact shadows
- Controlled highlights
- Minimal background detail

### Shape language

Use a combination of:

- Rectangular blocks
- Long horizontal and vertical pieces
- L-shaped pieces
- Cross or stepped pieces
- Compact square pieces
- Large hero pieces

Shapes should be distinct at a glance. Avoid silhouettes that are so complex they become difficult to track during movement.

### Materials

The target and surrounding pieces should feel like the same manufactured material. Variation may come from color and shape, not from unrelated surface styles.

Avoid:

- Metallic reflections
- Glass transparency
- Rough stone textures
- Realistic wood grain
- Excessive micro-detail

unless the game profile later confirms a different material identity.

## 4. Color direction

### Target

- Bright saturated yellow
- Warm highlight
- Slightly darker golden side shading
- Strong separation from the board and nearby pieces

### Exit gate

Use the same yellow family as the target, but slightly darker or brighter so the gate is clearly related without blending into the block.

Every other colored block must have a visually matching gate. Gates may be distributed across the top, bottom, left, and right edges. Gate colors must remain distinguishable at mobile size.

### Surrounding blocks

Use a cool-to-neutral supporting palette:

- Cyan
- Blue
- Green
- Purple
- White or light gray

Use orange and red sparingly because they can compete with the yellow target and failure feedback.

### Board and background

- Deep blue or blue-violet outer frame
- Dark desaturated inner playfield
- Soft neutral grid or board separation
- No high-frequency background pattern

## 5. Board and layout direction

### Structural invariants

These are mandatory gameplay-construction rules and must be validated before visual polish:

- Declare the logical grid row and column count.
- Use one consistent base tile size across the board.
- Construct every block from integer-grid footprints.
- Give every 1x1 tile exactly four Lego-style studs in a consistent 2x2 pattern.
- Keep stud spacing, bevel, depth, and scale consistent across all blocks.
- Use explicit footprints such as 1x1, 1x2, 1x3, 1x2 straight, 2x2 square, L shapes, and other approved integer-grid shapes.
- Match every gate’s size, orientation, alignment, and cross-section to its corresponding block.
- Do not allow a block to appear to pass through a gate that is smaller or misaligned.

If any invariant cannot be verified from the mock, mark it STRUCTURALLY_INVALID and do not approve it.

The visual system supports two layout families:

### Free-form block layout

Irregular blocks of different shapes move through open spaces. Exits may appear on any board edge.

### Lane-based layout

Long vertical or horizontal blocks form clearer lanes and exits. This can be used when the game level is more column-oriented.

For this concept, prefer the free-form layout because it creates a clearer “find the way out” story. Use a board with enough empty space to make the yellow route and at least one additional colored route visible. The final solution must clear all colored blocks, not only yellow. Declare and validate the grid and tile dimensions before creating the mock.

Do not force the original 8×8 geometry if the actual game uses a different logical grid.

## 6. Camera and composition

### Master view

- Portrait 9:16 composition
- Elevated top-down camera
- Slight perspective rather than completely flat orthographic
- Board fills most of the frame
- Outer frame remains visible
- Target and gate remain inside the center-safe region

### Hook framing: 0–3 seconds

- Show the target block near the center
- Keep the matching gate visible in the same frame if possible
- Use a very slow push-in
- Allow the target block to wiggle
- Leave clean space for the hook text above or below the board

### Failed move: 3–8 seconds

- Move to a closer crop
- Keep the target, finger, and blocking piece visible together
- Use a small camera punch on contact
- Never let the finger cover the obstacle

### Reveal: 8–15 seconds

- Pull back enough to show both surrounding blocks
- Maintain the relationship between the moved pieces and the opened route
- Use a subtle follow or reframe, not a dramatic camera move

### Payoff: 15–18 seconds

- Follow the target block toward the gate
- Use a gentle push-in during the final movement
- Keep the gate and target fully visible through the escape

### CTA: 18–20 seconds

- Pull back to reveal a harder board
- Keep the new target and gate visually obvious
- Preserve a clean text area for the CTA

## 7. Typography

Use a rounded, bold, highly readable casual-game typeface.

### Hook

~~~text
CAN YOU GET
YELLOW OUT?
~~~

Use two lines if needed. Place outside the gameplay focal area.

### Payoff

~~~text
FREED!
~~~

Use a large, short, high-contrast treatment. The word should appear after the target has visibly crossed the gate.

### CTA

~~~text
YOUR TURN.
FIND THE WAY OUT!
~~~

Do not place the CTA over the target movement or exit gate.

## 8. Motion and juice direction

### Target block

- Small idle wiggle while trapped
- Short anticipation before movement
- Smooth slide with controlled easing
- Slight resistance or bump on failure
- Confident movement during successful escape

### Surrounding blocks

- Responsive slide
- Mild friction
- Short settle at the end of movement
- No excessive bounce

### Failed attempt

- Gentle physical bump
- Red highlight on the blocking piece
- Soft error sound
- No aggressive shake

### Successful escape

- Clear slide sound
- Small yellow motion trail
- Matching gate click
- Short glow as the block crosses
- Controlled confetti burst
- Text reveal: FREED!

Effects must confirm the action without hiding block boundaries or the solution route.

## 9. Audio direction

Use tactile, friendly, low-fatigue sound design:

- Soft block slide
- Gentle collision bump
- Short error tone
- Clear gate click
- Small success chime
- Light confetti sparkle
- Subtle upbeat puzzle bed

The audio should feel satisfying rather than aggressive. The successful gate click is the strongest sound in the sequence.

## 10. Twenty-second storyboard

### 0–3 seconds: Hook

The yellow target block wiggles in the center. The matching exit gate pulses. The camera slowly pushes in.

Text: CAN YOU GET YELLOW OUT?

### 3–8 seconds: Failed attempt

The finger moves the yellow block toward the gate. A horizontal or irregular block blocks the route. The yellow block bumps gently. The obstacle receives a brief red highlight.

### 8–15 seconds: Reveal

The finger slides two surrounding blocks into open spaces. Each move creates visible space. The route from target to gate becomes obvious.

### 15–18 seconds: Payoff

The yellow block slides through the matching gate. Gate click, glow, short confetti burst.

Text: FREED!

### 18–20 seconds: CTA

A harder board appears with a new target and exit arrangement.

Text: YOUR TURN. FIND THE WAY OUT!

## 11. Aspect-ratio and safe framing

Primary format: 9:16 portrait.

Prepare future adaptations for:

- 4:5
- 1:1
- 16:9

Keep these safe:

- Target block
- Gate
- Blocking piece
- Finger
- Main text
- CTA

The board may be cropped only after the current move remains understandable.

## 12. Mockup instructions

Create three visual mock directions before production:

### Mock A: Premium plastic

Glossy rounded blocks, controlled reflections, deep blue-violet frame, clean board, strong yellow focus.

### Mock B: Soft toy puzzle

Softer matte-plastic material, warmer highlights, gentler shadows, friendlier and more relaxed tone.

### Mock C: High-contrast gameplay

Darker board, brighter target and gate, stronger obstacle highlight, clearer route visualization, optimized for rapid mobile comprehension.

The mocks should show the same concept and board logic. Do not change the strategic idea while exploring the visual treatments.

## 13. Required production assets

- Target block
- Matching exit gate
- Four to six surrounding block shapes
- Board frame
- Inner playfield
- Empty-space or grid treatment
- Finger cursor
- Red obstacle highlight
- Yellow success glow
- Confetti effect
- Hook, payoff, and CTA typography
- Slide, bump, click, success, and confetti audio

## 14. Non-negotiables

- Yellow target remains the primary focal point.
- Matching yellow gate and the other color-coded gates remain visually clear.
- Grid dimensions and tile size are explicit and consistent.
- Every visible block uses an approved integer-grid footprint.
- Every 1x1 tile has the same four-stud Lego pattern.
- Every gate matches its block’s dimensions and alignment.
- Obstacle and solution are readable at a glance.
- The first yellow escape uses only a few understandable moves, while the larger board communicates that all blocks must eventually be cleared.
- Blocks remain visually consistent.
- Effects do not hide gameplay.
- The board remains readable on mobile.
- The production must not imply mechanics that the actual game cannot support.

## 15. Open validation items

~~~yaml
actual_board_geometry: pending
declared_grid_dimensions: required
consistent_tile_size: required
consistent_stud_pattern: required
valid_integer_block_footprints: required
gate_block_dimension_match: required
target_block_size_and_shape: pending
all_block_to_gate_mappings: pending
gate_locations: pending
movement_rules: pending
full_board_solution_sequence: pending
harder_cta_board: pending
actual_payoff_effects: pending
~~~

## CAD decision

~~~yaml
status: REQUIRES_MOCK_REVISION
reason: The previous mock incorrectly represented a single-gate objective. All colored blocks and matching gates must be visible in the next mock set.
next_step: Create ten controlled mocks with varied block shapes and color-matched gates.
~~~

