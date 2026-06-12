# Recipe: WordPress Post Editing

Use this recipe for editing a WordPress post or page in the user's logged-in browser.

## Prompt

```text
Use the browser-computer-automation skill.
Use my real Chrome session in WordPress.
Edit the post content I provide, upload media if needed, save draft, and stop before publishing.
```

## Control Surface

Use browser tools for public pages. Use real Chrome through `computer_use` for logged-in admin editing and media upload dialogs.

## Steps

1. Capture the current WordPress editor page.
2. Identify whether the editor is Gutenberg, Classic Editor, or a page builder.
3. Edit one content block at a time.
4. Upload media through the media library or native picker.
5. Preview if requested.
6. Save draft.

## Human-Controlled Gates

Stop for:

- publish/update live page if user has not explicitly confirmed
- plugin installation
- theme changes
- user or permission changes
- payment or domain settings

## Notes

For page builders, use visual captures more often because many controls are custom and may not expose useful accessibility labels.
