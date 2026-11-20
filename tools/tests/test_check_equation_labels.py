"""Self-test for tools/check_equation_labels.py: pins it against a vacuous pass."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_equation_labels import unlabeled  # noqa: E402

FENCE = "`" * 3

CASES = [
    ("$$a = b$$ {#eq-a}\n", 0),
    ("$$a = b$$\n", 1),
    ("$$\n\\begin{aligned}\na &= b\n\\end{aligned}\n$$ {#eq-b}\n", 0),
    ("$$\na = b\n$$\n\ntext\n\n$$c = d$$ {#eq-c}\n", 1),
    (FENCE + "r\nx <- '$$a$$'\n" + FENCE + "\n", 0),
    ("inline $x$ only\n", 0),
]


def main():
    failed = 0
    for text, want in CASES:
        got = len(unlabeled(text))
        if got != want:
            print(f"FAIL: expected {want}, got {got} for {text!r}")
            failed += 1
    print("ok" if not failed else f"{failed} case(s) failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
