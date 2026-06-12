# Recipe: Generic File Upload Workflow

Use this recipe when a website requires uploading images, PDFs, or other local files.

## Prompt

```text
Use the browser-computer-automation skill.
Find the best files from the folder I specify, prepare them for upload, upload them through the current Chrome page, verify previews, and stop before any irreversible submit.
```

## File Selection

Use local tools to inspect files first:

```bash
find "$HOME/Downloads" -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.pdf' \)
```

For images, prefer:

- high resolution
- clear subject
- strong composition
- no watermark
- no broken anatomy or obvious AI artifacts
- no tiny unreadable text

## Upload Pattern

1. Copy chosen files to a temporary upload folder.
2. Rename files with short ASCII names.
3. Open the site's upload control.
4. Select files one at a time if multi-select fails.
5. Wait for progress indicators to finish.
6. Verify rendered previews.

## Human-Controlled Gates

Stop for:

- final submit
- legal confirmation
- payment
- identity verification
- CAPTCHA or anti-bot challenge
