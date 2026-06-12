# Operator Harness

`scripts/hermes_operator.py` is the project guardrail that makes Hermes act less like a naive clicker.

Hermes should run it before browser actions:

```bash
scripts/hermes_operator.py --task "Use my current Chrome window to fill this form and stop before publish"
```

It returns:

- `Control surface`
- `Reason`
- `Stop gates`
- `Next command`
- `Handoff`
- `Warnings`

## Modes

Auto route:

```bash
scripts/hermes_operator.py --task "Open example.com and report the title"
```

Force Browser Use:

```bash
scripts/hermes_operator.py --mode browser-use --task "Open example.com"
```

Force real Chrome profile:

```bash
scripts/hermes_operator.py --mode browser-use-real-chrome --task "Open my dashboard"
```

Force desktop control:

```bash
scripts/hermes_operator.py --mode computer_use/CuaDriver --task "Use my current Chrome tab"
```

JSON for programmatic agents:

```bash
scripts/hermes_operator.py --json --task "Upload files from Downloads"
```

## Evaluation

Run:

```bash
python3 scripts/test_operator.py
```

The cases live in `tests/operator_cases.json`.

## Why This Exists

Skills are advisory. Hermes may still choose the wrong tool. The operator harness turns the advisory guidance into a concrete preflight command with explicit routing and warnings.
