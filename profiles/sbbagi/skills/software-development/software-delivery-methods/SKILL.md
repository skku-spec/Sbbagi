---
name: software-delivery-methods
description: "Use when planning, validating, reviewing, debugging, or test-driving software changes: plan mode, spikes, TDD, systematic debugging, and pre-commit review."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [software-development, planning, debugging, testing, review, tdd]
    related_skills: []
---

# Software Delivery Methods

## Overview

This umbrella captures method-level software engineering workflows. The shared class is not a language or tool; it is how an agent should de-risk code changes: plan when execution is premature, spike uncertainty, debug from root cause, write tests first where possible, and review before committing.

Former packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- The user asks for a plan, not execution.
- An implementation idea needs a throwaway experiment before committing to it.
- A bug must be understood before fixing.
- The user wants strict TDD or the task is testable and regression-prone.
- A code change should be reviewed before commit/push.

## Method Map

1. **Plan mode**: produce an actionable markdown plan and stop; do not execute.
2. **Spike**: isolate uncertainty in a disposable experiment, then return a verdict.
3. **Systematic debugging**: reproduce, inspect evidence, identify root cause, then fix.
4. **TDD**: RED-GREEN-REFACTOR with real test output at each stage.
5. **Pre-commit review**: diff, security scan, quality gates, auto-fix, and final verification.

## Source Packages

- `references/source-packages/plan/`
- `references/source-packages/spike/`
- `references/source-packages/systematic-debugging/`
- `references/source-packages/test-driven-development/`
- `references/source-packages/requesting-code-review/`

## Verification Checklist

- [ ] The chosen method matches the user's intent and risk level.
- [ ] Evidence is real tool output, not intuition.
- [ ] Plans/spikes/debugging notes include paths and next actions.
- [ ] Final answer states what was verified.
