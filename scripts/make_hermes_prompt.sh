#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -eq 0 ]; then
  echo "Usage: scripts/make_hermes_prompt.sh \"your task\""
  exit 1
fi

TASK="$*"

cat <<EOF
Use the browser-computer-automation skill.

Before acting, output:
1. Control surface decision:
   - API/connector
   - Browser Use
   - Browser Use with real Chrome profile
   - Hermes browser tools
   - computer_use/CuaDriver on real Chrome
   - stop for human verification
2. Why that surface is correct.
3. What gates you will stop for.

Task:
$TASK

If Browser Use is appropriate, prefer:
.venv-browser-use/bin/python scripts/run_browser_use_task.py --task "$TASK"

If the task needs my current logged-in Chrome window, native file picker, desktop UI, or a verification handoff, use computer_use/CuaDriver instead.

Never bypass CAPTCHA, PerimeterX, Cloudflare Turnstile, 2FA, identity, tax, payment, publish, or legal attestation gates. Stop and ask me to complete or confirm those steps.
EOF
