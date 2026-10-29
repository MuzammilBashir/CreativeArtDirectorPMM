# Hook production rules

Recorded: 2026-10-29. These are the owner's production requirements. Implementation interpretations are labeled separately below. This document does not authorize new spending or claim that Higgsfield automation is connected.

## Owner requirements

1. Higgsfield uses the cheapest suitable, capable model for draft images and videos to conserve generation budget.
2. Each production step has three attempts, with two options for selection.
3. Image drafts, including concept mocks, first frames and storyboard images, use the selected Higgsfield model's smallest supported output resolution. Choose the lowest-cost capable model; do not force 480p when the image model does not support it. Updated by the owner on 2026-10-29.
4. Video drafts are 480p.
5. Higgsfield iterates on the same video three times using Art Director feedback.
6. Final video output is 720p.
7. The completed hook is 4–5 seconds long.
8. Art Director is the scorer and final judge, scoring Visual, Story Matching, and Game DNA.
9. A score of 90% or higher approves the hook.
10. Emotional engagement is the central purpose of every hook. Each hook must be meaningful and serve the brief's purpose. Art Director develops its own story and visual directions from the brief before asking Higgsfield to generate mocks.

## Story and emotional direction before mocks

Before the first-frame prompt, Art Director records:

- **Purpose:** what this hook should accomplish for the supplied idea.
- **Intended feeling:** the primary emotion or emotional response, such as curiosity, empathy, anticipation, amusement, satisfaction, relief, or challenge.
- **Reason to care:** the recognizable desire, situation, tension, or sensory experience that makes the hook meaningful.
- **Story:** an original, readable 4–5 second progression that expresses the idea. Reference beats are inspiration, not a locked script. A simple action and consequence can be a story; elaborate drama is not required.
- **Visual direction:** how the first frame, focal subject, expression/action, composition, camera, light, color, motion and sound support the intended feeling, using the existing shared visual skills.
- **Ending:** the payoff or purposeful open question, and intended connection to the following segment. Mark an unknown Mixer connection explicitly.

These fields operationalize the owner's direction; they do not prescribe one emotion or narrative formula for every hook. Intended emotional effect is a hypothesis until audience evidence supports it. Do not equate shock, sadness, decorative spectacle or visual polish alone with meaningful engagement.

Art Director checks that the story serves the brief and that each major beat contributes before sending prompts to Higgsfield. If purpose or emotional logic is unclear, revise the story before generating mocks. Higgsfield executes the supplied story/visual direction rather than independently redefining the idea.

## Working interpretations

These details make the rules executable but are not additional owner-specified requirements. Revise them if the owner clarifies a different intent.

- **Attempt budget:** Treat the three-attempt rule as a maximum of three total rounds per step, including the initial round. Each round produces two alternatives, A and B. For storyboard work, an alternative is a coherent set of 4–5 frames. This permits up to six alternatives per step; stop early when a suitable option passes. The video iteration requirement uses this same three-round budget, rather than adding three revisions after three initial attempts. Whether the owner intends three revisions after the initial video remains to be confirmed before paid production.
- **Feedback:** Revisions address the same selected video concept and Art Director's recorded findings. Store both options, the selection, scores, failed criteria, and specific feedback. Exhausting attempts without approval means blocked/revise, never automatic approval or a reset budget.
- **Image resolution:** Preserve the intended aspect ratio and use the selected model's smallest supported native resolution for all draft stills. Record that setting and actual output dimensions. Downsampled review copies are optional and do not reduce generation cost. A model minimum above 480p no longer requires an image-resolution exception.
- **Video resolution:** Draft videos remain 480p and final videos remain 720p. Interpret these as 480 and 720 pixels on the short edge respectively (for example, 480 x 854 and 720 x 1280 for portrait output). Confirm supported dimensions before generation. If native video draft resolution is unavailable, record the limitation and resolve the cost/resolution choice before spending; resizing a higher-resolution generation does not reduce its generation cost.
- **Model selection:** Check currently available models, credits/prices, supported resolution/duration, reference controls, and task suitability at execution time. Choose the lowest-cost capable option based on that evidence, not a permanently hardcoded model name or an unsupported quality claim. Record the model and expected/actual credits when available.
- **Timing:** The total delivered video is 4–5 seconds, not 4–5 seconds per storyboard frame. Verify actual duration and dimensions on the exported file.

## Scoring and approval

Use the existing Art Director visual skills and owner feedback ledger; do not create a competing visual standard.

Score each applicable category from 0 to 100, with specific evidence from the actual video:

| Category | Evaluation basis |
| --- | --- |
| Visual | Existing visual standards, composition, readability, motion, continuity, and visible defects |
| Story Matching | Fidelity to the brief's purpose and approved story; meaningful progression, intended emotional engagement, and hook/payoff delivery. Cite visible/audible execution evidence without claiming proven audience response. |
| Game DNA | Fidelity to supplied Game DNA when it exists |

**Provisional weighting:** Use equal weights because the owner has not specified weights.

- Phase one has no Game DNA: report `Game DNA: N/A — not supplied`, and calculate `(Visual + Story Matching) / 2`. Never award an invented DNA score or describe game accuracy as approved.
- When Game DNA is supplied: calculate `(Visual + Story Matching + Game DNA) / 3`.
- Compare the unrounded aggregate to 90. A score of at least 90 passes the scoring gate. Explain each score; subjective creative scores are not measured performance evidence.
- Mandatory production requirements and existing applicable critical blockers still apply independently of the average. A wrong duration/resolution or other critical failure requires revision even if the creative score is high.
- Review first frames and storyboards before advancing, using applicable visual/story criteria. Motion and other uninspectable aspects remain unassessed until the actual video exists.
- After draft approval, create the 720p final, inspect and score that actual export, and verify its duration/dimensions before Mixer handoff. Draft approval alone does not approve an unchecked upscale.

## Handoff record

Include the approved final file, brief/story reference, model, generation settings, attempt/version IDs, review scores and rationale, duration, resolution, Game DNA availability, and any remaining limitations. Mixer development remains outside the current task.
