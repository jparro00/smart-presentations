# Slide Type HTML Examples

These HTML snippets work with ALL themes. Class names are consistent across themes — only the CSS styling differs. Replace `data-page-id` and `data-content` values. The first slide in the deck must include the `active` class.

---

## slide-title

```html
<section class="slide slide-title" data-page-id="PAGE_ID">
  <div class="circle-motif" style="width:450px;height:450px;top:-80px;right:-60px;border-color:rgba(134,188,37,0.08);"></div>
  <div class="circle-motif" style="width:300px;height:300px;top:60px;right:80px;border-color:rgba(0,163,224,0.06);"></div>
  <div class="display" data-content="PAGE_ID.heading"></div>
  <div class="brand-line"></div>
  <div class="subtitle" data-content="PAGE_ID.subtitle"></div>
  <div class="slide-footer gradient"></div>
</section>
```

---

## slide-title-centered

```html
<section class="slide slide-title-centered" data-page-id="PAGE_ID">
  <div class="circle-motif" style="width:500px;height:500px;top:50%;left:50%;transform:translate(-50%,-50%);border-color:rgba(134,188,37,0.06);"></div>
  <div class="display" data-content="PAGE_ID.heading"></div>
  <div class="green-bar" style="margin:20px auto;"></div>
  <div class="subtitle" style="text-align:center;" data-content="PAGE_ID.subtitle"></div>
  <div class="slide-footer gradient"></div>
</section>
```

---

## slide-divider

```html
<section class="slide slide-divider" data-page-id="PAGE_ID">
  <div class="circle-motif" style="width:500px;height:500px;bottom:-180px;right:-100px;border-color:rgba(134,235,34,0.06);"></div>
  <div class="act-label" data-content="PAGE_ID.label"></div>
  <div class="display" data-content="PAGE_ID.heading"></div>
  <div class="act-bar green"></div>
</section>
```

**Variations:**
- Change `.act-bar green` to `.act-bar blue` or `.act-bar gradient` for color variety
- Move circle motif to different corners for visual diversity

---

## slide-content (full-width)

```html
<section class="slide slide-content bg-dark" data-page-id="PAGE_ID">
  <div class="circle-motif" style="width:350px;height:350px;top:-40px;right:-60px;border-color:rgba(134,188,37,0.06);"></div>
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="body-text" data-content="PAGE_ID.body"></div>
  <div class="slide-footer"></div>
</section>
```

### With callout box below body:

```html
<section class="slide slide-content bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="body-text" data-content="PAGE_ID.body"></div>
  <div class="callout-box">
    <div class="small-text" data-content="PAGE_ID.callout"></div>
  </div>
  <div class="slide-footer"></div>
</section>
```

### With point list:

```html
<section class="slide slide-content bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <ul class="point-list">
    <li data-content="PAGE_ID.point-1"></li>
    <li data-content="PAGE_ID.point-2"></li>
    <li data-content="PAGE_ID.point-3"></li>
  </ul>
  <div class="slide-footer"></div>
</section>
```

---

## slide-content layout-two-col

```html
<section class="slide slide-content layout-two-col bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="slide-body">
    <div>
      <div class="body-text" data-content="PAGE_ID.col-left"></div>
    </div>
    <div>
      <div class="body-text" data-content="PAGE_ID.col-right"></div>
    </div>
  </div>
  <div class="slide-footer"></div>
</section>
```

### Two-col with cards:

```html
<section class="slide slide-content layout-two-col-equal bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="slide-body">
    <div class="col-card">
      <div class="h3" data-content="PAGE_ID.card-left-title"></div>
      <ul class="insight-list">
        <li data-content="PAGE_ID.card-left-1"></li>
        <li data-content="PAGE_ID.card-left-2"></li>
      </ul>
    </div>
    <div class="col-card teal">
      <div class="h3" data-content="PAGE_ID.card-right-title"></div>
      <ul class="insight-list blue">
        <li data-content="PAGE_ID.card-right-1"></li>
        <li data-content="PAGE_ID.card-right-2"></li>
      </ul>
    </div>
  </div>
  <div class="slide-footer blue"></div>
</section>
```

---

## slide-content layout-three-col

```html
<section class="slide slide-content layout-three-col bg-darker" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar small"></div>
  <div class="slide-body">
    <div>
      <div class="h3" data-content="PAGE_ID.col-1-title"></div>
      <div class="small-text" data-content="PAGE_ID.col-1-body"></div>
    </div>
    <div>
      <div class="h3" data-content="PAGE_ID.col-2-title"></div>
      <div class="small-text" data-content="PAGE_ID.col-2-body"></div>
    </div>
    <div>
      <div class="h3" data-content="PAGE_ID.col-3-title"></div>
      <div class="small-text" data-content="PAGE_ID.col-3-body"></div>
    </div>
  </div>
  <div class="slide-footer gradient"></div>
</section>
```

---

## Card Grid (2 cards)

