#!/usr/bin/env python3
"""Fail on any $$...$$ display equation without an {#eq-...} label.

The lab labels every display equation so that it gets a number and a
stable URL (ai-config AGENTS.md, "Graph and display equation defaults").
The equation-anchors filter adds a permalink only to a labeled equation,
so an unlabeled one has no anchor.

Usage: python3 tools/check_equation_labels.py [FILE_OR_DIR ...]
With no arguments it checks the top-level pages and _subfiles/.
Display math inside code fences is ignored.
"""
import re
import sys
from pathlib import Path

EQ = re.compile(r"\$\$(.+?)\$\$([ \t]*\{#eq-[^}]*\})?", re.S)
FENCE = re.compile(r"^(`{3,}|~{3,}).*?^\1[ \t]*$", re.S | re.M)


def unlabeled(text):
    """Return (line, first 70 chars) for each unlabeled display equation."""
    fences = [m.span() for m in FENCE.finditer(text)]
    found = []
    for m in EQ.finditer(text):
        if m.group(2) or any(a <= m.start() < b for a, b in fences):
            continue
        line = text.count("\n", 0, m.start()) + 1
        found.append((line, " ".join(m.group(1).split())[:70]))
    return found


def targets(args):
    if not args:
        root = Path(".")
        return sorted(root.glob("*.qmd")) + sorted(Path("_subfiles").glob("*.qmd"))
    out = []
    for a in args:
        p = Path(a)
        out += sorted(p.glob("*.qmd")) if p.is_dir() else [p]
    return out


def main(argv):
    bad = 0
    for f in targets(argv):
        for line, body in unlabeled(f.read_text(encoding="utf-8")):
            print(f"{f}:{line}: display equation has no {{#eq-...}} label: {body}")
            bad += 1
    if bad:
        print(
            f"\n{bad} unlabeled display equation(s). "
            "Put a label after the closing $$, e.g. $$ ... $$ {#eq-kraft-inequality}."
        )
        return 1
    print("All display equations are labeled.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
