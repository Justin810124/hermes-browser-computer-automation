#!/usr/bin/env bash
set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_SRC="$ROOT/skills/productivity/browser-computer-automation/SKILL.md"
SKILL_DEST="$HOME/.hermes/skills/productivity/browser-computer-automation/SKILL.md"
CUADRIVER="/Applications/CuaDriver.app/Contents/MacOS/cua-driver"

pass() { printf "PASS  %s\n" "$1"; }
warn() { printf "WARN  %s\n" "$1"; }
fail() { printf "FAIL  %s\n" "$1"; }

overall=0

printf "Hermes Browser Computer Automation doctor\n"
printf "=========================================\n\n"

if command -v hermes >/dev/null 2>&1; then
  pass "Hermes CLI found: $(command -v hermes)"
else
  fail "Hermes CLI not found in PATH"
  overall=1
fi

if [ -f "$SKILL_SRC" ]; then
  pass "Repository skill found"
else
  fail "Repository skill missing: $SKILL_SRC"
  overall=1
fi

if [ -f "$SKILL_DEST" ]; then
  pass "Installed skill found: $SKILL_DEST"
else
  warn "Installed skill not found. Run: bash scripts/install.sh"
fi

if command -v hermes >/dev/null 2>&1; then
  printf "\nHermes toolsets\n"
  printf "%s\n" "---------------"
  tools_output="$(hermes tools list 2>/dev/null || true)"
  for tool in browser computer_use vision terminal file skills; do
    if printf "%s\n" "$tools_output" | grep -q "$tool"; then
      pass "$tool appears in hermes tools list"
    else
      warn "$tool not found in hermes tools list"
    fi
  done
fi

printf "\nBrowser Use optional engine\n"
printf "%s\n" "---------------------------"
if command -v uv >/dev/null 2>&1; then
  pass "uv found: $(command -v uv)"
else
  warn "uv not found. Install uv before using Browser Use integration."
fi

if [ -x "$ROOT/.venv-browser-use/bin/python" ]; then
  if "$ROOT/.venv-browser-use/bin/python" - <<'PY' >/tmp/hermes-browser-use-check.out 2>/tmp/hermes-browser-use-check.err
import browser_use
print(getattr(browser_use, "__version__", "unknown"))
PY
  then
    pass "browser_use import works in .venv-browser-use: $(cat /tmp/hermes-browser-use-check.out)"
  else
    warn "browser_use is not importable in .venv-browser-use. Run: bash scripts/install_browser_use.sh"
  fi
else
  warn ".venv-browser-use not found. Run: bash scripts/install_browser_use.sh for Browser Use engine."
fi

if [ -f "$ROOT/.env" ]; then
  pass ".env file found"
else
  warn ".env not found. Browser Use needs an API key such as BROWSER_USE_API_KEY or OPENAI_API_KEY."
fi

printf "\nCuaDriver\n"
printf "%s\n" "---------"
if [ -x "$CUADRIVER" ]; then
  pass "CuaDriver found"
  "$CUADRIVER" doctor || {
    warn "CuaDriver doctor reported a problem. Check Accessibility and Screen Recording permissions."
    overall=1
  }
else
  warn "CuaDriver not found at $CUADRIVER"
fi

printf "\nValidation\n"
printf "%s\n" "----------"
if "$ROOT/scripts/validate_skill.py"; then
  pass "Skill validation passed"
else
  fail "Skill validation failed"
  overall=1
fi

exit "$overall"
