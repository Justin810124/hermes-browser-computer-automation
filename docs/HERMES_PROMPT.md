# Hermes Prompt

Use this prompt when you want Hermes to behave more like a careful browser/computer operator.

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
