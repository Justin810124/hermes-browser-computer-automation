# Demo Script

Use this script to record a real 45-60 second demo GIF or video.

## Goal

Show that the skill helps Hermes choose the right control surface for real browser work:

- browser tools for ordinary pages
- real Chrome for logged-in workflows
- native UI control for file uploads
- human pause for verification gates

Do not show private account data, credentials, tokens, payment details, tax details, or identity documents.

## Suggested Recording

### Scene 1: Setup, 5 seconds

Show the repository README and Quick Start:

```bash
bash scripts/install.sh
bash scripts/doctor.sh
```

Narration:

```text
This skill teaches Hermes how to handle real Chrome workflows safely.
```

### Scene 2: Real Chrome capture, 15 seconds

Open a harmless demo form or draft page in Chrome. Ask Hermes:

```text
Use the browser-computer-automation skill.
Use my real Chrome session.
Fill this draft form and save it, but stop before any final submit.
```

Show:

- page capture
- field identification
- text entry
- save draft

Narration:

```text
For logged-in workflows, Hermes uses the user's real Chrome session instead of a fresh automation profile.
```

### Scene 3: Upload, 15 seconds

Use a local folder with sample images. Show Hermes preparing short upload names and using the native picker.

Narration:

```text
For native file pickers, the skill switches to macOS UI control and verifies previews after upload.
```

### Scene 4: Human verification boundary, 10 seconds

Show a mock verification gate, not a real private challenge. The agent should stop and ask for user action.

Narration:

```text
CAPTCHA, PerimeterX, 2FA, identity, tax, payment, and publish gates stay human-controlled.
```

### Scene 5: Close, 5 seconds

Show the GitHub repo URL and open issues.

Narration:

```text
The project is open source and ready for workflow recipes, platform notes, and reliability improvements.
```

## Demo Checklist

- No credentials or private data visible.
- No anti-bot bypass claims.
- No final publish, payment, tax, or identity action.
- Shows `doctor.sh` passing.
- Shows real Chrome or clearly labels any mock page as a demo page.
- Ends with the repository URL.
