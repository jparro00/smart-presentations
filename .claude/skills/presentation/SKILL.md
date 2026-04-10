# HTML Presentation Skill

Build professional HTML presentations using the framework template with any theme. This skill enforces a 4-phase workflow: **Theme → Storyboard → Content → Assembly**.

Use this skill when the user wants to: create a presentation, build a slide deck, make slides, create a briefing, turn content into slides, assemble a presentation from notes, or produce a themed HTML deck. Also trigger when the user says "presentation", "slide deck", "slides", or "briefing" in the context of creating deliverables.

## Prerequisites

- A framework template must exist. Either:
  - `[theme]-framework.html` in the project root (pre-generated via `generate-template` skill), OR
  - `framework.html` + a theme CSS file in `themes/` (will be assembled inline)
- Read the reference file at `.claude/skills/presentation/references/slide-examples.md` for exact HTML snippets of each slide type

---

## PHASE 0: THEME SELECTION

Before anything else, determine which theme to use.

### If the user specified a theme (e.g., "make a tech-dark presentation"):
Use that theme. Skip the prompt.

### If the user specified a brand with a matching theme + brand skill:
Use the matching theme. If a companion brand skill exists for that theme, invoke it for voice guidelines.

### Otherwise, ask:
List the available themes from `themes/*.css` and present them. The built-in themes are:

| Theme | Description |
|-------|-------------|
| `corporate-minimal` | Blue accents on dark slate. Clean, authoritative, boardroom-ready. |
| `tech-dark` | Cyan/purple on true dark. Monospace accents, keynote energy. |
| `executive-light` | Light backgrounds, navy/gold. Serif headings, printed-report feel. |

Additional themes may exist in `themes/` — check and list any `.css` files found.

### Locate the template:
1. Check if `[theme]-framework.html` exists in the project root
2. If not, check if `framework.html` and `themes/[theme].css` exist
3. If neither, tell the user to run the `generate-template` skill first

---

## PHASE 1: STORYBOARD

Before writing any code, have a conversation to establish the deck structure.

### Step 1 — Gather Context
Ask the user (if not already provided):
- **Audience**: Who is this for? (e.g., leadership, client, internal team)
- **Purpose**: What decision or action should this drive?
- **Tone**: Executive briefing? Workshop? Pitch? Training?
- **Key message**: What is the single takeaway?
- **Length**: How many slides? (Default: 8-14 for a briefing, 15-25 for a deep dive)

### Step 2 — Propose Slide Outline
Present a numbered outline where each slide has:

```
Slide N: [page-id] — [Slide Type]
  → One-line description of content/purpose
```

### Design Diversity Rules
When proposing the outline, ensure variety:
- **Never** use the same slide type more than 3 times consecutively
- **Alternate** between background classes (`bg-dark`, `bg-darker`, `bg-black`)
- Use **at least 3 different** slide types in any deck
- Place a `slide-divider` every 3-5 content slides to create narrative rhythm
- Mix column layouts: some full-width, some two-col, some card grids
- Vary accent variants: alternate default and `.blue` footer bars, card accent rules, highlight boxes
- Use `slide-callout` for pivotal moments — maximum 2 per deck
- Use `slide-stats` when you have quantitative evidence — maximum 2 per deck
- End section with a `slide-numbered-list` for action items / "the ask"

### Step 3 — Get Approval
Present the outline. Wait for user to approve or modify before proceeding.

---

## PHASE 2: CONTENT DRAFT

For each slide in the approved outline, draft the actual text content.

### Content Format
Present content as a structured block per slide:

```
## Slide N: [page-id] ([slide-type])

- label: "SECTION LABEL"
- heading: "Main heading with one <accent> word"
- body: "Body text paragraph..."
- [additional fields depending on slide type]
```

