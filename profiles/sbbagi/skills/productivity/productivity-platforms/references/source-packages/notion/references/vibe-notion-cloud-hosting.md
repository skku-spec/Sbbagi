# Vibe Notion on Cloud Hosts

`vibe-notion` is different from the official Notion API / `vibe-notionbot` path: it reads the `token_v2` session that the Notion desktop app already holds so the agent acts as the logged-in user, not as an integration bot.

## Durable requirements

To use `vibe-notion` in “act as the user” mode, the runtime must have:

1. A supported Notion desktop app installation (officially macOS or Windows desktop).
2. An interactive GUI session where the user can log into Notion Desktop.
3. Access to the desktop app’s local session data so `vibe-notion` can extract/store credentials, normally under `~/.config/vibe-notion/credentials.json` unless `VIBE_NOTION_CONFIG_DIR` is set.
4. Node/npm available to install the CLI: `npm install -g vibe-notion`.

A plain headless Linux VPS is usually the wrong shape for `vibe-notion` because it lacks a desktop app session. It can still run `vibe-notionbot` or Notion Integration API tooling.

## Cloud hosting guidance

Recommended for `vibe-notion` user-session mode:

- Windows Cloud VM / Windows VPS via AWS EC2 Windows, Azure VM, Google Compute Engine Windows, Vultr, Kamatera, Contabo, etc.
- macOS cloud via MacStadium, AWS EC2 Mac, MacinCloud, etc. This works but is often expensive for simple automation.

Lower-confidence / avoid unless tested:

- Linux desktop VM with unofficial Notion wrappers. Notion’s official desktop downloads are macOS/Windows, and `vibe-notion` may not find the same session layout in unofficial clients.

## Decision rule

- If the user needs edits/comments attributed to their personal Notion account and visibility equal to their logged-in session: recommend a Windows Cloud VM first, then macOS Cloud if they already need macOS.
- If bot attribution is acceptable or the deployment must stay on a headless server: recommend `vibe-notionbot`, `ntn`, or direct Notion Integration API with an integration token and explicit page/database sharing.

## Quick validation commands

After provisioning a GUI Windows/macOS machine and logging into Notion Desktop:

```bash
npm install -g vibe-notion
vibe-notion workspace list --pretty
```

For bot mode on any server:

```bash
npm install -g vibe-notion
export NOTION_TOKEN=***
vibe-notionbot auth status --pretty
```
