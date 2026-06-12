# Launch Plan

## Project Name

Recommended repo name:

```text
hermes-browser-computer-automation
```

Short description:

```text
User-in-the-loop Chrome and macOS automation skill for Hermes Agent.
```

GitHub topics:

```text
hermes-agent, browser-automation, computer-use, chrome-automation, macos, cuadriver, ai-agent, gui-automation, skills
```

## One-Line Pitch

Give Hermes Agent the missing playbook for logged-in Chrome sessions, native macOS UI, file uploads, and human verification boundaries.

## Why People May Star It

- Many agent demos fail on real logged-in websites.
- File upload dialogs and custom dashboards are still hard for agents.
- Anti-bot systems break headless browser workflows.
- Most automation projects do not clearly define a safe human-verification boundary.
- This repo is small, installable, and easy to adapt.

## Safe Positioning

Avoid:

- "bypass PerimeterX"
- "solve CAPTCHA"
- "stealth browser"
- "undetectable automation"
- "botting"

Use:

- "user-in-the-loop"
- "real Chrome session"
- "desktop co-pilot"
- "safe automation boundaries"
- "stop at verification gates"
- "logged-in workflow assistance"

## Launch Checklist

1. Create a public GitHub repository.
2. Push the current folder as the initial version.
3. Add a clear demo GIF or short screen recording.
4. Add three practical recipes:
   - Fiverr seller profile draft
   - Shopify product media upload
   - WordPress post editing
5. Open 5-10 good first issues before announcing.
6. Publish a short post explaining the problem:
   - "Why agents fail on real browser tasks"
   - "When to use browser tools vs real Chrome"
   - "Why CAPTCHA is a human boundary, not an automation target"
7. Share with Hermes users, AI agent builders, and browser automation communities.

## Version Roadmap

### v0.1

- Skill file
- Installer
- Validation script
- Safety policy
- CuaDriver MCP instructions

### v0.2

- Workflow recipes
- Example prompts
- Demo screenshots
- Troubleshooting guide

### v0.3

- Cross-platform notes for Windows and Linux
- Integration examples for other local agents
- Reliability checklist for form filling and uploads

### v1.0

- Stable skill schema
- Tested workflow library
- Community-maintained docs
- Compatibility matrix for Hermes versions and toolsets

## Suggested README Badges

Add these after the repo exists:

```markdown
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![Safety](https://img.shields.io/badge/safety-user--in--the--loop-blue)
```

## Maintainer Rules

- Reject issues or PRs that attempt to bypass CAPTCHA, PerimeterX, 2FA, payment, tax, identity, or legal verification.
- Keep examples practical and truthful.
- Prefer small workflow recipes over giant abstractions.
- Require docs updates for behavior changes.
- Keep the core skill readable enough for users to audit.
