# Video review and Mixer handoff
Date: 2026-10-29
Art Director decision: APPROVED for internal silent hook handoff. Not a complete published ad or gameplay-accuracy approval.

## Selection and scores
A-v1: Visual 90, Story Matching 92, mean 91. Selected.
B-v1: Visual 89, Story Matching 90, mean 89.5. Not selected; its larger mid-exhale mouth/torso movement is less settled.
Game DNA: N/A, not supplied. Scores are subjective creative judgments, not performance predictions. First-frame crop and stylization limitations were accepted by the owner.

A preserves the exhausted opening and proceeds through laptop closure, left-hand phone pickup and a restrained smile. Identity, palette and hand roles remain recognizable in inspected frames. The exact prompted timestamps are not perfectly reproduced: laptop closure occurs earlier than planned, but order and total duration remain appropriate. No extra video attempt needed after A passed.

## Evidence and limits
- Both drafts: ffprobe confirms 480x854, 30 fps, 5.000 seconds, no audio stream.
- Direct inspection: 20 chronological samples per draft at 4 fps, at 240px-wide phone-preview scale. This does not inspect every interstitial frame.
- Gemini video review: ../../../reference-analysis/A-v1-d8b9bb924e/gemini-20261029T145947096285Z.md (resolve from project Hooks/reference-analysis if this relative link is unavailable).
- Gemini observations are model-assisted only. Its opening claim of a closed laptop is false; direct samples show it open then closing. A positive notification/unlock is unsupported because screen content is hidden. Its retention, universal-effect and platform-safe-area claims are unsupported and excluded. No such claims become project learnings.
- Motion fluency assessment uses sampled visual evidence plus model-assisted full-video input, not a human real-time playback check. Fine brief artifacts may remain.
- Storyboard reference camera slightly widens in video; emotional subject and actions remain readable.

## Final export
File: ../06-final/HOOK-001-720p-silent-v1.mp4
Source: ../05-video-drafts/A-v1.mp4
Higgsfield job: 9770a699-5259-4746-b8f0-304e71825ac8
Generator: Wan 3.0, native 480p, 5s, audio disabled.
Export: local FFmpeg Lanczos scale to 720x1280, H.264, CRF18, yuv420p, 30fps, faststart. Standard resampling, NOT AI enhancement and NOT newly synthesized detail. Minor aspect correction from 480x854 to exact 9:16.
Verified exported duration 5.000s and dimensions 720x1280. Export contact sheet inspected: same story sequence, no newly apparent defects at sampled preview scale. Final creative scores retained at Visual90/Story92; upscale alone earns no score increase.
Usage/license status: unknown; internal generated draft/handoff, no legal clearance claim.

## Mixer instructions
Use as silent 5-second opening. Preserve exhaustion -> choice -> anticipation order. Add synchronized laptop click and subtle exhale if sound is wanted; avoid keyboard taps when hands are not typing. Optional low room tone. Attach verified gameplay after final phone beat once game/DNA is supplied; no destination gameplay was provided. No spoken VO or embedded text is included. Mixer implementation remains outside this task; no message sent to an external recipient.

## Costs and provenance
First-frame three rounds: 1.5 quoted credits total.
Storyboard first round: six new stills plus reused approved opening = 1.5 quoted credits.
Video first round: two outputs = 10 quoted credits.
Quoted Higgsfield total: 13 credits, billing not independently verified. Gemini analysis cost not quoted here.
Exact prompts and reference/job IDs: ../02-prompts/attempt-2.json, attempt-3.json, storyboard-attempt-1.json, video-attempt-1.json; first-round first-frame record preserved separately.