```html
<section class="slide slide-content bg-darker" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar small"></div>
  <div class="card-grid card-grid-2">
    <div class="card">
      <div class="card-accent-rule"></div>
      <div class="h3" data-content="PAGE_ID.card-1-title"></div>
      <div class="small-text" data-content="PAGE_ID.card-1-body"></div>
    </div>
    <div class="card">
      <div class="card-accent-rule blue"></div>
      <div class="h3" data-content="PAGE_ID.card-2-title"></div>
      <div class="small-text" data-content="PAGE_ID.card-2-body"></div>
    </div>
  </div>
  <div class="slide-footer blue"></div>
</section>
```

---

## Card Grid (3 cards)

```html
<section class="slide slide-content bg-darker" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar small"></div>
  <div class="card-grid card-grid-3">
    <div class="card">
      <div class="card-accent-rule"></div>
      <div class="h3" data-content="PAGE_ID.card-1-title"></div>
      <div class="small-text" data-content="PAGE_ID.card-1-body"></div>
    </div>
    <div class="card">
      <div class="card-accent-rule blue"></div>
      <div class="h3" data-content="PAGE_ID.card-2-title"></div>
      <div class="small-text" data-content="PAGE_ID.card-2-body"></div>
    </div>
    <div class="card">
      <div class="card-accent-rule teal"></div>
      <div class="h3" data-content="PAGE_ID.card-3-title"></div>
      <div class="small-text" data-content="PAGE_ID.card-3-body"></div>
    </div>
  </div>
  <div class="slide-footer gradient"></div>
</section>
```

---

## slide-callout

```html
<section class="slide slide-callout bg-dark" data-page-id="PAGE_ID">
  <div class="circle-motif" style="width:600px;height:600px;bottom:-200px;left:-200px;border-color:rgba(134,235,34,0.05);"></div>
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="callout-text" data-content="PAGE_ID.statement"></div>
  <div class="slide-footer gradient"></div>
</section>
```

**Variation — with supporting evidence below:**

```html
<section class="slide slide-callout bg-dark" data-page-id="PAGE_ID">
  <div class="circle-motif" style="width:600px;height:600px;bottom:-200px;right:-200px;border-color:rgba(0,163,224,0.05);"></div>
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="callout-text" data-content="PAGE_ID.statement"></div>
  <div class="highlight-box" style="margin-top:32px;max-width:700px;">
    <div class="small-text" data-content="PAGE_ID.evidence"></div>
  </div>
  <div class="slide-footer blue"></div>
</section>
```

---

## slide-stats

```html
<section class="slide slide-stats bg-darker" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="stat-grid stat-grid-3">
    <div class="stat-block">
      <div class="stat-number" data-content="PAGE_ID.stat-1-number"></div>
      <div class="stat-label" data-content="PAGE_ID.stat-1-label"></div>
    </div>
    <div class="stat-block">
      <div class="stat-number" data-content="PAGE_ID.stat-2-number"></div>
      <div class="stat-label" data-content="PAGE_ID.stat-2-label"></div>
    </div>
    <div class="stat-block">
      <div class="stat-number" data-content="PAGE_ID.stat-3-number"></div>
      <div class="stat-label" data-content="PAGE_ID.stat-3-label"></div>
    </div>
  </div>
  <div class="slide-footer"></div>
</section>
```

**For 2 stats:** Use `stat-grid-2`, **For 4 stats:** Use `stat-grid-4`

---

## slide-numbered-list

```html
<section class="slide slide-numbered-list bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="ask-list">
    <div class="ask-item">
      <div class="ask-number">1</div>
      <div class="ask-body">
        <div class="h3" data-content="PAGE_ID.action-1-title"></div>
        <div class="small-text" data-content="PAGE_ID.action-1-desc"></div>
      </div>
    </div>
    <div class="ask-item blue">
      <div class="ask-number">2</div>
      <div class="ask-body">
        <div class="h3" data-content="PAGE_ID.action-2-title"></div>
        <div class="small-text" data-content="PAGE_ID.action-2-desc"></div>
      </div>
    </div>
    <div class="ask-item">
      <div class="ask-number">3</div>
      <div class="ask-body">
        <div class="h3" data-content="PAGE_ID.action-3-title"></div>
        <div class="small-text" data-content="PAGE_ID.action-3-desc"></div>
      </div>
    </div>
  </div>
  <div class="slide-footer blue"></div>
</section>
```

**Alternate colors:** Every other `.ask-item` gets `.blue` for visual rhythm.

---

## slide-timeline

