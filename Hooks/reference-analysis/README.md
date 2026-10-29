# Hook reference analysis

Date: 2026-10-29.

## Current coverage: 15 of 15 reports saved

All 15 source videos now have hash-matched Gemini reports. Subsequent Flash-Lite runs completed knitting, marbles, soapcutting, strawberina, Hook_Aging, wifeplayinggame, and Hollywood Crush. A final delayed retry completed `hf_20261007_123830_cc87edb5-6a8d-40c7-9243-58fe10d11f7d.mp4`.

See [current per-video report paths](current-status.json) for authoritative saved-report coverage. `batch-status.json` describes a particular batch and may omit the final single-video retry. Sections below are historical progress records.

**Completion means model reports are saved, not that all statements are verified.** All sources have local sampled-frame surveys, but audio, precise timing and continuous motion still need full verification. Existing corrections are in `first-pass-review.md`, `additional-references-review.md`, and neighboring `review.md` files. No report is production approval or a validated performance learning.

## Model fallback test

Gemini 3.1 Flash-Lite successfully analyzed `Hook_NoMeTime.mp4` after the retry batch below, bringing the saved-report total to **7 of 15**. Eight remain incomplete. The report is model-generated and pending full review. A test with `gemini-3.7-flash` returned 429; Google's current documentation says that model routes to 3.8 Flash, so it is not an independent fallback. The batch runner now accepts an explicit model, runs sequentially with a delay, stops dispatch after 429, and disables SDK automatic retries. Previous `batch-status.json` remains a historical batch snapshot, not the current total.

## Latest retry: 15 references

The owner added `Hook_Aging.mp4` and `Hook_NoMeTime.mp4` and requested a retry excluding the four completed reports. All 11 incomplete/new files were attempted once by the batch runner. The original four each still have one saved report and were skipped.

- **6 total Gemini reports available:** the original four plus `hf_20261007_121650_5168a466-b043-4f94-9874-c981bce80e07.mp4` and `iq140night.mp4`.
- **9 incomplete:** `hf_20261007_123830_cc87edb5-6a8d-40c7-9243-58fe10d11f7d.mp4`, `Hook_Aging.mp4`, `knitting.mp4`, `soapcutting.mp4`, and `wifeplayinggame.mp4` returned 504; `Hook_NoMeTime.mp4` returned 503; `marbles.mp4`, `strawberina.mp4`, and the Hollywood reference returned 429 RESOURCE_EXHAUSTED. The 429 response does not establish whether the cause is a short-term rate limit or account quota.
- All 15 now have local metadata and inspected sampled-frame contact sheets. This does not substitute for full audio/motion analysis.
- [New reference visual observations](additional-references-review.md) cover the two additions.
- Each newly completed report has a neighboring `review.md` flagging uncertain claims; none is production-approved.

The current [batch results](batch-status.json) are the retry record. The initial attempt is summarized below for history. Before another API batch, resolve or allow recovery from the reported service/rate limits; reuse all six saved reports.

## Initial pass history

- 13 source videos inventoried; all have audio tracks and portrait dimensions.
- All 13 contact sheets inspected at one frame per second. This is a partial visual survey, not full motion/audio validation.
- Four Gemini 3.8 Flash reports completed: cathook, asmrstar, girlfriendcrying, iq140day.
- Nine Gemini analyses remain incomplete. The hf_ videos, wifeplayinggame and Hollywood reference returned service-unavailable errors; iq140night, knitting, marbles, soapcutting and strawberina returned deadline-exceeded errors. The Hollywood filename encoding problem was repaired; its subsequent retry reached the service but returned 503.
- No production assets have been generated or approved. No performance metrics or Game DNA are available.

## Read first

- [Reviewed observations and Gemini corrections](first-pass-review.md)
- [Collection study brief for Art Director](../briefs/collection-study-v1.md)
- [Cathook reference brief](../briefs/cathook-reference-study-v1.md)
- [Technical inventory](video-inventory.json)
- [Latest API batch results](batch-status.json)

Original Gemini reports are preserved in each successful reference's hash-named directory. Their model-generated claims must be read alongside the corrections. Do not use their estimated timestamps as exact measurements.

Next analysis work: retry the nine currently incomplete API analyses when service/quota permits, verify essential audio/motion claims, and refine the draft study briefs. Saved successful analyses should be reused rather than regenerated.
