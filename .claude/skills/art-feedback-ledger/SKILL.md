---
name: art-feedback-ledger
description: The owner's standing feedback on art creation, mocks, prompts and visual reviews. Load before ANY image prompt, mock, restyle, or visual critique, and update it whenever the owner corrects or approves visual work.
metadata:
  short-description: Owner's art feedback, applied every time
---

# Art Feedback Ledger

Rules the owner has given during real tasks. They override general instinct and refine (never replace) the Ad Bible and specialist skills. Apply every rule before creating or reviewing visuals, so the owner never has to repeat it.

## How to use

1. Read every rule below before writing an image prompt, editing a mock, or reviewing visuals.
2. Before showing a result, check it against each rule and say which ones it fails.
3. When the owner gives feedback on art or visuals (a correction, a preference, or approval of an approach), update this file in the same turn:
   - New lesson → add a rule with the next ID.
   - Refines an existing rule → edit that rule; never duplicate.
   - Contradicts a rule → replace it and note the date of the change.
   - One-off instructions for a single asset are not rules; record only what applies to future work.
4. Mirror every change to `.claude/skills/art-feedback-ledger/SKILL.md` (copy the file; links are absolute-free so it copies cleanly).

Rule format: `ID — rule` then `Why:` (the owner's reason) and `Source:` (date and task).

## Rules

### AF-01 — Mocks must be achievable in a mobile engine
Match the reference's style tier (e.g. gamey semi-realistic), and render it as an in-engine mobile game frame, not a photoreal render or an "edited screenshot". Prompt for mobile techniques: baked/simple lighting, simple shadows, simplified textures, moderate polygon count, low-detail background cards, bloom only on lights. Exclude photorealism, cinematic grading, depth of field, lens flare, volumetric light, film grain and heavy motion blur. Review every mock with: "Could our engine render this on a mid-range phone?"
Why: we are mobile developers; a mock the build can't reach misleads the ad and sets an impossible art target.
Source: 2026-10-28, racer mocks v1–v2 drifted to photoreal.

### AF-02 — Don't overshoot the style tier in either direction
When correcting realism, stay at the reference's level: semi-realistic means realistic proportions with simplified shading, not cartoon. Keep detail consistent across the frame; secondary objects (traffic, props, terrain) must never look more detailed than the hero.
Why: v3 swung too cartoony; v4/v5 traffic and hillside were more detailed than the hero car.
Source: 2026-10-28, racer mocks v3–v5.

### AF-03 — Restyle = change the look only; gameplay and silhouettes are locked
When asked to apply one game's visual style to another's gameplay, keep the board, every piece's footprint, position, colour assignment, stud/detail count, gates, empty cells and UI elements exactly as in the source. Change only material, finish, palette, frame, background and UI skin. Verify cell by cell against the source before presenting.
Why: the owner needs the restyle to stay true to the actual gameplay.
Source: 2026-10-28, Cube Blast restyle of the stud-block game.

### AF-04 — No mascot or added characters unless asked
Taking a reference's style does not mean taking its mascot, goal panel, or characters.
Why: owner explicitly excluded the Cube Blast bear.
Source: 2026-10-28, Cube Blast restyle.

### AF-05 — Fix every flaw found in review before presenting
Read rendered text in every result (popups, HUD, labels). If text is misspelled or garbled, fix it with a targeted edit before showing the image. Prefer a targeted edit of the best version over regenerating from scratch when the layout already works.
Why: v5's first pass rendered "NEAR MISS" as "MMIISS"; the owner approved editing v4 rather than starting over.
Source: 2026-10-28, racer mock v5.

### AF-06 — Iterate with an honest critique after each version
After each mock, compare it to the previous version and the reference: what was fixed, what is still wrong, what is new, and mobile feasibility. Don't call a version done when a known issue remains.
Why: owner confirmed this critique loop ("you understood the problems") and kept iterating on it.
Source: 2026-10-28, racer mocks v1–v5.

### AF-08 — Match the reference's colour tone, highlight strength and exposure
When matching a style reference, sample the reference's actual colours and copy their tone (hue, saturation, value), not just colour names. Keep highlights as soft and small as the reference; never stronger. Keep overall exposure and brightness at the reference's level; never over-bright. Prompt with measured values (hex colours, "soft subtle highlights", "same exposure as reference") rather than words like "bright", "strong glint" or "stage lighting".
Why: Cube Blast restyle v1 had different colour tones, highlights that were too strong, and over-bright lighting.
Source: 2026-10-28, Cube Blast restyle v1.

### AF-09 — Self-score against the reference and retry until ≥ 90%
Before showing any style-matched visual, compare it with the reference myself and give it a score out of 100 using the Art Director's knowledge (visual-language skill, the review framework, the Block Out benchmark for block games, and this ledger). Measure what can be measured (sampled colour difference, brightness, highlight coverage, geometry match) and judge the rest by eye. If the score is below 90, name the gaps, fix the prompt or edit, and retry. Present only a result that scores ≥ 90, with its score breakdown and the rejected attempts listed. If several retries can't reach 90, stop and report the best score and what blocks it. Image generation can't hit exact colour values, so when only tone is off, a deterministic per-colour correction pass on the best version is allowed. Say so when presenting. Reusable tools: `visual-directions/cube-blast-restyle/score.py` (colour 40, exposure 20, highlights 15, geometry 25) and `correct.py`.
Why: the owner should not have to spot mismatches; the agent must check its own work against the reference.
Source: 2026-10-28, Cube Blast restyle v1 feedback.

### AF-07 — Visual analysis format
When asked to analyse game screenshots, give for each one: art style, game genre, 10 good things, and the bad things, judged by Art Director rules. Label game titles and mechanics as `inferred` unless verified.
Why: format the owner requested.
Source: 2026-10-28, reference screenshot analysis.