```html
<section class="slide slide-timeline bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="timeline">
    <div class="timeline-node">
      <div class="timeline-dot"></div>
      <div class="timeline-title" data-content="PAGE_ID.node-1-title"></div>
      <div class="timeline-desc" data-content="PAGE_ID.node-1-desc"></div>
    </div>
    <div class="timeline-node">
      <div class="timeline-dot blue"></div>
      <div class="timeline-title" data-content="PAGE_ID.node-2-title"></div>
      <div class="timeline-desc" data-content="PAGE_ID.node-2-desc"></div>
    </div>
    <div class="timeline-node">
      <div class="timeline-dot teal"></div>
      <div class="timeline-title" data-content="PAGE_ID.node-3-title"></div>
      <div class="timeline-desc" data-content="PAGE_ID.node-3-desc"></div>
    </div>
    <div class="timeline-node">
      <div class="timeline-dot"></div>
      <div class="timeline-title" data-content="PAGE_ID.node-4-title"></div>
      <div class="timeline-desc" data-content="PAGE_ID.node-4-desc"></div>
    </div>
  </div>
  <div class="slide-footer gradient"></div>
</section>
```

---

## slide-comparison

```html
<section class="slide slide-comparison bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="green-bar"></div>
  <div class="comparison-grid">
    <div class="comparison-col">
      <div class="h3" data-content="PAGE_ID.col-left-heading"></div>
      <ul class="insight-list">
        <li data-content="PAGE_ID.left-1"></li>
        <li data-content="PAGE_ID.left-2"></li>
        <li data-content="PAGE_ID.left-3"></li>
      </ul>
    </div>
    <div class="comparison-col">
      <div class="h3" data-content="PAGE_ID.col-right-heading"></div>
      <ul class="insight-list blue">
        <li data-content="PAGE_ID.right-1"></li>
        <li data-content="PAGE_ID.right-2"></li>
        <li data-content="PAGE_ID.right-3"></li>
      </ul>
    </div>
  </div>
  <div class="slide-footer blue"></div>
</section>
```

---

## slide-diagram

```html
<section class="slide slide-diagram bg-dark" data-page-id="PAGE_ID">
  <div class="label" data-content="PAGE_ID.label"></div>
  <div class="h1" data-content="PAGE_ID.heading"></div>
  <div class="diagram-area">
    <!-- SVG goes here — custom per diagram -->
    <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
      <!-- Build SVG content as needed -->
    </svg>
  </div>
  <div class="slide-footer gradient"></div>
</section>
```

Note: Diagram SVGs are custom — use CSS custom property values for colors. Read the theme CSS to find the actual hex values, or use these semantic tokens in inline styles:
- Primary: `var(--color-primary)`, Bright: `var(--color-primary-bright)`
- Secondary: `var(--color-secondary)`, Tertiary: `var(--color-tertiary)`
- Text: `var(--color-text-primary)`, Muted: `var(--color-text-secondary)`
- Lines/borders: `var(--color-panel-border)` or `rgba(255,255,255,0.15)` for dark themes

---

## slide-end

```html
<section class="slide slide-end" data-page-id="end">
  <div class="circle-motif" style="width:700px;height:700px;border-color:rgba(134,188,37,0.06);top:50%;left:50%;transform:translate(-50%,-50%);"></div>
  <div class="brand-mark" style="font-size:2.2rem;" data-content="end.brand"></div>
  <div class="tagline" data-content="end.tagline"></div>
  <div class="copyright" data-content="end.copyright"></div>
</section>
```

**Standard JSON for end slide:**
```json
"end": {
  "brand": "Your Company",
  "tagline": "",
  "copyright": ""
}
```

---

## Circle Motif Placement Guide

Add 1-2 circle motifs per slide for visual depth. Never more than 3. Never overlapping.

**Common placements:**
```html
<!-- Top-right (most common) -->
<div class="circle-motif" style="width:350px;height:350px;top:-40px;right:-60px;border-color:rgba(134,188,37,0.06);"></div>

<!-- Bottom-right -->
<div class="circle-motif" style="width:500px;height:500px;bottom:-180px;right:-100px;border-color:rgba(134,235,34,0.06);"></div>

<!-- Bottom-left -->
<div class="circle-motif" style="width:600px;height:600px;bottom:-200px;left:-200px;border-color:rgba(134,235,34,0.05);"></div>

<!-- Centered (for end slides) -->
<div class="circle-motif" style="width:700px;height:700px;top:50%;left:50%;transform:translate(-50%,-50%);border-color:rgba(134,188,37,0.06);"></div>

<!-- Smaller secondary motif -->
<div class="circle-motif" style="width:200px;height:200px;top:100px;right:120px;border-color:rgba(0,163,224,0.05);"></div>
```

**Color options:**
- Green: `rgba(134,188,37,0.06)` to `rgba(134,188,37,0.08)`
- Neon green: `rgba(134,235,34,0.05)` to `rgba(134,235,34,0.06)`
- Blue: `rgba(0,163,224,0.05)` to `rgba(0,163,224,0.06)`

---

## Footer Bar Variety

Alternate across slides for visual rhythm:
```html
<div class="slide-footer"></div>           <!-- Green gradient (default) -->
<div class="slide-footer blue"></div>      <!-- Blue-green gradient -->
<div class="slide-footer gradient"></div>  <!-- Full rainbow gradient -->
```
