# Ad Review Framework — V1

Use this framework for every mobile UGC ad and gameplay ad before it is marked test-ready.

## Scope

This V1 reviews UGC, gameplay, static, and motion creative supporting those formats. Playable ads are out of scope and require a later framework.

## Decision statuses

- `APPROVED`: meets the required thresholds and is ready for the approved test or delivery workflow.
- `REVISE`: has a bounded issue that can be corrected without replacing the core concept.
- `REJECTED`: is materially misleading, weak, inconsistent, untestable, copied too closely, or not worth revising.
- `BLOCKED`: cannot be reviewed because required authoritative evidence or production input is missing.
- `NEEDS_APPROVAL`: requires an action outside the validated autonomous policy, such as new spend, publishing, or unresolved rights.

## Evidence labels

For each important finding, use:

- `verified`: directly inspected and supported.
- `inferred`: reasoned interpretation.
- `unknown`: not checked or unresolved.

## Scoring

Score each category from 0 to 5:

- `0`: absent, incorrect, or unacceptable
- `1`: materially deficient
- `2`: weak but partially usable
- `3`: acceptable
- `4`: strong
- `5`: exceptional and clearly useful

Minimum approval thresholds:

- Strategic clarity: 4
- Hook strength: 3
- Gameplay accuracy: 4
- Visual polish: 4
- Readability: 4
- Visual consistency: 4
- Technical compliance: 4
- Test usefulness: 4
- No critical blocker

## Review dimensions

### 1. Strategic clarity

- Is the audience identifiable?
- Is the player desire, frustration, or fantasy clear?
- Does the ad communicate one primary idea?
- Is the CTA appropriate to the objective?

### 2. Hook strength

- Is the first moment understandable without context?
- Does it create curiosity, tension, surprise, or desire?
- Does the hook connect to the actual game?
- Is it visible or audible early enough for the placement?

### 3. Gameplay accuracy

For block-board or arrow-picture prototypes, apply [puzzle production guidance](skills/visual-language/references/puzzle-production.md). Record mechanics validation as `pass`, `fail`, or `unchecked` independently of the creative score. Require the level data, declared movement contract, solver/route evidence, and inspection of the actual render. Image generation, a solvability score, or an attractive screenshot cannot substitute for these checks. Source-game equivalence remains a separate claim. A failed mechanics check prevents gameplay approval regardless of polish.

For arrows, report picture coverage and omitted cells separately from board occupancy. For blocks, inspect footprints and gate spans against the checked blueprint. If motion is part of the deliverable, review that motion; a still or instant-clear prototype does not validate an exit animation.

- Are the mechanics, UI, characters, environments, and outcomes real?
- Are all claims supported by verified game evidence?
- Has editing changed the apparent mechanic, difficulty, or result?
- Is dramatization clearly framing rather than a false gameplay claim?

### 4. Visual direction and consistency

- Does the ad follow the approved game visual direction?
- Are shape, color, lighting, detail level, typography, UI, and motion coherent?
- Do variants feel like one creative family?
- Are references used as principles rather than copied execution?

### 5. Visual polish

- Are composition, framing, lighting, motion, and transitions intentional?
- Are there generation artifacts, broken anatomy, continuity errors, or distracting defects?
- Does the asset feel finished at delivery size?

### 6. Mobile readability

- Is the key message understandable quickly?
- Are captions and UI readable on a small screen?
- Is contrast sufficient across scenes?
- Are platform safe areas and crops respected?
- Was the asset viewed at intended phone size or in an equivalent ad preview?

### 7. Emotional pacing

- Does the sequence have a clear hook, proof, payoff, and CTA?
- Are there dead moments or unnecessary complexity?
- Does the ending resolve with a convincing next action?

### 8. Technical compliance

- Correct aspect ratio, duration, resolution, file type, audio behavior, and size
- No broken links, missing assets, unsupported fonts, or rendering errors
- Correct naming, version, source references, and metadata

### 9. Test usefulness

- Is the creative hypothesis explicit?
- Is the primary variation axis known?
- Can the result be compared to a control or related variant?
- Does this test a meaningful choice rather than a cosmetic change?

### 10. Provenance and usage status

- Is every source and generated asset recorded?
- Are creator, tool, prompt or source, date, and usage status present?
- Are unknown licenses clearly marked?
- Are recognizable real people, trademarks, protected characters, or living-artist styles handled within policy?

## Critical blockers

Block or reject immediately when any applies:

- False or unverifiable gameplay claim
- Missing required gameplay evidence
- Core message cannot be understood
- Asset is visually broken at delivery size
- Reference is copied too closely
- Provenance is missing for a required asset
- Unresolved rights, likeness, trademark, or licensing concern
- Platform or brand constraint is violated
- Required technical output cannot be validated
- The action requires new spend or publication outside policy

## Review report

```markdown
# Ad Review Report

asset_id:
game_id:
concept_id:
variant_id:
format: UGC | gameplay | static | motion
placement:
review_date:
reviewer: Autonomous Art Director

## Decision

status: APPROVED | REVISE | REJECTED | BLOCKED | NEEDS_APPROVAL
summary:

## Scores

strategic_clarity: /5
hook_strength: /5
gameplay_accuracy: /5
visual_consistency: /5
visual_polish: /5
mobile_readability: /5
emotional_pacing: /5
technical_compliance: /5
test_usefulness: /5
provenance: /5

## Evidence

verified_sources:
inferences:
unknowns:
gameplay_sources:
visual_reference_sources:
performance_context:

## Findings

strengths:
issues:
critical_risks:
required_revisions:
provenance_notes:

## Test recommendation

hypothesis:
primary_variation_axis:
control_or_variant:
success_signal:
next_iteration:
```

## Revision behavior

For `REVISE`, list the smallest fixes, assign each to the appropriate tool or agent, and re-review the revised version. Do not silently change the hypothesis.

For `REJECTED`, record whether the failure came from the concept, hook, visual direction, production method, source material, or evidence.

For `BLOCKED`, identify the exact missing input. Do not compensate with invented facts.

For `NEEDS_APPROVAL`, state the exact external action, estimated cost or risk, and the policy decision required.

