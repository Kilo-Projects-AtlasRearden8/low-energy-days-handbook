# STATUS — Low-Energy Days Handbook

## What was built

A beginner manual on low-energy and ADHD-friendly productivity, delivered as
Markdown docs (`docs/`) plus a static HTML site (`site/`) with printable
routine cards.

**Manual (docs/):**
- `intro.md` — welcome, who this is for, core idea, how to use
- `pick-one-task.md` — choosing just one task, how to choose, ADHD tips
- `gentle-scheduling.md` — soft times not deadlines, blocks, sample day
- `rest-without-guilt.md` — rest is not a reward, handling guilt
- `energy-tracking.md` — one-word daily energy check-in, optional notes
- `low-demand-routines.md` — example routines, build your own, ADHD tips
- `routine-cards.md` — how to print and use the cards

**Static site (site/):**
- `site/index.html` — polished, navigable version of the manual
- `site/cards.html` — printable routine cards with print CSS (cut-out lines,
  black-and-white friendly)
- `site/css/style.css` — warm, accessible styling with print overrides
- `site/js/site.js` — minimal progressive-enhancement entry point

**Other files:**
- `README.md` — project overview, credits Asdale Dynamics, LLC
- `LICENSE` — MIT, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `.gitignore` — OS, editor, build, log ignores
- `verify.py` — verification script

## How to run it

There is no build step. It is local-first static files.

- Read the manual: open any file in `docs/`, or open `site/index.html` in a web
  browser.
- Print the cards: open `site/cards.html` in a browser, click "Print Cards" or
  press Ctrl+P, choose landscape if offered, print, and cut along dashed lines.
- Run verification: `python3 verify.py`

## Verification results

`python3 verify.py` — all 27 checks passed:

- All 15 required files present
- LICENSE contains exact copyright line
- README credits Asdale Dynamics, LLC
- Both HTML files well-formed (DOCTYPE, balanced tags, stylesheet linked)
- cards.html has print media query, print trigger, and print card grid
- No secret or personal-data patterns found (API keys, AWS keys, GitHub tokens,
  SSN-like patterns)
- No `.github/workflows` directory

HTML tag balance verified with Python's html.parser — zero unclosed tags in
both pages.

Git initialized and committed as `3d31030` ("Add Low-Energy Days Handbook with
printable routine cards"), 15 files, using existing identity (Dylan Asdale /
dylanasdale@users.noreply.github.com). No co-author trailers. Not pushed, no
remote created.

## Known gaps

- No automated HTML validator beyond tag-balance check (no external validator
  dependency added, to keep it dependency-free and local-first).
- Cards print test is visual (browser print) rather than automated pixel check.
- No search, dark mode, or font-size controls on the site (intentionally
  minimal; can be added later).
- No CI/CD (`.github/workflows` deliberately omitted per instructions).
