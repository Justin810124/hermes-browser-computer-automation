#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$HOME/.hermes/skills/productivity/browser-computer-automation"

mkdir -p "$DEST"
cp "$ROOT/skills/productivity/browser-computer-automation/SKILL.md" "$DEST/SKILL.md"

echo "Installed browser-computer-automation skill to:"
echo "  $DEST/SKILL.md"
echo
echo "Restart or reset Hermes so the skill is reloaded."

