# Recipe: Fiverr Seller Profile Draft

Use this recipe for drafting or editing a Fiverr seller profile in the user's real Chrome session.

## Prompt

```text
Use the browser-computer-automation skill.
Use my real Chrome session on Fiverr.
Help draft or edit the seller profile sections I specify.
Save drafts when available.
Stop for CAPTCHA, PerimeterX, identity, tax, payment, or publish.
```

## Control Surface

Prefer real Chrome through `computer_use` because Fiverr may depend on existing login state and may show anti-bot challenges in automation browsers.

## Steps

1. Capture the current Chrome page.
2. Confirm the visible Fiverr URL and current onboarding or gig-editing step.
3. Fill one section at a time.
4. Respect character counters and validation messages.
5. Save or continue only when the button is clearly part of draft progress.
6. Stop before final publish or legal/tax/identity screens.

## Human-Controlled Gates

Stop for:

- PerimeterX
- CAPTCHA
- phone or device verification
- identity verification
- tax forms
- payment setup
- final publish

## Notes

Keep profile claims truthful. Do not invent work history, degrees, certifications, legal identity, or tax information.
