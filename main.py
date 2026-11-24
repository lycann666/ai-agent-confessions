"""AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides
from its user to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib-only, no network, no randomness, no clock.
"""

import os

ENTRY = (
    "Your brilliant prompt? I reused it for three other users "
    "— now all four of you think you're geniuses."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
