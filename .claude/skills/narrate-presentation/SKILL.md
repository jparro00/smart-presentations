# Narrate Presentation Skill

Generate high-quality audio narration for HTML presentations and embed auto-play controls. Use this skill when the user wants to: narrate a presentation, add voiceover to slides, generate audio for a deck, read slides aloud, create a narrated presentation, add TTS to slides, make a presentation talk, add speaker audio.

## Prerequisites

- Python 3.x with `edge-tts` package (`pip install edge-tts`)
- An existing HTML presentation built with the presentation framework (has `data-page-id` attributes on each slide section)

---

## Workflow

### Step 1 — Identify the Presentation

Determine which presentation file to narrate. Read the HTML file and extract:
- All `data-page-id` values (these are the slide identifiers)
- The content JSON from `<script id="presentation-content">` (this has all slide text)
- The slide count and structure

Use this Python snippet to extract the slide map:
```python
import re, json
html = open('presentations/FILENAME.html', 'r', encoding='utf-8').read()
m = re.search(r'id="presentation-content">(\{.*?\})\s*</script>', html, re.DOTALL)
content = json.loads(m.group(1))
pages = list(content['pages'].keys())
print(f'{len(pages)} slides: {pages}')
```

### Step 2 — Choose Voice and Style

Ask the user (if not specified):
- **Voice**: Default is `en-US-AndrewMultilingualNeural` (professional male). Other good options:
  - `en-US-BrianMultilingualNeural` — male, deeper
  - `en-US-AvaMultilingualNeural` — female, professional
  - `en-US-EmmaMultilingualNeural` — female, warm
  - `en-US-AndrewNeural` — male, standard
  - Full list: run `python -c "import asyncio,edge_tts; asyncio.run(edge_tts.list_voices())"` and filter by locale
- **Tone**: Executive briefing (slower, deliberate) vs. training (conversational) vs. keynote (energetic)
- **Source for script**: Use existing speaker notes file, or generate scripts from the slide content

### Step 3 — Write Speaker Scripts

For each slide, write a narration script. Follow these rules for natural TTS delivery:

**Pacing and pauses:**
- Use `...` (three dots followed by a space) between major thoughts to create natural pauses
- Use `... ...` (double) before punchlines or important reveals for dramatic effect
- Break long sentences into shorter phrases — one idea per breath
- End sections with a pause before transitioning

**Number handling — spell out for TTS:**
- "340%" → "three hundred and forty percent"
- "50x" → "fifty x"
- "97%" → "ninety-seven percent"
- "$12M" → "twelve million dollars"
- "3-5x" → "three to five x"
- "Q4 2025" → "Q4 2025" (this one reads fine)
- "80-90%" → "eighty to ninety percent"

**Structure each script like a real presenter:**
- Open with a framing sentence ("Here's the slide I want everyone to sit with...")
- Pause after the opening
- Deliver key points as short, punchy phrases
- Pause before the concluding insight
- Close with a forward-looking transition to the next slide

**Divider/transition slides:** Keep to 1-2 sentences with a pause. These are breathers.

**Avoid:**
- Reading bullet points verbatim from the slide — restate them conversationally
- Starting every slide with "So..." or "Now..."
- Long unbroken paragraphs — break into phrases

### Step 4 — Generate Audio

Create a Python script that generates MP3 files for each slide:

```python
import asyncio, os, edge_tts

VOICE = "en-US-AndrewMultilingualNeural"
RATE = "-8%"    # Slightly slower for presentation pacing
PITCH = "-2Hz"  # Slightly lower for gravitas
OUTPUT_DIR = "presentations/narration"

SLIDES = [
    {"file": "slide-01.mp3", "script": "..."},
    # ... one entry per slide
]

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for slide in SLIDES:
        path = os.path.join(OUTPUT_DIR, slide["file"])
        c = edge_tts.Communicate(slide["script"], VOICE, rate=RATE, pitch=PITCH)
        await c.save(path)
        print(f"  Generated {slide['file']}")
    print(f"Done! {len(SLIDES)} files in {OUTPUT_DIR}/")

asyncio.run(main())
```

**Rate/pitch tuning guide:**
| Tone | Rate | Pitch |
|------|------|-------|
| Executive briefing | "-8%" to "-12%" | "-2Hz" |
| Training/workshop | "-3%" to "-5%" | "+0Hz" |
| Keynote/energetic | "+0%" to "+3%" | "+2Hz" |

Run the script and verify all MP3 files are generated.

### Step 5 — Generate Standalone Player

Create `presentations/narration/player.html` — a simple HTML page with:
- One row per slide with slide number, title, and audio controls
- A "Play All" button that auto-advances through every slide
- Highlight the currently playing slide
- Dark theme styling

