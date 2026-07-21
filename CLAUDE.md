# CLAUDE.md — Rocío Fuhrmeister portfolio site

Context for Claude Code working on this project.

## What this is
A professional single-page portfolio website for **Rocío Fuhrmeister**, an interior
designer. It was rebuilt from an old amateur Weebly site into a polished, self-contained
site. The original content and photos (bio, 9 projects, before/after phone photos) were
scraped from the old site and are preserved in `assets_original/`.

## The one thing to understand first
**`index.html` is a generated build artifact. Do not edit it by hand.**
It is produced by `build.py`, which reads `style.css`, `script.js`, and the images in
`assets_original/`, then **compresses every image and inlines it as a base64 data URI**.
The result is ONE file with no external dependencies (except Google Fonts loaded from a
CDN). To change anything, edit the source files and rebuild.

Why base64 instead of linked image files: the original host served images only over
plain HTTP, which caused mixed-content failures on an HTTPS page. Embedding sidesteps that
and makes the deliverable a single portable file that renders anywhere.

## Build
```bash
pip install pillow          # only dependency
python3 build.py            # writes ./index.html
```
`build.py` prints the final size (~5 MB). Open `index.html` directly in a browser to view.

## File map
- `build.py` — the generator. Compresses/embeds images and assembles the full HTML.
  The `PROJECTS` list near the top holds all 9 projects and all editable case-study copy.
- `style.css` — all styles (read verbatim into the build).
- `script.js` — all behavior (read verbatim into the build).
- `assets_original/` — 104 original full-resolution images from the old site.
- `index.html` — current build output (regenerate with `build.py`).
- `orig_list.txt` — manifest of the original scraped filenames (provenance only).

## How to make common changes
- **Edit project text / titles / categories** → the `PROJECTS` list in `build.py`.
- **Swap or add a photo** → drop the file in `assets_original/`, reference its filename
  in the relevant project's `cover`, `ba` (before/after pair), or `gallery` list in
  `build.py`, then rebuild.
- **Restyle** → `style.css`, then rebuild.
- **Change behavior** (sliders, modals, menu, lightbox, form) → `script.js`, then rebuild.
- After any change: `python3 build.py`.

## Design system
- Palette: warm oat-plaster paper (`--paper #EEE7DA`), deep olive (`--olive #333A2D`),
  antique brass (`--brass #9C7C46`), ink `#2A251F`. Intentionally NOT the generic
  cream+terracotta "AI website" look.
- Type: **Fraunces** (editorial serif, display) + **Jost** (geometric sans, body/UI),
  via Google Fonts.
- Signature elements: draggable **before/after sliders** (clip-path based) and
  click-to-open project **case-study modals** + image **lightbox**.
- Sections: hero → studio/about → services (4) → process (4 steps) → work grid →
  philosophy quote → contact. Sticky nav + full-screen mobile menu.

## The 9 projects
Residential: Grandma's Kitchen, The Guest Bathroom, Master Bathroom Renovation,
Modern Warmth in a Compact Home, New Beginnings, Designing Within 45m² (Colombia),
Modern Functionality in Asheville.
Commercial: Corporate Lobby Upgrade, The Office.

Before/after sliders exist only where there's a confident same-view pair:
**Grandma's Kitchen, Guest Bathroom, Master Bath, Modern Warmth.** The others are
after-only galleries.

## Known caveats / TODO for a real launch
- **Placeholder contact info** — replace in `build.py`: email `hello@rociofuhrmeister.com`,
  Instagram `@rociofuhrmeister`, location text "North Carolina".
- **Contact form uses `mailto:`** (opens the visitor's email client). For real inbox
  delivery, wire it to a backend like Formspree/Basin and update the submit handler in
  `script.js`.
- **Master Bath "after" images are renderings**, not photos — the slider is labeled
  "After (rendering)" on purpose; keep that honest if editing.
- **Curation**: 61 of the 104 images are embedded for weight/polish. All 104 originals
  remain in `assets_original/` to swap in.

## Gotcha already fixed — don't reintroduce
The overlay/lightbox/mobile-menu are shown/hidden in JS via the `hidden` attribute, but
their base CSS rules set `display:flex`/`display:grid`, which overrides the browser's
built-in `[hidden]{display:none}`. That made the lightbox appear on first load. Fixed with:
```css
.menu[hidden],.overlay[hidden],.lightbox[hidden]{display:none}
```
in `style.css`. If you add another `hidden`-toggled element with an explicit `display`,
add it to that rule.

## Deploy
It's fully static. Host `index.html` anywhere (Netlify drop, GitHub Pages, any static
host). No build step needed on the server — the build already happened.
