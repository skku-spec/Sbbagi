# Sbbagi Preservation Report

Date: 2026-06-18

## Target

- Profile name: `spbaki`
- Expected profile directory: `/Users/slit/.hermes/profiles/spbaki`
- Destination repository: `https://github.com/skku-spec/Sbbagi.git`

## What Was Still Present

- `/Users/slit/.local/bin/spbaki`

Content:

```sh
#!/bin/sh
exec hermes -p spbaki "$@"
```

## What Was Missing Before This Commit

These paths did not exist when preservation began:

- `/Users/slit/.hermes`
- `/Users/slit/.hermes/profiles/spbaki`
- `/Users/slit/.local/state/hermes`
- `/Users/slit/hermes-agent`
- `/Users/slit/hermes-agent-finalization-hooks`
- `/Users/slit/hermes-agent-update-integration`
- `/Users/slit/hermes-agent-update-20260521`
- `/Users/slit/Library/LaunchAgents/ai.hermes.gateway-spbaki.plist`

No active `ai.hermes.gateway-spbaki` or `hermes_cli.main --profile spbaki`
process was found after the interrupted deletion was stopped.

## Recovery Checks Attempted

- Direct filesystem checks for the profile path.
- Filename search for `spbaki` outside restricted macOS folders.
- Text search for `spbaki` in remaining shell/tool transcripts.
- GitHub repository access check.
- Time Machine query via `tmutil listbackups`.

`tmutil listbackups` returned `Operation not permitted`, so Time Machine backup
contents could not be inspected from this session.

## Upload Policy

The destination repository is public. Full Hermes profiles can contain API keys,
OAuth tokens, Discord tokens, private chat logs, and personal data. No secret
material was uploaded.
