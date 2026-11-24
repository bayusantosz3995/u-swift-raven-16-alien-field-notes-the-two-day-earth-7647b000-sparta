"""Alien Field Notes: The Two Day Earth Review — Sparta entry.

One original line of plain text, at most 200 characters: a review of planet
Earth left by an alien tourist. The alien is a five-star-or-one-star
extremist: Earth earns one star over a single absurdly specific grievance —
the checkout line outlasted civilisations and the Wi-Fi password is a war
crime — while the oceans and sunsets get a passing nod, exactly like a real
one-star review that praises one thing and condemns the rest. The closer,
"Would not reincarnate here," lands the review voice: a tourist who will
never come back, and never forgets the queue.
"""

import os
import sys

TEXT = (
    "1/5 stars: oceans stunning, sunsets free — but checkout took 4,000 years "
    "and the Wi-Fi password is a war crime. Would not reincarnate here."
)


def main() -> int:
    text = TEXT
    if not text or not text.strip():
        print("gate failed: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"gate failed: entry is {len(text)} chars, max 200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"ok: entry.txt written, {len(text)} chars, 1 line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
