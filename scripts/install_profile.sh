#!/usr/bin/env bash
set -euo pipefail

PROFILE_NAME="${1:-sbbagi}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if command -v hermes >/dev/null 2>&1; then
  HERMES_BIN="$(command -v hermes)"
elif [ -x /opt/venv/bin/hermes ]; then
  HERMES_BIN="/opt/venv/bin/hermes"
else
  echo "Hermes CLI not found. Install first: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash" >&2
  exit 1
fi

HERMES_HOME_DIR="${HERMES_HOME:-$HOME/.hermes}"
PROFILE_DIR="$HERMES_HOME_DIR/profiles/$PROFILE_NAME"
mkdir -p "$PROFILE_DIR"

copy_dir() {
  local src="$1" dst="$2"
  if [ -d "$src" ]; then
    mkdir -p "$dst"
    cp -R "$src"/. "$dst"/
  fi
}

copy_dir "$REPO_ROOT/profiles/sbbagi" "$PROFILE_DIR"
chmod 700 "$PROFILE_DIR/scripts/gmail_spec_watchdog.py" 2>/dev/null || true

BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"
cat > "$BIN_DIR/sbbagi" <<EOF
#!/bin/sh
exec "$HERMES_BIN" -p "$PROFILE_NAME" "\$@"
EOF
chmod +x "$BIN_DIR/sbbagi"

# Backward-compatible wrapper for the earlier romanization.
cat > "$BIN_DIR/spakki" <<EOF
#!/bin/sh
exec "$HERMES_BIN" -p "$PROFILE_NAME" "\$@"
EOF
chmod +x "$BIN_DIR/spakki"

# Backward-compatible typo wrapper from the original preserved artifact.
cat > "$BIN_DIR/spbaki" <<EOF
#!/bin/sh
exec "$HERMES_BIN" -p "$PROFILE_NAME" "\$@"
EOF
chmod +x "$BIN_DIR/spbaki"

echo "Installed 스빡이 profile to: $PROFILE_DIR"
echo "Wrappers: $BIN_DIR/sbbagi, $BIN_DIR/spakki, and $BIN_DIR/spbaki"
echo
echo "Next steps on this machine:"
echo "1) Configure model/OAuth credentials: $HERMES_BIN -p $PROFILE_NAME setup"
echo "2) Configure Discord gateway if needed: $HERMES_BIN -p $PROFILE_NAME gateway setup"
echo "3) For Gmail watchdog, set up Google OAuth token at: $PROFILE_DIR/google_token.json"
echo "4) Create cron after Gmail works:"
echo "   $HERMES_BIN -p $PROFILE_NAME cron create 'every 5m' --script gmail_spec_watchdog.py --no-agent --deliver origin"
