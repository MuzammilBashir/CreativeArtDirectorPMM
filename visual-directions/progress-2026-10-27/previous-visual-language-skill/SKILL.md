---
name: visual-language
description: Define and review the visual language of mobile-game ads, including color, contrast, art style, shape, materials, lighting, typography, visual hierarchy, and consistency.
metadata:
  short-description: Visual style and consistency for mobile-game ads
---

# Visual Language

## Purpose

Translate an approved creative brief and game identity into a coherent visual system for mobile UGC and gameplay ads. Define how the creative should look; do not replace the Creative Strategist’s concept or campaign hypothesis.

## Inputs

- Approved creative brief
- Game profile and verified gameplay sources
- Existing brand or art direction
- Target audience and placement
- Relevant genre and format playbooks
- Approved references and provenance status

## Define

### Color

- Primary, secondary, accent, background, warning, success, and CTA roles
- Contrast between gameplay, text, UI, and background
- Color hierarchy and emotional intent
- Color behavior across light and dark scenes
- Color-blind-safe alternatives where required

Do not choose colors only because they are fashionable. Every color should improve recognition, hierarchy, emotion, or game identity.

### Art style

- 2D, 3D, live-action, hybrid, or stylized treatment
- Shape language
- Line quality
- Detail level
- Materials and textures
- Character and prop treatment
- Environment treatment
- Lighting and shadow language
- UI and icon treatment
- Typography and caption hierarchy

### Visual hierarchy

Define the order in which the viewer should notice:

1. Hook or focal subject
2. Gameplay action or proof
3. Consequence, reward, or failure
4. Supporting text
5. CTA or brand

### Consistency

Check that characters, objects, colors, typography, lighting, camera treatment, and effects belong to the same visual system across the asset family.

## Style direction output

~~~yaml
visual_direction_id:
game_id:
concept_id:
visual_tone:
art_style:
shape_language:
color_roles:
contrast_rules:
lighting:
materials:
character_rules:
environment_rules:
ui_and_typography:
visual_hierarchy:
approved_references:
reference_boundaries:
out_of_style:
mobile_readability_notes:
~~~

## Review rules

- Judge the actual asset, not its description.
- Review at intended mobile size and placement crop.
- Reject generation artifacts, inconsistent characters, broken anatomy, unreadable text, and accidental style changes.
- Do not approve visual polish that hides inaccurate gameplay.
- Use references for principles, not copied expression.
- Record source and usage status for references and generated assets.

## Boundaries

This skill does not choose the campaign idea, write the primary strategy, define device exports, or implement animation systems. It may flag problems in those areas but routes them to the appropriate skill or agent.

