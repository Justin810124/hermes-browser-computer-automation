# Recipe: Hermes Browser Use Routing

Use this recipe when Hermes is acting like a simple web clicker and you want it to choose the right engine first.

## Prompt

```text
Use the browser-computer-automation skill.
Before acting, output the control-surface decision.

Task: <your task>
```

## Expected Decision

For ordinary public web tasks:

```text
Control surface: Browser Use
Reason: This is an ordinary web workflow and does not need my current desktop UI.
```

For logged-in tasks that can use a Chrome profile:

```text
Control surface: Browser Use real Chrome
Reason: This needs authenticated state but not native macOS handoff.
```

For current visible Chrome, uploads, CAPTCHA, or desktop UI:

```text
Control surface: computer_use/CuaDriver
Reason: This needs the user's current visible Chrome session or native UI.
```

## Commands

Dry run:

```bash
.venv-browser-use/bin/python scripts/run_browser_use_task.py --dry-run --task "<task>"
```

Ordinary web task:

```bash
.venv-browser-use/bin/python scripts/run_browser_use_task.py --task "<task>"
```

Existing Chrome profile:

```bash
.venv-browser-use/bin/python scripts/run_browser_use_task.py --real-chrome --profile "Default" --task "<task>"
```

## Stop Gates

Stop for CAPTCHA, PerimeterX, Cloudflare Turnstile, 2FA, identity, tax, payment, publish, or legal attestation.
