---
name: apple-ecosystem
description: "Use when operating Apple/macOS apps and device workflows: Notes, Reminders, iMessage/SMS, Find My, or general GUI computer-use automation."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [apple, macos, notes, reminders, imessage, findmy, computer-use]
    related_skills: []
---

# Apple Ecosystem Workflows

## Overview

Use this umbrella for Apple/macOS task execution where Hermes needs to drive local Apple apps, CLIs, or GUI automation. It consolidates the former one-tool-per-app skills into a single decision tree so the agent searches one class-level entry and then chooses the appropriate subsection.

The original skill packages are preserved under `references/source-packages/<skill-name>/` for complete commands, examples, and edge-case notes.

## When to Use

- Managing Apple Notes or Reminders on macOS.
- Sending or reading iMessage/SMS through local macOS tooling.
- Locating Apple devices or AirTags with Find My.
- Driving arbitrary macOS GUI workflows with screenshots, AppleScript, or computer-use primitives.

## Decision Tree

1. **Structured app CLI exists**: prefer the app-specific CLI (`memo`, `remindctl`, `imsg`) because it is deterministic and scriptable.
2. **No direct CLI exists**: use AppleScript or GUI automation, then verify with screenshots or queried state.
3. **Location/device state**: use Find My workflows and explicitly communicate accuracy/latency limitations.
4. **Any destructive action**: confirm scope before deleting, sending, completing, or modifying user data.

## App Subsections

- Notes: `references/source-packages/apple-notes/source-skill.md`
- Reminders: `references/source-packages/apple-reminders/source-skill.md`
- iMessage/SMS: `references/source-packages/imessage/source-skill.md`
- Find My: `references/source-packages/findmy/source-skill.md`
- macOS GUI computer-use: `references/source-packages/macos-computer-use/source-skill.md`

## Verification Checklist

- [ ] The host is macOS or the required Apple service/CLI is reachable.
- [ ] Recipient, note title, reminder list, or device target is unambiguous.
- [ ] State-changing actions are verified by reading back app state or screenshot evidence.
- [ ] User-facing output includes limitations for location and GUI automation accuracy.
