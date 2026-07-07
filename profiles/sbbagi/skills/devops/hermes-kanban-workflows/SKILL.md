---
name: hermes-kanban-workflows
description: "Use when orchestrating or working Hermes Kanban boards: decomposition, worker lifecycle, tenant/workspace isolation, task completion, and block handling."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, kanban, orchestration, workers, devops]
    related_skills: [hermes-agent]
---

# Hermes Kanban Workflows

## Overview

This umbrella combines the orchestrator and worker sides of Hermes Kanban. The class-level workflow is durable multi-agent task routing: decompose work, assign cards, maintain isolation, capture worker outputs, and unblock or complete tasks with useful metadata.

Former packages are preserved under `references/source-packages/kanban-orchestrator/` and `references/source-packages/kanban-worker/`.

## When to Use

- A task should be routed through a durable board rather than handled in the current chat.
- You are acting as an orchestrator decomposing work for profiles/workers.
- You are a worker handling a claimed card and need lifecycle/pitfall guidance.

## Orchestrator Pattern

- Create cards only when the board adds value: parallelism, durability, profile specialization, or long-running execution.
- Make tasks independently actionable with paths, acceptance criteria, blockers, and expected artifacts.
- Resist doing the implementation work inside the orchestrator; route it.

## Worker Pattern

- Treat board, workspace, and tenant as hard boundaries.
- Capture IDs returned by board operations before claiming or linking tasks.
- Complete with a concise summary plus machine-usable metadata.
- Block early with a specific question when missing context prevents safe progress.

## Source Guides

- Orchestrator: `references/source-packages/kanban-orchestrator/source-skill.md`
- Worker: `references/source-packages/kanban-worker/source-skill.md`

## Verification Checklist

- [ ] Task is appropriate for board routing.
- [ ] Cards contain enough context for a no-history worker.
- [ ] Worker respects board/workspace isolation.
- [ ] Completion/block comments are specific and actionable.
