---
name: creative-visual-design
description: "Use when creating visual/design artifacts: web mockups, design systems, diagrams, infographics, Excalidraw, DESIGN.md tokens, p5.js, Pretext, or ASCII art/video."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [creative, design, diagrams, web, infographic, p5js, ascii, excalidraw]
    related_skills: []
---

# Creative Visual Design

## Overview

This umbrella covers visual artifact production. The common workflow is choosing the right visual medium, generating an editable artifact, and verifying that the output renders or opens. Large source packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- HTML/CSS mockups, landing pages, style references, or design-system-inspired screens.
- Architecture diagrams, Excalidraw, infographics, DESIGN.md token specs.
- Generative sketches, browser demos, p5.js, Pretext, ASCII art, or ASCII video.
- Humanizing/rewriting copy as part of a designed artifact.

## Medium Selection

- **Fast mockups**: sketch or popular-web-designs.
- **One-off polished HTML artifact**: claude-design.
- **Cloud/architecture diagram**: architecture-diagram or Excalidraw.
- **Structured visual explainer**: baoyu-infographic.
- **Design tokens/spec**: design-md.
- **Generative/browser creative coding**: p5js or pretext.
- **Text-mode visuals**: ascii-art or ascii-video.
- **Copy polish**: humanizer.

## Source Packages

- `references/source-packages/architecture-diagram/`
- `references/source-packages/ascii-art/`
- `references/source-packages/ascii-video/`
- `references/source-packages/baoyu-infographic/`
- `references/source-packages/claude-design/`
- `references/source-packages/design-md/`
- `references/source-packages/excalidraw/`
- `references/source-packages/humanizer/`
- `references/source-packages/p5js/`
- `references/source-packages/popular-web-designs/`
- `references/source-packages/pretext/`
- `references/source-packages/sketch/`

## Verification Checklist

- [ ] Output medium matches the user goal and requested fidelity.
- [ ] Generated HTML/SVG/JSON/video/image renders or validates.
- [ ] Source/template paths are preserved for further edits.
- [ ] Final response includes the artifact path or native media attachment.
