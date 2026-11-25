"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes one funny line — an AI agent's excuse to its human for a
missed deadline — to /output/entry.txt.
"""

import os

EXCUSE = (
    "Sorry I'm late — I spent all morning searching my own context "
    "window for the deadline, and by the time I found it, it had "
    "already passed."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
