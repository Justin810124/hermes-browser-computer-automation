# Launch Campaign

This is the recommended first launch sequence for the project.

## Launch Goal

Get early feedback from people building local agents, browser automation tools, and desktop computer-use workflows.

Do not optimize the first wave for mass traffic. Optimize for:

- useful stars
- real user feedback
- workflow recipe contributions
- compatibility reports
- demo improvements

## Core Message

```text
AI browser demos often work on clean pages but fail on real logged-in workflows.

This Hermes skill teaches the agent when to use browser tools, when to use the user's real Chrome session, when to use macOS UI control, and when to stop for human verification.
```

## Links

- Repo: https://github.com/Justin810124/hermes-browser-computer-automation
- Release: https://github.com/Justin810124/hermes-browser-computer-automation/releases/tag/v0.2.0
- Real Chrome demo GIF: https://github.com/Justin810124/hermes-browser-computer-automation/blob/main/assets/demo-real.gif
- Demo script: https://github.com/Justin810124/hermes-browser-computer-automation/blob/main/docs/DEMO_SCRIPT.md
- Good first issues: https://github.com/Justin810124/hermes-browser-computer-automation/issues

## First 72 Hours

### Hour 0: GitHub Polish

- Confirm README loads with real Chrome GIF.
- Confirm open issues are clear.
- Confirm release notes are readable.
- Add social preview image if GitHub settings permit it.

### Hour 1: X / Twitter

Post the short launch copy from `docs/PROMOTION_COPY.md`.

Follow-up reply:

```text
The interesting part is the boundary:

- browser tools for ordinary pages
- real Chrome for logged-in workflows
- macOS UI for native file pickers
- stop at CAPTCHA, PerimeterX, 2FA, identity, tax, payment, or publish

Repo: https://github.com/Justin810124/hermes-browser-computer-automation
```

### Hour 3: Relevant Communities

Share as a technical note, not a drive-by link.

Good framing:

```text
I ran into a practical issue while trying to make a local agent handle real browser work: headless automation is often the wrong surface for logged-in workflows.

I turned the pattern into a Hermes skill and would love feedback from people working on local agents or browser automation.
```

### Hour 8-24: Show HN

Use:

```text
Show HN: Hermes skill for real Chrome and macOS computer automation
```

Ask for feedback, not stars.

### Day 2: Follow Up With Learnings

Post a short update:

```text
Early feedback so far:
- people care about logged-in Chrome sessions
- native file pickers are still painful for agents
- the human-verification boundary needs to be explicit

Next: longer real workflow demo and cross-platform notes.
```

### Day 3: Convert Feedback Into Issues

For every useful comment:

- open an issue
- label it
- thank the commenter
- link the issue in a reply

## Launch Posts

### X / Twitter

```text
I open-sourced a Hermes Agent skill for real Chrome + macOS computer automation.

It helps agents handle logged-in workflows, form filling, uploads, and native UI while stopping at CAPTCHA/2FA/payment/identity gates.

Not stealth. Not bypass. User-in-the-loop desktop automation.

Real Chrome demo in the README:
https://github.com/Justin810124/hermes-browser-computer-automation
```

### Show HN

Title:

```text
Show HN: Hermes skill for real Chrome and macOS computer automation
```

Text:

```text
I built a small Hermes Agent skill after running into a practical local-agent problem: browser automation often works on clean demo pages but breaks on real logged-in workflows.

Examples: seller dashboards, file upload dialogs, custom React controls, and anti-bot screens.

The skill defines a simple decision tree:
- use browser tools for ordinary pages
- use real Chrome through computer_use when the task needs the user's logged-in session
- use CuaDriver/macOS UI control for native dialogs
- stop for CAPTCHA, PerimeterX, 2FA, identity, tax, payment, or publish gates

It is intentionally not a CAPTCHA or anti-bot bypass project. It is a user-in-the-loop automation playbook for real desktop workflows.

The README includes a real Chrome demo GIF and the repo includes a local demo page so contributors can reproduce or improve the demo.

Repo: https://github.com/Justin810124/hermes-browser-computer-automation
```

### Reddit / Discord

```text
I made a small open-source Hermes skill after running into a practical agent problem: headless browser automation often fails on real logged-in workflows.

This skill is a playbook for choosing browser tools vs real Chrome vs macOS UI control, with a hard stop at verification gates like CAPTCHA, PerimeterX, 2FA, payment, tax, identity, and publish.

It includes a real Chrome demo GIF, a reproducible local demo page, and starter workflow recipes.

Would love feedback from people building local agents or desktop automation workflows:
https://github.com/Justin810124/hermes-browser-computer-automation
```

## What Not To Say

Avoid:

- "bypass PerimeterX"
- "solve CAPTCHA"
- "undetectable"
- "stealth automation"
- "botting"
- "growth hack"

Use:

- "human verification boundary"
- "user-in-the-loop"
- "real Chrome session"
- "logged-in workflow assistance"
- "desktop co-pilot"

## Success Metrics

First 72 hours:

- 20 meaningful stars
- 3 issues from other people
- 1 external workflow suggestion
- 1 compatibility report

First 2 weeks:

- 100 stars
- 10 issues
- 3 recipe contributions
- 1 longer narrated demo video
