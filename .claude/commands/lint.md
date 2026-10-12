---
description: Lint all R source files and report issues
allowed-tools:
  - Bash(rm -f ids)
  - Bash(Rscript -e 'lintr::lint*')
---

First run `rm -f ids` to remove the repo's self-referential `ids -> .` symlink
(see CLAUDE.md) from the working tree. `lintr::lint_dir()`'s own directory
walk follows symlinks and has no config-level way to skip it (any
`.lintr.R` exclusion naming `ids` collapses onto the real files it aliases
and silently excludes them too --- see `.lintr.R`'s comment), so with the
symlink present every real lint is duplicated dozens of times over. Removing
it first is safe: it only deletes the symlink, never the directory it points
into.

Then run `Rscript -e 'lintr::lint_dir()'` to check all R source files against `.lintr.R`.
Afterwards, whether or not lint succeeds, restore the symlink with
`git checkout -- ids`, so the deletion is never committed.

Report all lint issues grouped by file, including:

- File path and line number
- The lint rule violated
- A one-line explanation of how to fix it

If there are no issues, confirm the code is clean.
