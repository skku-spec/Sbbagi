---
name: github-workflows
description: "Use when operating GitHub repositories end-to-end: authentication, cloning/forking, issues, PRs, reviews, CI, releases, and codebase inspection."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [github, git, gh, pull-requests, issues, code-review, repositories]
    related_skills: []
---

# GitHub Workflows

## Overview

A single umbrella for GitHub operations. Most tasks combine authentication, repository inspection, branch/commit work, PR creation, issue management, CI interpretation, and review. Use this class-level skill first, then jump to the relevant source package for exact commands/templates.

Former packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- Configuring GitHub auth or diagnosing `gh`/git credential issues.
- Cloning, forking, creating, releasing, or managing repositories.
- Creating/triaging issues or PRs.
- Reviewing local changes or remote PRs.
- Inspecting codebase size/language composition before a GitHub task.

## Workflow Map

1. **Auth**: check `gh auth status`, remotes, SSH/HTTPS, and token scope before write operations.
2. **Repo management**: clone/fork/create repos, configure remotes, and verify origin/upstream.
3. **Inspection**: use pygount or targeted file searches to understand codebase shape before changing it.
4. **Issues**: search before creating duplicates; use labels/assignees only after confirming repo conventions.
5. **PR lifecycle**: branch from up-to-date base, commit with conventional messages, open PR, monitor CI, and respond to review.
6. **Code review**: inspect diffs, run security/static checks, leave actionable comments, and verify suggested fixes.

## Source Packages

- `references/source-packages/github-auth/`
- `references/source-packages/github-repo-management/`
- `references/source-packages/github-issues/`
- `references/source-packages/github-pr-workflow/`
- `references/source-packages/github-code-review/`
- `references/source-packages/codebase-inspection/`

## Verification Checklist

- [ ] Auth and remotes are valid for the intended operation.
- [ ] Current branch/base branch are known.
- [ ] Changes are reviewed with `git diff` and tests where applicable.
- [ ] Remote side effects are verified with `gh` or API output.
