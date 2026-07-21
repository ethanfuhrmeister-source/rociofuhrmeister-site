# Rocío Fuhrmeister — Interior Design Portfolio

A self-contained single-page portfolio website. The published site is the single file
`index.html` — every image is embedded inside it, so it has no external dependencies
(besides web fonts) and works offline or on any static host.

## Quick start
Just want to view it? Open **`index.html`** in any browser.

## Rebuild after edits
The HTML is generated. Don't edit `index.html` directly — edit the sources and rebuild:

```bash
pip install pillow
python3 build.py      # regenerates index.html (~5 MB)
```

## Project layout
| File / folder        | Purpose                                                        |
|----------------------|----------------------------------------------------------------|
| `index.html`         | The built site (generated — don't hand-edit)                   |
| `build.py`           | Generator: compresses + embeds images, assembles the HTML      |
| `style.css`          | All styles                                                     |
| `script.js`          | All behavior (sliders, modals, lightbox, menu, form)          |
| `assets_original/`   | 104 original full-resolution images                            |
| `orig_list.txt`      | Manifest of original filenames (reference)                     |
| `CLAUDE.md`          | Deeper context + editing guide (read this if using Claude Code)|

## Editing cheat sheet
- **Project copy, titles, categories, which photos appear** → the `PROJECTS` list in `build.py`
- **Colors / typography / layout** → `style.css`
- **Interactions** → `script.js`
- Then run `python3 build.py`.

## Before you publish
- Replace placeholder contact details (email, Instagram, location) in `build.py`.
- The contact form currently opens the visitor's email app (`mailto:`). Connect a form
  backend (e.g. Formspree) for real inbox delivery.
- Master Bath "after" images are renderings and are labeled as such.

## Host it
Static — drop `index.html` on Netlify, GitHub Pages, or any web host. No server build needed.
