# Spakki profile export session notes

This reference captures a reusable pattern from packaging the SPEC “스빡이” Hermes profile into a GitHub repository for installation on other machines.

## Repo shape that worked

```text
.gitignore
README.md
profiles/sbbagi/config.yaml
profiles/sbbagi/memories/USER.md
profiles/sbbagi/memories/MEMORY.md
profiles/sbbagi/scripts/gmail_spec_watchdog.py
cron/gmail_spec_watchdog.template.json
scripts/install_profile.sh
```

## What to include

- Persona/user preference memory that is safe and durable.
- Safe `config.yaml` defaults: model/provider names, display preferences, toolsets, Discord behavior, memory limits, security redaction.
- Reusable scripts such as script-only Gmail watchdogs.
- Installer script that copies files into `$HERMES_HOME/profiles/<profile>` and creates wrapper binaries.
- README steps for fresh-machine auth: `hermes -p <profile> setup`, `gateway setup`, and Google OAuth token creation.

## What to exclude

- Google OAuth token/client secret files.
- `.env`, `auth.json`, Discord tokens, API keys.
- `state.db*`, sessions, logs, cron output, `.tick.lock`, runtime state JSON.
- Downloaded Gmail attachments, extracted documents, IDs, private channel data, or personal documents.

## Gmail watchdog portability lesson

If the user asks for a general inbox monitor, do not hard-code sender filters. Use a query like:

```text
in:anywhere newer_than:30d -in:sent -in:drafts -in:trash -in:spam
```

Track seen message IDs in a profile-local state file. On first run, mark existing matches as seen and print nothing. With Hermes cron, create it as a script-only job (`no_agent=true`) so empty stdout stays silent and no LLM tokens are spent.

## Headless GitHub auth lesson

If HTTPS push fails because there is no credential helper and `gh auth login --web` is awkward from a gateway/headless session, the durable fallback is SSH:

1. Generate key: `ssh-keygen -t ed25519 -C 'hermes-agent' -f ~/.ssh/<keyname> -N ''`.
2. Show only the `.pub` key to the user.
3. User adds it in GitHub → Settings → SSH and GPG keys.
4. Configure `~/.ssh/config` for `github.com` with the private key.
5. Set remote to `git@github.com:owner/repo.git` and push.

Do not record this as “gh auth does not work”; the durable lesson is to offer PAT or SSH fallback when browser/device login is unsuitable for the active channel.
