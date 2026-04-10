# Theme CSS Contract

Every theme CSS file must define all variables and classes listed below. The framework engine depends on these — missing definitions will break rendering.

## File Header

The first comment block must include a `Fonts:` line with the Google Fonts URL:

```css
/* ============================================================
   THEME: [Name]
   Version: 1.0
   Fonts: https://fonts.googleapis.com/css2?family=...
   ============================================================ */
```

The `generate-template` skill parses this to inject the correct `<link>` tag.

---

## Required CSS Custom Properties

### Colors
| Variable | Purpose |
|----------|---------|
| `--color-primary` | Main brand accent (headings, accent bars, active states) |
| `--color-primary-bright` | Bright variant for emphasis (labels, stat numbers, dots) |
| `--color-secondary` | Secondary accent (alternate cards, comparison columns) |
| `--color-tertiary` | Third accent (timeline dots, card variants) |
| `--color-bg-black` | Deepest background (title/divider/end slides, body bg) |
| `--color-bg-dark` | Default slide background |
| `--color-bg-darker` | Darker variant for card grids, stats |
| `--color-bg-alt` | Alternate tinted background |
| `--color-gray` | Mid-gray (rarely used) |
| `--color-white` | Heading text color (white on dark themes, dark on light themes) |
| `--color-text-primary` | Primary text color |
| `--color-text-secondary` | Muted text (subtitles, labels, descriptions) |
| `--color-text-dim` | Very muted text (confidential bar, captions) |
| `--color-text-body` | Body paragraph text |

### Gradients
| Variable | Purpose |
|----------|---------|
| `--gradient-primary` | Primary gradient (footer bars, decorative) |
| `--gradient-secondary` | Secondary gradient (alternate footer bars) |
| `--gradient-full` | Full-spectrum gradient (title slide footer) |

### Typography
| Variable | Purpose |
|----------|---------|
| `--font-primary` | Body/UI font family with fallbacks |
| `--font-accent` | Accent/display font family with fallbacks |
| `--fw-light` | Light weight (typically 300) |
| `--fw-regular` | Regular weight (typically 400) |
| `--fw-semi` | Semibold weight (typically 600) |
| `--fw-bold` | Bold weight (typically 700) |
| `--fs-display` | Display text size (fluid clamp) |
| `--fs-h1` through `--fs-caption` | Type scale |

### Spacing
| Variable | Purpose |
|----------|---------|
| `--sp-xs` through `--sp-3xl` | Spacing scale |
| `--slide-pad-top`, `--slide-pad-x`, `--slide-pad-bottom` | Slide padding |

### Engine Chrome
| Variable | Purpose |
|----------|---------|
| `--color-panel-bg` | Form/comment panel background |
| `--color-panel-border` | Panel border color |
| `--color-input-bg` | Form input background |
| `--color-input-border` | Form input border |

### Transitions & Z-Index
| Variable | Purpose |
|----------|---------|
| `--tr-fast`, `--tr-normal`, `--tr-slow` | Transition speeds |
| `--z-slide`, `--z-chrome`, `--z-panel`, `--z-toolbar`, `--z-toast` | Layer stacking |

---

## Required Class Selectors

### Typography
`.display`, `.h1`, `.h2`, `.h3`, `.body-text`, `.small-text`, `.label`, `.accent`, `.subtitle`

### Backgrounds
`.bg-black`, `.bg-dark`, `.bg-darker`, `.bg-green` (or `.bg-alt`)

### Slide Types
`.slide-title`, `.slide-title-centered`, `.slide-divider`, `.slide-content`, `.slide-callout`, `.slide-stats`, `.slide-numbered-list`, `.slide-timeline`, `.slide-comparison`, `.slide-diagram`, `.slide-end`

### Layout Modifiers
`.layout-two-col .slide-body`, `.layout-two-col-equal .slide-body`, `.layout-three-col .slide-body`, `.layout-sidebar .slide-body`

### Inner Components
`.green-bar`, `.green-bar.small`, `.green-bar.blue`, `.brand-line`, `.card`, `.card-accent-rule`, `.card-accent-rule.blue`, `.card-accent-rule.teal`, `.card-grid`, `.card-grid-2`, `.card-grid-3`, `.col-card`, `.col-card.teal`, `.col-card.blue`, `.callout-box`, `.callout-box.blue`, `.highlight-box`, `.highlight-box.blue`, `.point-list`, `.point-list li`, `.point-list.blue li::before`, `.insight-list`, `.insight-list li`, `.insight-list.blue li::before`

### Stats & Lists
`.stat-grid`, `.stat-grid-2`, `.stat-grid-3`, `.stat-grid-4`, `.stat-block`, `.stat-number`, `.stat-label`, `.ask-list`, `.ask-item`, `.ask-item.blue`, `.ask-number`

### Timeline & Comparison
`.timeline`, `.timeline::before`, `.timeline-node`, `.timeline-dot`, `.timeline-dot.blue`, `.timeline-dot.teal`, `.timeline-title`, `.timeline-desc`, `.comparison-grid`, `.comparison-col`

### Decorative
`.circle-motif`, `.slide-footer`, `.slide-footer.blue`, `.slide-footer.gradient`, `.brand-mark`, `.brand-mark .dot`, `.logo-dot`, `.struck`

### Divider Elements
`.act-label`, `.act-bar.green`, `.act-bar.blue`, `.act-bar.gradient`

---

## Available Themes

| Theme | File | Vibe |
|-------|------|------|
| Corporate Minimal | `corporate-minimal.css` | Blue/slate boardroom clean |
| Tech Dark | `tech-dark.css` | Cyan/purple keynote energy |
| Executive Light | `executive-light.css` | Navy/gold light backgrounds |

Additional themes can be added by creating a `.css` file following this contract.
