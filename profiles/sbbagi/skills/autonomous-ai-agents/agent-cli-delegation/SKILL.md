---
name: agent-cli-delegation
description: Use when delegating coding or review work to external autonomous CLI agents such as Claude Code, OpenAI Codex, or OpenCode.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [agents, delegation, claude-code, codex, opencode, tmux, coding]
    related_skills: [hermes-agent]
---

# Agent CLI Delegation

## Overview

This umbrella covers launching, supervising, and extracting results from external coding agents. The common class is the orchestration pattern: pick an agent, give it a bounded task, run it in one-shot/background/tmux mode, monitor output, and verify artifacts before reporting success.

Complete former skill packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- The user explicitly asks to use Claude Code, Codex, or OpenCode.
- A task benefits from an isolated coding agent with its own context and terminal.
- You need parallel implementation/review work that is too large for a normal `delegate_task` child.

## Agent Choice

- **Claude Code**: good for feature implementation, PR-style edits, and repository navigation when its CLI is available.
- **Codex CLI**: good for OpenAI Codex-backed coding, background PTY sessions, and one-shot implementation/review tasks.
- **OpenCode**: good for OpenCode-based implementation and PR review, especially when a local binary is already configured.

## Orchestration Pattern

1. Confirm the binary is installed and authenticated.
2. Prefer one-shot mode for bounded tasks; use tmux/PTTY for interactive or long-running work.
3. Give the agent exact paths, acceptance criteria, and verification commands.
4. Capture output periodically; do not rely on claims of success.
5. Verify changed files, tests, and external side effects yourself.

## Source Guides

- Claude Code: `references/source-packages/claude-code/source-skill.md`
- Codex: `references/source-packages/codex/source-skill.md`
- OpenCode: `references/source-packages/opencode/source-skill.md`

## Common Pitfalls

- Starting an interactive CLI without PTY/tmux.
- Letting a child agent make unverified claims about commits, PRs, or tests.
- Forgetting `-w`/worktree isolation when multiple agents edit the same repo.

## Verification Checklist

- [ ] Binary and authentication checked.
- [ ] Task prompt contains paths, constraints, and done criteria.
- [ ] Output captured from the agent session.
- [ ] Parent verified artifacts/tests before final user report.
