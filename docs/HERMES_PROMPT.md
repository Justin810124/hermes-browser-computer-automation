# Hermes Prompt

Use this prompt when you want Hermes to behave more like a careful browser/computer operator.

## Best Version

```text
Use the browser-computer-automation skill.
Before opening, clicking, typing, or navigating anything, run:

scripts/hermes_operator.py --task "<my task>"

Follow the operator's Control surface, Next command, Handoff, and Warnings exactly.
If it says computer_use/CuaDriver, do not use browser_navigate.
If it says Browser Use, run the provided command.
If it says stop, ask me to handle or confirm the gate.
```

```text
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

If Browser Use is appropriate, prefer:
.venv-browser-use/bin/python scripts/run_browser_use_task.py --task "<task>"

If the task needs my current logged-in Chrome window, native file picker, desktop UI, or a verification handoff, use computer_use/CuaDriver instead.

Never bypass CAPTCHA, PerimeterX, Cloudflare Turnstile, 2FA, identity, tax, payment, publish, or legal attestation gates. Stop and ask me to complete or confirm those steps.
```

## Short Version

```text
Use browser-computer-automation. First choose the control surface. Use Browser Use for ordinary web tasks, real Chrome/computer_use for logged-in desktop workflows, and stop for verification/payment/publish gates.
```

## Generate A Prompt

```bash
scripts/make_hermes_prompt.sh "Use my real Chrome session to fill this form and stop before publish"
```
