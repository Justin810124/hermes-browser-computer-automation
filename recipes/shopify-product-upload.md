# Recipe: Shopify Product Media Upload

Use this recipe for product creation or media updates in a logged-in Shopify admin session.

## Prompt

```text
Use the browser-computer-automation skill.
Use my real Chrome session on Shopify admin.
Upload the selected product images, fill the fields I provide, save the product as a draft, and stop before publishing or payment-related changes.
```

## Control Surface

Use real Chrome through `computer_use` for logged-in admin pages and native file pickers.

## Steps

1. Capture the Shopify admin page.
2. Verify the store/admin URL.
3. Inspect product fields and required validation.
4. Prepare upload files with short names in a temporary folder.
5. Upload files one at a time if multi-select is unreliable.
6. Wait for upload progress to finish and previews to render.
7. Save as draft when requested.

## Human-Controlled Gates

Stop for:

- publish or set active
- payment provider settings
- billing changes
- app install permissions
- irreversible inventory actions

## Notes

When selecting images, prefer clear product visibility, consistent aspect ratio, no watermarks, and no fake text artifacts.
