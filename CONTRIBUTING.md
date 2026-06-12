# Contributing

Contributions are welcome if they improve safe, user-in-the-loop browser and desktop automation for Hermes Agent.

Good contributions:

- clearer workflows for real Chrome automation
- better CuaDriver setup instructions
- safer file upload playbooks
- examples for common dashboards
- troubleshooting notes for macOS permissions
- tests or scripts that validate `SKILL.md` formatting

Please do not contribute:

- CAPTCHA or PerimeterX bypass instructions
- stealth browser evasion
- credential extraction
- payment automation
- spam/account-abuse workflows

## Development

Validate the skill file:

```bash
python3 scripts/validate_skill.py
```

Install locally:

```bash
bash scripts/install.sh
```

Restart or reset Hermes after installing.

