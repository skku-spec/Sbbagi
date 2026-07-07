---
name: runtime-debugging-tools
description: "Use when attaching live debuggers to Python or Node.js processes with pdb, debugpy, node inspect, or Chrome DevTools Protocol."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [debugging, python, nodejs, debugpy, pdb, inspector]
    related_skills: [software-delivery-methods]
---

# Runtime Debugging Tools

## Overview

This umbrella covers process-level interactive debugging for Python and Node.js. It is separate from general systematic debugging: use it when breakpoints, stack inspection, watch expressions, or live process attachment are the right evidence-gathering mechanism.

Former packages are preserved under `references/source-packages/python-debugpy/` and `references/source-packages/node-inspect-debugger/`.

## When to Use

- A failing test or server needs breakpoints or stack inspection.
- Logs are insufficient and the bug depends on runtime state.
- You need to attach to a running Python/Node process.

## Tool Choice

- **Python**: use `pdb` for local CLI/test debugging; use `debugpy` when a Debug Adapter Protocol client or remote attach flow is needed.
- **Node.js**: use `node inspect` for terminal debugging or the inspector/Chrome DevTools Protocol for running processes.

## Workflow

1. Reproduce the failure normally first.
2. Launch or attach with the smallest debugger surface that answers the question.
3. Inspect stack/locals/state; form a root-cause hypothesis.
4. Exit cleanly and apply a minimal fix.
5. Re-run the original reproducer and relevant regression tests.

## Source Guides

- Python: `references/source-packages/python-debugpy/source-skill.md`
- Node.js: `references/source-packages/node-inspect-debugger/source-skill.md`

## Verification Checklist

- [ ] Failure reproduced before debugging.
- [ ] Breakpoint/attach command is recorded.
- [ ] Root cause is tied to observed runtime state.
- [ ] Original failure is re-tested after the fix.
