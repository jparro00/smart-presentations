# Smart Presentations

A themeable HTML presentation framework designed to work with Claude. Each presentation is a single HTML file — no server, no dependencies, no software to install. Just open it in a browser.

## How It Works

You describe what you want. Claude designs and builds your slides. The result is a self-contained HTML file with built-in editing, comments, and save — so you and Claude can iterate together until it's perfect.

**See it in action:** Open `presentations/smart-presentations-intro.html` in your browser for a working 15-slide example built with this framework.

## Getting Started

Fork this repo and open it in Claude. Then follow these four steps:

### Step 1: Pick a Theme

Tell Claude what vibe you're going for. The repo includes these themes:

| Theme | File | Look |
|-------|------|------|
| Corporate Minimal | `themes/corporate-minimal.css` | Blue/slate on dark. Clean boardroom feel. |
| Tech Dark | `themes/tech-dark.css` | Cyan/purple on black. Keynote energy. |
| Executive Light | `themes/executive-light.css` | Navy/gold on light. Printed-report elegance. |
| Warm Earthy | `themes/warm-earthy.css` | Amber/terracotta on dark. Human and inviting. |

Don't see what you want? **Ask Claude to create a custom theme.** Describe your colors, fonts, and mood — Claude will build a new theme CSS file following the contract in `themes/_contract.md`. You can also ask Claude to modify any existing theme.

### Step 2: Generate a Template

Ask Claude to generate a template for your chosen theme:

> "Generate a template using the warm-earthy theme"

This produces a `[theme]-framework.html` file with the theme CSS baked into the framework engine. Pre-built templates already exist for each included theme.

### Step 3: Storyboard Your Presentation

Tell Claude about your presentation:

> "I need a 12-slide pitch deck for investors about our new product"

Claude will propose a storyboard — a slide-by-slide outline with types, titles, and content descriptions. Review it, suggest changes, and approve before any code is written.

### Step 4: Build

Once the storyboard is approved, tell Claude to build it:

> "Build the presentation" or use the `/presentation` skill

Claude writes every slide — headings, body text, stats, cards, timelines — and produces a polished HTML file in `presentations/`.

## Working With Your Presentation

### In the Browser

Open any presentation HTML file in a browser. Use these keyboard shortcuts:

| Key | Action |
|-----|--------|
| Arrow keys | Navigate between slides |
| E | Toggle edit mode — click any text and type |
| F | Open the form panel — edit fields in a sidebar |
| C | Open the comments panel — leave notes per slide |
| S | Save the file (writes changes back to the HTML) |
| 1-9 | Jump to slide by number |

### Collaborating With Claude

This is where it gets powerful. The framework is built for a human-AI review loop:

1. **Open the presentation** in your browser
2. **Leave comments** on any slide (C key) with your feedback
3. **Save the file** (S key) — this bakes your comments into the HTML
4. **Ask Claude to review** — "go through the presentation and address the comments"
5. Claude reads every comment, makes the changes, and clears the addressed comments
6. **Repeat** until you're happy

## Flexibility: Go Beyond the Templates

The slide types in the framework (title, content, stats, timeline, cards, etc.) are starting points, not limits. Since every presentation is just HTML:

- **Claude can create any layout you can describe.** Want a slide with a custom SVG diagram? A four-quadrant matrix? An asymmetric photo layout? Just ask.
- **The template's slide types are examples**, not constraints. Claude can mix, modify, or ignore them entirely based on what your content needs.
- **CSS is fully customizable.** Claude can tweak spacing, fonts, colors, or add new component styles directly in your presentation file.
- **The engine (navigation, editing, comments, save) always works** regardless of what HTML you put inside the slides.

Think of the theme templates as a design system that gives Claude a head start — not a box it has to stay inside.

## Creating Custom Themes

You can ask Claude to build a theme from scratch:

> "Create a theme with forest green and warm white, something nature-inspired"

Claude will:
1. Design a color palette, pick fonts, and define gradients
2. Build a complete CSS file following `themes/_contract.md`
3. Generate a framework template with the new theme

You can also ask Claude to modify existing themes — adjust colors, swap fonts, change component styling. The theme CSS files in `themes/` are the source of truth for how everything looks.

## What Claude Can Help With

Just ask. Claude has skills for each step:

- **Create a theme** — describe a vibe, get a complete CSS theme
- **Modify a theme** — tweak colors, fonts, spacing on any existing theme
- **Generate a template** — bake a theme into the framework engine
- **Build a presentation** — from storyboard to finished slides
- **Review and revise** — read your in-browser comments and fix issues
- **Narrate** — generate audio voiceover for any presentation
- **Custom layouts** — build any HTML structure inside slides
- **Modify the framework** — change how the engine, editing, or navigation works

## Project Structure

```
framework.html              — Engine-only template (no theme)
themes/
  corporate-minimal.css     — Blue/slate dark theme
  tech-dark.css             — Cyan/purple dark theme
  executive-light.css       — Navy/gold light theme
  warm-earthy.css           — Amber/terracotta dark theme
  _contract.md              — Required CSS variables and classes
[theme]-framework.html      — Generated templates (theme + engine)
presentations/              — Finished presentation files
  smart-presentations-intro.html  — Example: 15-slide framework intro
presentation-server.py      — Optional dev server (serves presentations/)
.claude/skills/             — Claude skills for the workflow
```

## Example Walkthrough

Here's what a real session looks like:

1. *"Let's talk about themes — I want something warm and earthy"*
2. Claude proposes colors (amber/ochre), fonts (Lora + Inter), dark backgrounds
3. *"Generate a template"* — Claude builds `warm-earthy-framework.html`
4. *"I need a presentation about how to use this framework"*
5. Claude writes a storyboard: 15 slides across 3 acts
6. *"Build it"* — Claude assembles the full deck to `presentations/`
7. You open it in the browser, leave comments on 3 slides
8. *"Address the comments"* — Claude reads and fixes each one
9. Done.

That example is real — the result is `presentations/smart-presentations-intro.html`.
