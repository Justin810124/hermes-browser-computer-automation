# Promotion Copy

Use these as starting points. Edit them to match the community and avoid spammy posting.

## Hacker News Show HN

Title:

```text
Show HN: Hermes skill for real Chrome and macOS computer automation
```

Post:

```text
I built a small Hermes Agent skill that teaches the agent how to choose between browser automation, the user's real Chrome session, and macOS computer-use tools.

The problem: a lot of agent browser demos work on clean pages but break on real logged-in workflows: seller dashboards, file upload dialogs, custom React controls, and anti-bot screens.

The skill defines a simple decision tree:
- use browser tools for ordinary pages
- use real Chrome through computer_use when the task needs the user's logged-in session
- use CuaDriver/macOS UI control for native dialogs
- stop for CAPTCHA, PerimeterX, 2FA, identity, tax, payment, or publish gates

It is intentionally not a CAPTCHA or anti-bot bypass project. It is a user-in-the-loop automation playbook for real desktop workflows.

The README includes a real Chrome demo GIF plus a recording script for a longer walkthrough.

Repo: https://github.com/Justin810124/hermes-browser-computer-automation
```

## X / Twitter

```text
I open-sourced a Hermes Agent skill for real Chrome + macOS computer automation.

It helps agents handle logged-in workflows, form filling, uploads, and native UI while stopping at CAPTCHA/2FA/payment/identity gates.

Not stealth. Not bypass. User-in-the-loop desktop automation.

Real Chrome demo in the README:
https://github.com/Justin810124/hermes-browser-computer-automation
```

## Product Hunt

Name:

```text
Hermes Browser Computer Automation
```

Tagline:

```text
User-in-the-loop Chrome and macOS automation for Hermes Agent
```

Description:

```text
A practical Hermes Agent skill for real logged-in browser workflows. It teaches Hermes when to use browser tools, when to use the user's real Chrome session, when to use macOS UI control, and when to stop for human verification such as CAPTCHA, PerimeterX, 2FA, identity, tax, payment, or publish gates.
```

## Reddit / Discord

```text
I made a small open-source Hermes skill after running into a practical agent problem: headless browser automation often fails on real logged-in workflows.

This skill is a playbook for choosing browser tools vs real Chrome vs macOS UI control, with a hard stop at verification gates like CAPTCHA, PerimeterX, 2FA, payment, tax, identity, and publish.

Would love feedback from people building local agents or desktop automation workflows:
https://github.com/Justin810124/hermes-browser-computer-automation
```

## Blog Post Outline

Title:

```text
Why AI Agents Fail on Real Browser Tasks
```

Outline:

1. Clean browser demos are not the real world.
2. Logged-in workflows need the user's actual Chrome session.
3. Native file pickers are outside normal DOM automation.
4. Anti-bot challenges are human boundaries, not automation targets.
5. A safer decision tree: browser tools, real Chrome, native UI, stop gates.
6. Example: seller profile setup with uploads.
7. Open-source repo and roadmap.
