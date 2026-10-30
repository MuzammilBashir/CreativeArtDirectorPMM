---
name: storytelling
description: Write, critique, and improve short stories for mobile-game hooks and product-ad openings. Use for premises, scripts, story beats, and story-quality review before visual prompting; reference analysis remains with Hook Analyzer.
metadata:
  short-description: Meaningful stories for game hooks
---

# Storytelling for game hooks

## Purpose and ownership

Help Art Director create a short story that gives a particular viewer a reason to care, anticipate an outcome, and want the following game experience. A sequence of technically executable actions is not sufficient evidence of an engaging story.

Work within the supplied brief: Creative Strategist owns audience, promise and strategic intent; Hook Analyzer supplies reference evidence; Art Director authors the original story and its execution. If strategy is missing, offer clearly labeled exploratory premises rather than inventing campaign facts. This skill supports product hooks too, using the actual product experience in place of gameplay.

Paths below are repository-root relative so the canonical and Claude copies work identically.

## Retrieve only what the task needs

- Follow `vault/Art Director/Art Director Home.md`, root `SKILL.md`, and `agent-memory/art-director-memory.md`.
- Read `skills/creative-strategist/SKILL.md`, the brief, supplied gameplay/product evidence, and relevant audience or performance records.
- For Hooks, read `Hooks/rules/production-rules.md`; the current new-hook target is 4–5 seconds. A hook is an opening segment, not necessarily a complete ad with resolution and CTA.
- Apply `skills/art-feedback-ledger/SKILL.md`. Load shared visual, camera and motion skills when translating an accepted written story into execution; do not duplicate them here.
- For reference-led work, use `Hooks/knowledge/gemini-collection-synthesis-v1.md` and the actual matching reports/corrections. Read `skills/storytelling/references/research-basis.md` when research rationale or further study is useful.

## Start with the player, then the premise

Identify the specific desire the game can truthfully serve: solving a stubborn problem, mastering a move, discovering something, expressing taste, restoring order, gaining power, competing, or another evidenced appeal. These are options, not a fixed audience taxonomy.

Keep three things separate:

- **Player desire:** what makes this experience worth trying.
- **Character objective or action objective:** what someone or something is trying to accomplish in this scene.
- **Viewer anticipation:** the specific outcome or answer the opening makes the viewer want next.

These may overlap, but naming an emotion such as curiosity does not explain what the viewer is curious about. State the question concretely. Stakes can be small: one remaining gap, an almost-finished pattern, a surprising consequence, or a choice whose result matters within the scene. Do not manufacture trauma or danger merely to inflate intensity.

## Develop the story before the prompt

Write the premise in plain language without camera, rendering, model settings or decorative adjectives. When exploring, compare a few genuinely different premises; do not turn every small writing request into a fixed concept quota.

Choose a structure that fits the idea. Useful possibilities include:

- A clear objective meets an obstacle, prompting a consequential choice.
- A visible action produces an unexpected but understandable result.
- An unusual situation establishes a specific question, then a reveal changes its meaning.
- A near-complete process makes the next contact, turn, transformation or completion worth anticipating.
- A viewer sees a solvable problem and mentally commits to a move.

These are writing tools, not mandatory story formulas. Characters, dialogue, conflict and a positive ending are optional. For sensory or mechanic-led hooks, the process itself can carry the story if its progression and anticipated event are concrete.

Check causality: explain why one beat leads to the next, or why a reveal changes the meaning of an earlier beat. Mere chronology ("then picks up phone, then smiles") does not demonstrate meaningful development. Surprise should reward or productively revise an expectation; randomness alone is not a story payoff.

Write the ending as a deliberate promise to the next segment. It may provide a small payoff, pause at a meaningful decision, or leave a precise question open. Describe what the following gameplay/product segment must deliver. If that footage is absent, record the intended bridge and its missing evidence. Do not pretend an unspecified hidden phone screen establishes product relevance.

## Critique the written idea separately

Before a production prompt, give a candid story verdict with concrete reasons:

| Question | Evidence to seek in the written story |
| --- | --- |
| Why would this viewer care? | A specific desire, recognizable circumstance, interesting problem or sensory expectation |
| Why continue watching? | A concrete unresolved outcome, rather than "creates curiosity" |
| What develops? | A consequence, escalation, discovery, reversal, progress or purposeful anticipation |
| Why does the game belong? | Its actual appeal or interaction fulfills the setup, or an explicit exploratory connection awaits validation |
| Can this fit the duration? | A readable causal unit with enough time for comprehension and the key change |

Use these as diagnostic questions, not a checklist that automatically certifies engagement. Name the weakest part and rewrite it. If replacing the game with any unrelated app leaves the premise equally intact, investigate whether its connection is too generic; this is a diagnostic, not an automatic rejection of broad emotional hooks.

Judge the story without awarding points for polish, model compliance or an attractive character. Do not claim that a subjective score predicts engagement. The production score/gate remains governed by `Hooks/rules/production-rules.md`; do not create a competing numeric threshold or let an average conceal an unresolved story failure.

For 4–5 seconds, choose the smallest meaningful story unit. Remove explanatory setup and redundant action before accelerating everything. A complete long-form character arc or every beat of a 15-second reference need not fit. Test whether a reader can explain the premise and anticipated outcome from the proposed sequence; this is a clarity check, not audience validation.

## Output scaled to the request

For a new story, provide:

```text
Status: EXPLORATORY | REVISE | READY_FOR_PROMPTING
Premise:
Player/viewer desire and evidence or assumption:
Why care:
Specific anticipation or question:
Short beat sequence with approximate total timing:
Payoff or open question:
Game/product connection and required next segment:
Weakest point and revision made:
Unknowns:
```

For critique, explain what the story currently communicates, where the viewer's interest lacks support, and the smallest useful rewrite. A short request may need only a paragraph. `READY_FOR_PROMPTING` means usable for the authorized production task, not proven engaging, game-accurate without evidence, or permission to spend. During writing practice, stay in text unless generation is requested.

## Learn from corrections

The owner judged HOOK-001's execution okay but its story meaningless (2026-10-30). Its earlier internal 91% approval remains historical, not evidence of story acceptance. Its tired-worker -> phone -> smile sequence lacked a sufficiently specific reason to care and game connection. Preserve that scoped diagnosis; do not ban quiet hooks, office settings, phone props or emotional changes generally.

Save story versions, rejection reasons and owner feedback in the relevant production or study record. Update agent memory and the existing feedback ledger for reusable owner corrections, keeping Claude copies aligned. New research interpretations stay hypotheses until calibrated; no single owner approval or platform recommendation proves audience performance. Campaign testing must distinguish attention from downstream player quality and outcomes.
