---
name: aspect-ratio-delivery
description: Prepare and review mobile-game ad compositions for aspect ratios, device classes, safe areas, resolution, cropping, and platform delivery requirements.
metadata:
  short-description: Mobile ad sizing and delivery preparation
---

# Aspect Ratio and Delivery

## Purpose

Ensure that a creative remains understandable, attractive, and technically usable across mobile placements and device classes.

This skill defines delivery behavior. It does not replace current platform documentation or invent specifications that were not checked.

## Core formats

Start with the requested placement. Common working canvases include:

- 9:16 portrait
- 4:5 feed portrait
- 1:1 square
- 16:9 landscape

Do not assume one master crop will work everywhere.

## Device classes

Design and test against classes rather than relying on one model:

- Modern iPhone portrait
- Older or smaller iPhone portrait
- Standard Android portrait
- Tall Android portrait
- Android with camera cutout or rounded corners
- Small and large tablets
- Foldable or unusual aspect-ratio screens when relevant

Named device models may be used for verification, but the system should reason about viewport classes, aspect ratio, pixel density, safe areas, and crop behavior.

## Composition rules

Maintain:

- A crop-safe focal action
- Text and CTA inside the safe area
- Adequate margins around gameplay
- Readable UI at delivery size
- A clear hierarchy after resizing
- No dependency on a single screen’s exact pixel dimensions

Separate:

~~~text
Creative canvas: the original composition.
Delivery canvas: the platform-specific export.
Safe area: the region where critical content remains visible.
~~~

## Technical delivery checklist

Verify from current platform requirements:

- Aspect ratio
- Pixel resolution
- Duration
- Frame rate
- File type and codec
- Bitrate or file size
- Audio behavior
- Naming and version
- Caption and CTA safe area
- Crop preview

Never invent a platform specification. If the current requirement is not available, mark it unknown and block delivery-specific approval.

## Adaptive versioning

Create a master composition and platform-specific versions when needed. Track what changes:

- Camera crop
- Text position
- UI scale
- CTA position
- Gameplay window
- Caption line breaks
- End-card layout

Do not change the creative hypothesis while adapting the delivery canvas.

## Delivery output

~~~yaml
delivery_plan_id:
asset_id:
platform:
placement:
aspect_ratio:
resolution:
duration:
frame_rate:
codec:
audio:
safe_area:
device_classes_checked:
crop_variants:
technical_sources:
unknown_requirements:
status: ready | revise | blocked
~~~

## Review rules

- Review the actual export, not only the master.
- Inspect at mobile size and in placement context.
- Check first-second comprehension after every crop.
- Confirm critical gameplay is not removed or altered.
- Confirm text, UI, and CTA survive all intended versions.

## Boundaries

This skill does not choose the creative concept, define visual style, or direct animation and sound. It can request changes from those skills when delivery constraints expose a problem.

