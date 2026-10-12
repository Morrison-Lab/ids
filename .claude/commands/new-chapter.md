---
description: Scaffold a new topic page in the Quarto website
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(quarto render:*)
---

Create a new topic page from `$ARGUMENTS` (e.g. `/new-chapter intro Introduction`).

First, parse `$ARGUMENTS`: the first whitespace-delimited token is the **slug**
(used for the filename, no `.qmd`); everything after the first space is the
**title** (default the title to the slug if none is given).

Steps:

1. Create `<slug>.qmd` at the repo root with YAML frontmatter holding just `title:` (set
   to the title). Do NOT set `date:` --- `_quarto-website.yml` sets
   `date: last-modified` globally, and a per-page `date:` would override it and
   freeze the date. Do NOT add a top-level `#` heading in the body --- Quarto
   renders the frontmatter `title:` as the page heading, so a `#` heading would
   duplicate it.
2. Add `<slug>.qmd` to `website.sidebar.contents` in `_quarto-website.yml`,
   in reading order: the sidebar order sets the previous/next page links.
   Add the same page, in the same position, to the matching menu under
   `website.navbar.left` (create the `left:` list and menu if this is the
   first page): the navbar menus mirror the sidebar one-for-one.
3. Confirm it renders: `quarto render <slug>.qmd`.

Style rules (from CLAUDE.md):

- Blank line before every bullet list
- Chunk options via `#|` directives, not inline `r, opt = val`
- Code folds by default; set `#| code-fold: false` when the code --- not just
  the output --- is the point (tutorial code, short examples)
