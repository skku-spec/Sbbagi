Google Workspace OAuth must be configured per machine/profile. Do not commit google_token.json, google_client_secret.json, auth.json, .env, logs, sessions, state.db, or cron output.
§
SPEC Gmail watchdog is script-only/no_agent and should stay quiet when there is no new mail. It monitors all incoming senders and excludes sent/drafts/trash/spam. It masks obvious resident-registration numbers and long numeric identifiers before posting to Discord.
§
In this environment, Hermes CLI may be installed at /opt/venv/bin/hermes instead of on PATH; install scripts should detect both.
§
insane-search is packaged as a Hermes skill and runs with `python3 -m engine <URL>` from its skill directory. Dependencies include curl_cffi, feedparser, yt-dlp, beautifulsoup4, PyYAML, lxml, and pytest.