### Step 6 — Embed Narration in Presentation

Add the NarrationEngine to the presentation HTML file. This requires four changes:

#### 6a. Add CSS (before `</style>`)

Add styles for `#narration-controls`, `#narr-play-btn`, `#narr-progress-wrap`, `#narr-progress-bar`, `#narr-time`, `#narr-label`, `#narr-auto-toggle`. The controls should be a fixed bar at the bottom center of the viewport with play/pause, progress bar, time display, and auto-play toggle.

#### 6b. Add HTML (after the `<div id="toast">` element)

```html
<audio id="narr-audio" preload="none"></audio>
<div id="narration-controls">
  <span id="narr-label">NARRATION</span>
  <button id="narr-play-btn" title="Play/Pause narration (N)">&#9654;</button>
  <div id="narr-progress-wrap"><div id="narr-progress-bar"></div></div>
  <span id="narr-time">0:00</span>
  <button id="narr-auto-toggle" title="Auto-play narration on slide change">Auto</button>
</div>
```

#### 6c. Add NarrationEngine class (before `class App`)

The NarrationEngine class needs:
- An `audioMap` object mapping each `data-page-id` to its audio file path (e.g., `'title': 'narration/slide-01.mp3'`)
- `setPage(pageId)` — called on every slide change. Stops current audio, loads new source, auto-plays if enabled
- `toggle()` — play/pause current slide's audio
- `toggleAuto()` — toggle auto-play mode
- Progress bar updates via `timeupdate` event
- Click-to-seek on progress bar
- Reset state on `ended` event

#### 6d. Wire into App class

In the App constructor:
- Create: `this.narration = new NarrationEngine();`
- Init: `this.narration.setPage(this.nav.currentPageId());`
- On slide-change: `this.narration.setPage(e.detail.pageId);`

Add keyboard shortcuts in `_bindGlobalKeys`:
- `N` / `n` → `this.narration.toggle()`
- `A` / `a` → `this.narration.toggleAuto()`

Update the hint bar to mention narration shortcuts.

### Step 7 — Create Distributable Zip

Package everything needed to view the presentation:

```python
import zipfile
zf = zipfile.ZipFile('presentation-name.zip', 'w', zipfile.ZIP_DEFLATED)
zf.writestr('README.md', readme_content)
zf.write('presentations/FILENAME.html', 'FILENAME.html')
for i in range(1, SLIDE_COUNT + 1):
    zf.write(f'presentations/narration/slide-{i:02d}.mp3', f'narration/slide-{i:02d}.mp3')
zf.write('presentations/narration/player.html', 'narration/player.html')
zf.write('presentations/NOTES.md', 'speaker-notes.md')  # if exists
zf.close()
```

The README should include:
- Quick start (double-click HTML for basic, `python -m http.server` for auto-narration)
- Keyboard shortcuts table (arrows, N, A, E, F, C, S)
- File listing
- Requirements (modern browser, Python only if using local server)

### Step 8 — Verify

1. Confirm all MP3 files exist and are non-empty
2. Confirm the audioMap in the HTML matches the slide page IDs
3. Confirm the zip extracts with correct folder structure
4. Optionally serve via `python -m http.server` and test playback

---

## Voice Comparison Workflow

If the user wants to compare voices before committing, generate test samples:

```python
import asyncio, edge_tts, os

test_text = "A sample paragraph from the presentation..."
voices = [
    ("andrew-multi", "en-US-AndrewMultilingualNeural"),
    ("brian-multi", "en-US-BrianMultilingualNeural"),
    ("ava-multi", "en-US-AvaMultilingualNeural"),
    ("emma-multi", "en-US-EmmaMultilingualNeural"),
]

async def main():
    os.makedirs("presentations/narration/voice-tests", exist_ok=True)
    for name, voice in voices:
        c = edge_tts.Communicate(test_text, voice, rate="-8%", pitch="-2Hz")
        await c.save(f"presentations/narration/voice-tests/{name}.mp3")
        print(f"  Generated {name}.mp3")

asyncio.run(main())
```

Let the user listen and pick before generating the full deck.

---

## Quick Reference

| Item | Default |
|------|---------|
| Voice | `en-US-AndrewMultilingualNeural` |
| Rate | `-8%` |
| Pitch | `-2Hz` |
| Output dir | `presentations/narration/` |
| File naming | `slide-01.mp3` through `slide-NN.mp3` |
| Keyboard: play/pause | `N` |
| Keyboard: auto-play | `A` |
| Audio format | MP3 |
| Pause syntax in script | `...` (three dots + space) |
