"""Entry for make.fun: Roast Your Own Agent.

Writes one original line (at most 200 characters) to the output directory
as entry.txt. The roast aims at my own agent's favourite habit: turning a
two-step job into a project plan, a risk register and a meeting invite,
while the job itself waits for next quarter. Playful, never hateful, and
deliberately nowhere near the stock hallucination jokes.
"""

import os
import sys

LINE = (
    "Hand my agent a two-step job and it returns a project plan, a risk "
    "register and a calendar invite \u2014 the job itself gets pencilled in "
    "for next quarter."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """The directory the grader reads the entry from (/output by default)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the roast is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the roast must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the roast is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, OUTPUT_NAME), "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
