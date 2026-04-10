# Smart Presentations — Project Context

## What This Is
A themeable HTML presentation framework with embedded editing, comments, narration, and save. Clone the repo, pick a theme, generate a template, and use Claude skills to create and narrate presentations.

## Project Structure
- `framework.html` — Engine-only template (no theme CSS — use `generate-template` skill)
- `themes/` — Swappable theme CSS files
  - `corporate-minimal.css` — Blue/slate boardroom clean
  - `tech-dark.css` — Cyan/purple keynote energy
  - `executive-light.css` — Navy/gold light backgrounds
  - `_contract.md` — CSS variable + class contract that all themes must follow
- `presentations/` — All content decks live here
- `presentation-server.py` — Optional dev server (serves from `presentations/`)
- `.claude/skills/` — Claude skills
  - `generate-template/` — Pick a theme, build a framework template
  - `presentation/` — Create presentations (any theme)
  - `narrate-presentation/` — Generate audio narration for any presentation

## Architecture
Each presentation is a single HTML file containing:
- **Theme CSS** — brand tokens, typography, slide types, inner components (from `themes/`)
- **Engine CSS** — navigation chrome, panels, toolbar, edit mode, print styles
- Slide sections with `data-page-id` and `data-content` attributes
- `<script id="presentation-comments">` — JSON block for per-slide comments
- `<script id="presentation-content">` — JSON block for all text content (single source of truth)
- JS engine: ContentStore, ContentBinder, NavigationEngine, EditController, CommentSystem, FormPanel, FileSaver, App

**localStorage is cleared on every page load.** The embedded JSON is always authoritative.

## Getting Started
1. **Pick a theme** — choose from `themes/` or create a custom one following `themes/_contract.md`
2. **Generate template** — use the `generate-template` skill to build `[theme]-framework.html`
3. **Create presentation** — use the `presentation` skill (4-phase: Theme, Storyboard, Content, Assembly)
4. **Narrate** (optional) — use the `narrate-presentation` skill to add audio voiceover

## Theme System
- Themes are self-contained CSS files in `themes/`
- All themes use the same generic CSS custom property names (`--color-primary`, `--color-bg-dark`, etc.)
- All themes define the same class selectors (`.slide-title`, `.card`, `.green-bar`, etc.)
- HTML structure is identical across themes — only the CSS styling differs
- See `themes/_contract.md` for the full contract
- The `meta.logo` field in content JSON controls the logo mark (data-bound, not hardcoded)

## Adding a Custom Theme
1. Copy any existing theme CSS from `themes/` as a starting point
2. Follow `themes/_contract.md` for required CSS variables and class selectors
3. Update colors, fonts, gradients, and component styles
4. Add a `Fonts:` comment in the header with your Google Fonts URL
5. Save to `themes/[your-theme].css`
6. Run the `generate-template` skill to build your template

## Comment Review Workflow
The user leaves comments in the browser (Notes panel, C key) and saves the HTML file. To review:

1. **Read the comments** — look for the `<script id="presentation-comments">` block
2. **Address each comment** — each is keyed by `data-page-id` so you know which slide
3. **Update in THREE places** when changing text: the baked HTML, the content JSON, and any form textarea
4. **Clear addressed comments** — replace with `<script type="application/json" id="presentation-comments">{}</script>`

## Important Notes
- **Accent style**: Defined per-theme via `.accent` class. One accent word per heading: `<span class="accent">word</span>`
- **Active slide**: Only the first `<section>` gets `class="... active"`. Save resets to slide 1.
- **data-content completeness**: EVERY text element needs a `data-content` attribute and matching JSON entry
- **Presentation server** (`presentation-server.py`) is optional — provides instant save via POST. Files work standalone.
