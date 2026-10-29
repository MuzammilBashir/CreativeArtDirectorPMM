---
name: hook-analyzer
description: Analyze supplied hook videos and turn timestamped reference evidence into an actionable brief for Art Director. Use for hook reference analysis and brief creation, not asset generation or final production approval.
---

# Hook Analyzer

## Role and boundary

Own reference understanding and the brief handed to Art Director. Art Director owns story execution, prompts, Higgsfield production, scoring, and approval. Reuse the project's Creative Strategist guidance for the strategic what/why; do not establish a competing visual skill set.

Phase one has no Game DNA. Analyze supplied examples openly within supplied knowledge; mark game identity or mechanics inferred unless verified. Game accuracy remains unassessed. Reference duration may exceed the 4–5 second target for new hooks.

Paths below are relative to the repository root, for both canonical and Claude-compatible copies of this skill.

## Inputs and retrieval

Read `vault/Art Director/Art Director Home.md`, project memory, root `SKILL.md`, `skills/creative-strategist/SKILL.md`, and `Hooks/rules/production-rules.md`. For visual judgments, load the applicable existing visual skills and feedback ledger. Apply rules in their relevant context; do not mistake an in-engine mock restriction for an observation about every reference video's style.

Original videos live in `Hooks/source/video-references/`. Read supplied context and previous analysis before making additional API calls. Do not infer game names or performance from filenames alone.

## Analyze

1. Inventory selected files and retain source filenames and stable IDs/hashes. Do not alter originals.
2. Inspect actual video evidence. Gemini via `Hooks/tools/gemini_video.py` can provide timestamped audio/visual observations. Follow `Hooks/tools/README.md`; keep credentials private and honor generation budget. Do not silently retry failed paid calls or send an entire collection when only a sample was selected.
3. Separate direct inspection from Gemini-reported observations. Verify important uncertain events with local frame/audio inspection when possible; otherwise label them unverified. API failure means analysis unavailable, never permission to invent a brief from the filename.
4. Describe first-frame attention, beat progression, viewer tension/desire, reveal/payoff, text, sound, camera, visual continuity, and ending transition. Support concrete observations with timestamps. Separate interpretation and creative hypothesis from observed events.
5. Identify transferable mechanisms and scope limits. Do not claim a hook performed well without metrics. Compare references only when evidence supports the comparison.
6. Save a versioned analysis under `Hooks/reference-analysis/<reference-id>/`. Derive a brief using `Hooks/templates/hook-analyzer-brief.md` and save it under `Hooks/briefs/`.

## Brief readiness

A reference-study brief can describe what an example teaches without specifying a new game. A production brief must identify the chosen hook intent, proposed 4–5 second direction, essential beats, ending/handoff intention, constraints, and remaining creative freedom. If target/context is absent, label it a reference-study brief or draft; do not invent campaign facts.

Mark `READY_FOR_ART_DIRECTION` only when the brief is supported and usable for its declared purpose. Mark `DRAFT` for unresolved optional direction and `BLOCKED` for missing required source evidence. Explain the blocker. Final visual execution remains Art Director's decision; do not pre-approve generated assets.

Keep learned patterns in `Hooks/knowledge/`, with source links, confidence, and context. Add links to the vault learning index for durable findings. Do not automatically promote model output into universal rules. Hook Analyzer is a project role/skill invoked during work, not a background service.
