# Hermes install notes for insane-search

Use this when a repo provides `insane-search` as a Claude Code plugin but the active environment is Hermes Agent.

## Install shape

1. Clone the repo somewhere outside the skill library:
   ```bash
   cd /data
   git clone https://github.com/fivetaku/insane-search.git
   ```
2. Copy the actual skill payload into the Hermes skill library:
   ```bash
   cp -a /data/insane-search/skills/insane-search /data/skills/insane-search
   ```
3. Disable or remove Claude-only first-run setup/star-prompt instructions from `SKILL.md` if present. Hermes does not have Claude Code's plugin marketplace flow or AskUserQuestion hook.
4. Prefer absolute working-directory commands in the skill body:
   ```bash
   cd /data/skills/insane-search && python3 -m engine "<URL>" [options]
   ```

## Python dependencies

Install the runtime and verification dependencies in the user Python environment:

```bash
python3 -m pip install --user --upgrade \
  curl_cffi feedparser yt-dlp \
  beautifulsoup4 PyYAML lxml pytest
```

`beautifulsoup4` is needed for selector validation, and `PyYAML` is needed for loading `engine/waf_profiles.yaml`. Without them the engine falls back/degrades and smoke tests may fail even though the CLI imports.

## Verification

The included smoke test is not pytest-discoverable: functions are named `t_*` and the file has its own `main()` runner. Run it directly:

```bash
cd /data/skills/insane-search
python3 engine/tests/test_smoke.py
```

Expected healthy result:

```text
8 passed, 0 failed
```

Then verify the CLI entry point:

```bash
cd /data/skills/insane-search
python3 -m engine https://example.com --selector h1 --json --no-playwright
```

Expected signs of success: JSON with `"ok": true`, `"verdict": "strong_ok"`, and a `curl_cffi` probe trace.

## Pitfalls

- `python3 -m pytest engine/tests/test_smoke.py` can report `no tests ran`; this is not proof the install is broken. Use the direct script runner above.
- Do not persist a general rule that Claude/Playwright/gh are unavailable just because a fresh environment lacks those binaries. Capture only the install/verification path above.
- Keep repo clone (`/data/insane-search`) separate from the active Hermes skill (`/data/skills/insane-search`) so future updates can diff upstream vs installed skill cleanly.
