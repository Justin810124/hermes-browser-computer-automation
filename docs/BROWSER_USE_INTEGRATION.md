# Browser Use Integration

This project now treats Browser Use as the optional high-skill web automation engine.

Use it for ordinary browser tasks where a self-healing browser agent is better than raw click/type loops. Use Hermes `computer_use` or CuaDriver when the task depends on the user's current visible Chrome window, native macOS UI, or a human-verification handoff.

## Install

```bash
bash scripts/install_browser_use.sh
```

Create `.env` from `.env.example` and add one API key.

Browser Use Cloud:

```bash
BROWSER_USE_API_KEY=...
```

OpenAI:

```bash
OPENAI_API_KEY=...
HERMES_BROWSER_USE_LLM=openai
HERMES_BROWSER_USE_MODEL=gpt-4.1-mini
```

## Run A Safe Dry Run

First ask the operator to choose a route:

```bash
scripts/hermes_operator.py --task "Open example.com and summarize the page"
```

```bash
.venv-browser-use/bin/python scripts/run_browser_use_task.py \
  --dry-run \
  --task "Open example.com and summarize the page"
```

## Run An Ordinary Web Task

```bash
.venv-browser-use/bin/python scripts/run_browser_use_task.py \
  --task "Visit https://duckduckgo.com and search for browser-use founders"
```

## Use Existing Chrome Login State

Browser Use documents `Browser.from_system_chrome()` for connecting to an existing Chrome profile so cookies and logins are available.

```bash
.venv-browser-use/bin/python scripts/run_browser_use_task.py \
  --real-chrome \
  --profile "Default" \
  --task "Open my logged-in dashboard and report the visible draft status. Stop before publishing or submitting anything."
```

You may need to fully close Chrome first, depending on the browser profile state.

## Routing Rule

Use this order:

1. Purpose-built API or connector, if available.
2. Browser Use for ordinary web tasks.
3. Browser Use with real Chrome profile for authenticated web tasks that do not require native UI handoff.
4. Hermes `computer_use` or CuaDriver for the user's current Chrome window, native file pickers, visual UI, and live handoff.
5. Stop for CAPTCHA, PerimeterX, Cloudflare Turnstile, 2FA, identity, tax, payment, publish, or legal attestation.

## Why This Helps Hermes

Hermes already has `browser`, `computer_use`, `vision`, `terminal`, and CuaDriver available on your machine. The weak point is choosing and sequencing them well.

Browser Use adds a mature browser-agent loop for common web tasks. This project adds:

- a safety wrapper
- a runner Hermes can call from terminal
- a skill-level decision contract
- docs for when to switch back to real desktop control

## Sources

- Browser Use quickstart: https://docs.browser-use.com/open-source/quickstart
- Browser Use real browser docs: https://docs.browser-use.com/open-source/customize/browser/real-browser
- Browser Use GitHub: https://github.com/browser-use/browser-use
