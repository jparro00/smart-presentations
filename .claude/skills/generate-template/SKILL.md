# Generate Template Skill

Generate a presentation template from the framework engine + a chosen theme. Use this skill when the user wants to: set up a new template, pick a theme, generate a framework, configure the presentation style, create a themed template, initialize the presentation system.

## Prerequisites

- `framework.html` must exist in the project root (the engine-only template)
- Theme CSS files must exist in `themes/` directory

---

## Workflow

### Step 1 — Choose a Theme

If the user hasn't specified a theme, present the available options from `themes/`. The built-in themes are:

| Theme | File | Description |
|-------|------|-------------|
| `corporate-minimal` | `themes/corporate-minimal.css` | Blue accents on dark slate. Clean, authoritative, boardroom-ready. Inter + Playfair Display. |
| `tech-dark` | `themes/tech-dark.css` | Cyan/purple on true dark. Monospace accents, keynote energy. Inter + JetBrains Mono. |
| `executive-light` | `themes/executive-light.css` | Light backgrounds, navy/gold. Serif headings, printed-report feel. Merriweather + Source Sans 3. |
| `custom` | User provides a CSS file path | Must follow the contract in `themes/_contract.md`. |

Additional themes may exist in the `themes/` directory — check for any `.css` files and list them.

### Step 2 — Read the Framework and Theme

1. Read `framework.html` from the project root
2. Read the chosen theme CSS file from `themes/[name].css` (or custom path)
3. Extract the Google Fonts URL from the theme CSS header comment:
   - Parse the line matching `Fonts: [URL]` in the opening comment block

### Step 3 — Inject Theme into Framework

Make these replacements in the framework HTML:

1. **Replace `<!-- THEME FONTS -->`** with:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link href="[extracted-fonts-url]" rel="stylesheet">
   ```

2. **Replace `<!-- THEME CSS -->`** with the full contents of the theme CSS file.

3. **Update `<title>`** to include the theme name:
   ```html
   <title>[Theme Name] Presentation Template</title>
   ```

4. **Set defaults in the content JSON meta block:**
   ```json
   "logo": "Your Company",
   "confidential": "CONFIDENTIAL"
   ```

   If the theme has a brand-specific config (e.g., a companion brand skill), follow that skill's guidance for logo and confidential values instead.

### Step 4 — Write the Output File

Write the assembled HTML to the project root as the template file:
- Default: `[theme-name]-framework.html` (e.g., `corporate-minimal-framework.html`)
- Or a user-specified filename

### Step 5 — Confirm

Report to the user:
- Which theme was applied
- The output file path
- Remind them to use the `presentation` skill to create decks from this template
- Remind them the template uses the same slide types and HTML structure as all other themes

---

## Custom Theme Guide

If the user wants to create their own theme:

1. Copy any existing theme CSS from `themes/` as a starting point
2. Read `themes/_contract.md` for the full list of required CSS variables and class selectors
3. Update the `:root` block with their brand colors, fonts, and spacing
4. Update all class selectors with their visual styling
5. Update the `Fonts:` comment in the header with their Google Fonts URL
6. Save to `themes/[name].css`
7. Run this skill with `theme=custom` and provide the CSS file path

---

## Quick Reference

| Input | Output |
|-------|--------|
| `framework.html` + `themes/[name].css` | `[name]-framework.html` |
| `framework.html` + custom CSS | `[custom-name]-framework.html` |