### Writing Rules
1. **One accent word per heading** — wrap in `<span class="accent">` (renders in the theme's primary accent style)
2. **Lead with insight, not description** — "The old moats are gone" not "Industry changes overview"
3. **Keep body text to 2-3 sentences max** — one idea per slide
4. **Use strong verbs** — "Ship", "Build", "Cut" not "Consider", "Explore", "Evaluate"
5. **Attribute claims** — "(Gartner, 2025)", "(est.)" for projections
6. **No jargon** — translate technical concepts into business impact
7. **Card titles**: 2-4 words. Card bodies: 1-2 sentences.
8. **Stat numbers**: use short formats — "47%", "3.2x", "$12M", "10k+"

### Content Fields by Slide Type

**slide-title**: heading, subtitle
**slide-divider**: label, heading
**slide-content**: label, heading, body (+ col-left/col-right for two-col layouts)
**slide-callout**: label, statement
**slide-stats**: label, heading, stat-N-number, stat-N-label (N=1,2,3,4)
**slide-numbered-list**: label, heading, action-N-title, action-N-desc
**slide-comparison**: label, heading, col-left-heading, col-right-heading, + list items
**slide-timeline**: label, heading, node-N-title, node-N-desc
**slide-end**: brand, tagline, copyright

### Step 4 — Get Content Approval
Present all slide content. Wait for user review. Iterate as needed.

---

## PHASE 3: ASSEMBLY

Once content is approved, build the presentation.

### Step 5 — Create the File
1. Copy the theme's framework template to a new file: `presentations/[presentation-name].html`
   - If `[theme]-framework.html` exists, copy that
   - Otherwise, read `framework.html`, read `themes/[theme].css`, extract the Fonts URL from the CSS header comment, replace `<!-- THEME FONTS -->` with the Google Fonts link, replace `<!-- THEME CSS -->` with the full CSS file contents, and write the assembled file
2. Read the reference file at `.claude/skills/presentation/references/slide-examples.md` for exact HTML snippets of each slide type

### Step 6 — Build Content JSON
Replace the `<script id="presentation-content">` block with the final content JSON.
Also ensure the comments block exists: `<script type="application/json" id="presentation-comments">{}</script>` — this must appear BEFORE the content script.

```json
{
  "meta": {
    "title": "Presentation Title",
    "confidential": "CONFIDENTIAL — MONTH YEAR — DO NOT DISTRIBUTE",
    "logo": "Your Company",
    "date": "",
    "slug": "kebab-case-slug"
  },
  "pages": {
    "page-id": {
      "field": "value with <span class=\"accent\">accent</span> words"
    }
  }
}
```

**Meta defaults:**
- `"logo": "Your Company"` (or whatever the user specifies)
- `"confidential": "CONFIDENTIAL"` (customize per organization)
- If a brand-specific skill exists for the chosen theme, follow its guidance for logo and confidential values.

**CRITICAL — Content JSON completeness:** Every single text element in the deck MUST have a `data-content` attribute and a matching JSON entry. This includes:
- Headings, labels, subtitles, body text, callout text
- Card titles and descriptions
- Bullet point text (`<li>` elements)
- Numbered list items
- Column headers and body text
- **SVG text** (text inside `<text>` elements in diagrams)
- **Graphic labels** (lane labels, status text, annotations on visuals)
- Any editable text the user might want to change

The embedded JSON is the **single source of truth** — localStorage is cleared on every page load.

### Step 7 — Build Slide Sections
Replace the example `<section>` elements inside `<div class="deck">` with the actual slides. For each slide:

1. Use the HTML snippet from the slide-examples reference
2. Set `data-page-id` to match the JSON page key
3. Set `data-content` attributes on **ALL text elements** to match `pageId.fieldName`
4. First slide gets `class="slide [type] active"` (the `active` class) — only the first slide
5. Add visual variety:
   - **Circle motifs**: vary sizes (300-600px), positions (corners). Use the theme's primary color at 0.06-0.08 opacity and secondary color at 0.05-0.06 opacity for border-color.
   - **Footer bars**: alternate `.slide-footer`, `.slide-footer.blue`, `.slide-footer.gradient`
   - **Backgrounds**: mix `bg-dark`, `bg-darker`, `bg-black`
   - **Card accent rules**: alternate default, `.blue`, `.teal`

### Step 8 — Verify
1. Start the preview server and open the presentation
2. Screenshot the title slide, a content slide, and the end slide at minimum
3. Fix any rendering issues
4. Confirm with the user

---

## SAVE & COMMENT WORKFLOW

- **Save button (S key)**: Bakes current content and comments into the embedded `<script>` blocks. Tries `showSaveFilePicker` first (Save As dialog). Falls back to download.
- **Comments (C key)**: Opens the notes panel. Users add per-slide comments. Comments are stored in `<script id="presentation-comments">` and persist on Save.
- **Claude reads comments**: Read the HTML file and extract the `presentation-comments` script block. Each comment is keyed by `data-page-id`. Address each comment, then clear the comments block.
- **Updating content**: When changing text, update in THREE places: (1) the baked HTML in the `<section>`, (2) the content JSON in `<script id="presentation-content">`, (3) any baked form textarea with matching `data-form-field`. Use `replace_all: true` when the same text appears in both HTML and JSON.
- **localStorage cleared on load**: The embedded JSON is always the source of truth.

---

## QUICK REFERENCE: Slide Type Catalog

| Type | Class | Best For |
|------|-------|----------|
| Title | `slide-title` | Opening slide, hero statement |
| Title Centered | `slide-title-centered` | Minimal, centered opening |
| Divider | `slide-divider` | Section breaks, acts |
| Content | `slide-content` | General information |
| Content + Two Col | `slide-content layout-two-col` | Primary + supporting |
| Content + Three Col | `slide-content layout-three-col` | Parallel concepts |
| Card Grid | `slide-content` + `.card-grid-2/3` | Feature comparison, overviews |
| Callout | `slide-callout` | Bold statement, key insight |
| Stats | `slide-stats` | Metrics, impact numbers |
| Numbered List | `slide-numbered-list` | Action items, CTAs |
| Timeline | `slide-timeline` | Roadmaps, phased plans |
| Comparison | `slide-comparison` | Before/after, pros/cons |
| Diagram | `slide-diagram` | Process flows, SVG visuals |
| End | `slide-end` | Closing brand mark |

## QUICK REFERENCE: Inner Components

- `.callout-box` / `.callout-box.blue` — left-border accent box
- `.highlight-box` / `.highlight-box.blue` — lighter accent box
- `.card` + `.card-accent-rule` — bordered card with colored top bar
- `.col-card` / `.col-card.teal` — card with 3px top accent
- `.point-list` / `.point-list.blue` — bullet list with themed dots
- `.insight-list` / `.insight-list.blue` — smaller bullet list
- `.green-bar` / `.green-bar.small` / `.green-bar.blue` — accent divider
- `.stat-block` — number + label for stats slides
- `.ask-item` / `.ask-item.blue` — numbered action item
- `.circle-motif` — decorative border circle (absolute positioned)
- `.struck` — strikethrough for deprecated concepts

## QUICK REFERENCE: Typography

- `.display` — hero text (clamp 2.2-3.8rem, light weight)
- `.h1` — primary heading (clamp 1.6-2.6rem, bold)
- `.h2` — secondary heading (clamp 1.1-1.5rem, bold)
- `.h3` — tertiary heading (clamp 1-1.25rem, bold)
- `.body-text` — paragraph text (clamp 0.9-1.05rem, light)
- `.small-text` — supporting text (clamp 0.8-0.9rem)
- `.label` — section label (0.7rem, uppercase, theme accent color)
- `.subtitle` — subtitle text (body size, secondary color)
- `.accent` — Theme accent styling (ONE per heading)
