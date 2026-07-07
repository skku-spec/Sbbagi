---
name: hermes-profile-portability
description: Package a Hermes profile for reuse on another machine without leaking secrets; install wrappers, cron scripts, and sanitized profile templates.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, profiles, portability, setup, github, secrets, cron]
---

# Hermes Profile Portability

Use this when a user wants to copy an existing Hermes persona/profile to another machine or publish it to a repository for future installs.

## Core workflow

1. **Separate portable artifacts from live runtime state.** Copy only reusable configuration, scripts, memory templates, and docs. Do **not** copy OAuth tokens, API keys, `.env`, `auth.json`, Google client secrets, session databases, logs, cron outputs, or downloaded user documents.
2. **Create a profile template directory** such as `profiles/<profile-name>/` with:
   - `config.yaml` containing safe defaults only.
   - `memories/USER.md` for durable persona/user preferences.
   - `memories/MEMORY.md` for non-secret operational notes.
   - `scripts/` for reusable cron/watchdog scripts.
3. **Add a repository `.gitignore` before staging.** Block `.env`, `auth.json`, `google_token.json`, `google_client_secret.json`, `state.db*`, `logs/`, `sessions/`, `cron/output/`, `state/*.json`, venvs, and caches.
4. **Provide an installer script** that copies the template into `$HERMES_HOME/profiles/<name>` and creates wrapper commands like `~/.local/bin/spakki` that run `hermes -p <name> "$@"`.
5. **Document per-machine setup explicitly.** New machines must run Hermes setup/model auth, gateway setup, and any Google OAuth flow again. Credentials are never portable through a public or shared repo.
6. **For cron/watchdog portability, store templates not live jobs.** Include the script and a JSON/README command showing how to recreate the cron job. Live `cron/jobs.json` often contains delivery channel IDs, timestamps, local profile names, and other machine-specific state.
7. **Verify before commit.** Run syntax checks for scripts/configs and a lightweight secret scan for common tokens/private keys. Then inspect `git diff --cached --stat` before committing.

## GitHub push/auth options on headless servers

- Prefer an already-configured `gh` or git credential helper if available.
- If the user can provide a PAT, use `gh auth login --with-token` or a one-time push URL without printing or storing the token in logs.
- If browser/device auth is awkward from a gateway/headless session, use SSH: generate an ed25519 key, show only the `.pub` key to the user, have them add it at GitHub SSH keys, then switch the repo remote to `git@github.com:owner/repo.git` and push.
- Never commit generated private keys; keep them under `~/.ssh` with `600` permissions.

## Privacy rules

- If the live profile handled Gmail, Discord, Google Workspace, or club operations, assume local files may contain personal data.
- Do not publish message bodies, attachments, IDs that identify private channels unless the user explicitly wants a private repo artifact and understands the risk.
- For Gmail watchdogs, keep script output privacy-safe: no attachment contents, mask obvious resident-registration numbers and long numeric identifiers, and stay silent when there is no new mail.

## References

- `references/spakki-profile-export.md` — example structure and lessons from exporting a SPEC/스빡이 Hermes profile to GitHub.
