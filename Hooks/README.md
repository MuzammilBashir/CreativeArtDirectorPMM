# Hooks

Workspace for learning from the owner's hook videos and developing the Art Director's hook/intro production process.

## Start with references

For Gemini-assisted video analysis, see [local integration setup](tools/README.md). Credentials stay in the ignored `Hooks/.env` file; analysis outputs require Art Director review before promotion into knowledge.

Drop original videos into `source/video-references/`. Optional game-name subfolders can group references from multiple games. Keep original filenames; no renaming or metadata preparation is required before sharing them.

Use `source/supporting-material/` for related briefs, screenshots, scripts, and owner notes. Source videos remain unchanged; extracted frames and analysis belong in `reference-analysis/`, grouped by reference ID.

## Folder map

| Folder | Purpose |
| --- | --- |
| `source/video-references/` | Original user-created hook videos, optionally grouped by game |
| `source/supporting-material/` | Context and supporting files accompanying references |
| `reference-analysis/` | Per-reference observations, timestamps, extracted frames, and review notes |
| `knowledge/` | Evidence-backed patterns and reusable learnings linked to their references |
| `rules/` | Creation constraints and approval criteria developed with the owner; label proposals separately from adopted rules |
| `briefs/` | Incoming briefs from the separately managed Hook Analyzer |
| `productions/` | One folder per intro, containing its prompts, assets, reviews, and handoff |
| `templates/` | Reusable analysis and production templates as the process develops |

## Production organization

Create these folders inside each production when work begins:

```text
productions/<intro-id>/
  01-story/
  02-prompts/
  03-first-frame/
  04-storyboard/
  05-draft-video/
  06-upscaled/
  07-mixer-handoff/
  reviews/
```

Preserve versions and record the approval or revision decision against the exact asset reviewed.

## Agreed scope

- Read [production rules](rules/production-rules.md) before production: draft cost selection, attempt limits, smallest-supported image drafts, 480p video drafts, 720p final video, 4–5 second duration, and the 90% scoring gate. Working interpretations are labeled separately from owner requirements.

- The existing Art Director visual skills are universal and apply to Hooks. Reuse the canonical skills in project `skills/` (and their existing Claude-compatible copies); do not create a separate Hooks visual skill set.
- Load the relevant visual-language, camera-composition, aspect-ratio-delivery, and juice-and-audio skills, plus the standing art-feedback ledger, for visual production and review. Apply game-specific references only when relevant; universal skill reuse does not make a particular game's visual style universal.
- `rules/` is for hook-specific storytelling, sequencing, and stage-approval criteria. It must not duplicate or silently override the shared visual skills. Reusable visual feedback belongs in the existing canonical skill or feedback ledger, with its Claude-compatible copy kept aligned.

- Initial learning begins with the owner's hook references from multiple games.
- Phase one uses supplied knowledge and the Hook Analyzer brief without Game DNA. Game accuracy remains unassessed; creative inventions must not be recorded as verified game facts.
- Handoff: Hook Analyzer brief -> Art Director story and visual directions -> Higgsfield generation. Art Director owns the story, visual directions, and production prompts; Higgsfield executes them.
- Sequence: static first-frame mock -> 4–5 storyboard images -> smaller-scale draft video -> upscale -> Mixer handoff.
- Art Director reviews and approves each stage itself, with feedback loops before advancing. The production rules establish the scoring gate; detailed scoring anchors will develop through reference analysis and owner feedback.
- Hook Analyzer is the upstream project role defined in `skills/hook-analyzer/SKILL.md`; it analyzes references and writes briefs using `Hooks/templates/hook-analyzer-brief.md`. Mixer implementation comes later.
- This folder setup does not implement generation, automatic video ingestion, or autonomous approval tooling.

Reference observations, interpretations, owner preferences, and measured performance remain distinct. A reference alone does not prove that a hook performs well. Link canonical learnings into the Obsidian vault instead of copying them into multiple knowledge stores.
