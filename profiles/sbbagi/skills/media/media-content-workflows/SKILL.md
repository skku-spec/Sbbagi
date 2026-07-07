---
name: media-content-workflows
description: "Use when searching, extracting, generating, or analyzing media content: GIFs, YouTube transcripts, audio features, and AI music/song workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [media, youtube, gif, audio, music, transcripts, spectrogram]
    related_skills: []
---

# Media Content Workflows

## Overview

This umbrella covers lightweight media retrieval, transcript extraction, audio analysis, and music/song generation. The shared class is transforming media into reusable content or artifacts with verified sources/outputs.

Former packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- Searching/downloading GIFs.
- Fetching YouTube transcripts for summaries, threads, blogs, or analysis.
- Creating spectrograms or extracting audio features.
- Generating music with HeartMuLa or crafting AI music/song prompts.

## Workflow Map

1. **Source retrieval**: capture URL, media ID, format, and license/attribution if relevant.
2. **Extraction**: transcripts, timestamps, metadata, audio features, or preview URLs.
3. **Generation**: lyrics/prompts/tags or model-specific generation commands.
4. **Verification**: check files exist, URLs resolve, and generated artifacts are playable/viewable.

## Source Packages

- `references/source-packages/gif-search/`
- `references/source-packages/youtube-content/`
- `references/source-packages/songsee/`
- `references/source-packages/heartmula/`
- `references/source-packages/songwriting-and-ai-music/`

## Verification Checklist

- [ ] Source URLs/IDs are recorded.
- [ ] Extracted text/features include relevant timestamps or metadata.
- [ ] Generated/downloaded files are verified on disk or by URL.
- [ ] User receives the requested artifact or concise summary.
