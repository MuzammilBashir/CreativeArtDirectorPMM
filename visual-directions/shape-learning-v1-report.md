# Shape Learning Report: Clear the Whole Board V1

## Evaluation policy

This batch was evaluated against:

- The supplied block-puzzle references
- The corrected gameplay rule: every colored block has a matching exit gate
- The objective: clear every block, including the stuck yellow block
- The visual direction for glossy toy-like blocks and mobile readability

A mock fails if any required block-to-gate relationship is missing or ambiguous. Visual attractiveness cannot compensate for a gameplay-rule failure.

## Scoring model

~~~text
Gate completeness and mapping: 30
Shape variety and readability: 20
Yellow focal clarity: 15
Board and route readability: 15
Reference fidelity: 10
Producer feasibility: 10
Total: 100
~~~

Approval threshold: 90 and no critical gameplay-rule failure.

## Results

| Mock | Score | Status | Main finding |
|---|---:|---|---|
| V01 | 72 | FAIL | Attractive board, but white and orange block-to-gate mappings are not visibly complete. |
| V02 | 93 | PASS | Strong multi-edge gate system, clear irregular shapes, strong yellow focal block, and readable interaction. |
| V03 | 90 | PASS | Good multi-edge gate coverage and varied shapes; slightly busier but still understandable. |
| V04 | 78 | FAIL | Strong cross-shaped layout, but at least one block color lacks a clearly matching gate. |
| V05 | 86 | FAIL | Strong shape variety and board rhythm, but several gate mappings are ambiguous. |
| V06 | 91 | PASS | Clear free-form layout, varied polyomino shapes, readable yellow target, and mostly clear gate mapping. |
| V07 | 83 | FAIL | Symmetrical layout is attractive, but multiple blocks do not have clearly visible matching gates. |
| V08 | 92 | PASS | Strong polyomino variety, good perimeter gate system, and clear target/blocker relationship. |
| V09 | 87 | FAIL | Good visual composition, but cyan/teal and repeated blue mappings are not sufficiently explicit. |
| V10 | 84 | FAIL | Organic layout is visually interesting, but gate completeness and matching clarity are unreliable. |

## Batch result

~~~yaml
total_mocks: 10
passed: 4
failed: 6
pass_rate: 40%
best_mocks:
  - V02
  - V08
  - V06
performance_validated: false
~~~

## What the failures taught us

### 1. Gate completeness needs to be designed before styling

Image generation tends to create attractive blocks faster than it creates logically paired gates. The next prompt and production workflow must first define a block-to-gate inventory.

### 2. Color matching is not enough when colors repeat

If two blocks share a similar blue or cyan family, the gate relationship becomes ambiguous. Use distinct color roles or add a secondary matching cue such as a simple gate stripe, outline, or icon.

### 3. More shapes can reduce gameplay clarity

Irregular shapes are valuable, but too many complex pieces make the target route and gate mapping difficult to read. Shape variety must be balanced with open space.

### 4. The yellow block must remain the focal hook

The strongest passes keep the yellow block central, clearly trapped, and visually separated from the other blocks without making it appear to be the only block that matters.

### 5. The full-board objective should be visible without explaining every solution

The mock should show enough matching gates to establish the clear-all-blocks objective. It does not need to show the complete solution sequence in one frame.

## Promoted visual rules

These rules are now promoted into the working visual direction:

1. Create a block-to-gate inventory before arranging the board.
2. Every visible colored block must have one visible matching gate.
3. Use six to eight primary blocks in concept mocks unless the game proves that more remain readable.
4. Keep the yellow block central or near-central as the emotional hook.
5. Use at least one irregular block, but balance it with simple pieces.
6. Leave sufficient empty space to show the next possible move.
7. Use distinct color families; do not rely on nearly identical blue or cyan gates.
8. Show multiple gates around the perimeter to communicate the full-board objective.
9. Use red highlighting only for the current obstacle, not as a permanent decorative glow.
10. Judge gameplay logic before polish.

## Best direction for the next iteration

Use V02 as the structural base and borrow the strongest shape language from V06 and V08:

- V02: clearest gate system and focal hierarchy
- V06: strongest free-form enclosure and varied shapes
- V08: strongest polyomino variety and perimeter distribution

The next mock set should keep V02’s clarity while testing fewer, more deliberately paired blocks.

## Learning status

~~~yaml
learning_status: promoted_to_working_pattern
scope: block-puzzle gameplay ads
confidence: medium
performance_verified: false
next_validation: producer or game-build confirmation
~~~

