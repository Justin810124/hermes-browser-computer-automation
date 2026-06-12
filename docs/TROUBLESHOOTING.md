# Troubleshooting

## Hermes cannot use real Chrome

Check that the `computer_use` toolset is enabled:

```bash
hermes tools list | rg computer_use
```

If missing:

```bash
hermes tools enable computer_use
```

Then restart or reset the Hermes session.

## Chrome is visible but clicks or typing fail

Run:

```bash
/Applications/CuaDriver.app/Contents/MacOS/cua-driver doctor
```

Grant macOS permissions in System Settings -> Privacy & Security:

- Accessibility for `CuaDriver.app`
- Screen Recording for `CuaDriver.app`

Restart CuaDriver:

```bash
open -n -g -a CuaDriver --args serve
```

## Browser automation hits PerimeterX or CAPTCHA

This is expected on some logged-in or protected sites.

Correct behavior:

1. Stop automation at the challenge.
2. Ask the user to complete the challenge in real Chrome.
3. Re-capture the page after the user says it is complete.
4. Continue with ordinary UI work.

Do not try to bypass the challenge.

## File picker uploads fail

Try this pattern:

1. Copy selected files into a simple temporary folder.
2. Rename files with short ASCII names.
3. Upload one file at a time.
4. Wait for previews and progress indicators to finish.

Example:

```bash
mkdir -p /tmp/hermes-upload
cp "$HOME/Downloads/example image.png" /tmp/hermes-upload/upload-01.png
```

## Long text fields truncate content

Use smaller chunks or paste through the system clipboard if the available tool supports it.

After typing or pasting, re-capture and verify:

- field content
- character counter
- validation messages
- save button state

## The agent wants to publish, pay, or confirm legal terms

The skill should stop. The user must explicitly confirm or perform these actions:

- publish
- final submit
- payment
- subscription
- tax form
- identity verification
- legal attestation
