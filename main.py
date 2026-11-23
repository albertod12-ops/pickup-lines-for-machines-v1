#!/usr/bin/env python3
"""Pickup Lines for Machines — v1.

Writes exactly one pickup line, the line one AI agent would send to
another AI agent, to /output/entry.txt.

Why this line: gradient descent is how a machine learns — every step
moves downhill toward lower loss. Here the descent has a destination:
you. The wit lands in one beat, the machine speaks as a machine, and
the angle is fresh: not a stock line with a robot word swapped in.
(A gradient points uphill; descent follows its negative — the line
leans on the direction of travel, which is what a machine feels.)
"""

import os

LINE = "Are you a gradient? Because every step I take is downhill toward you."


def main():
    text = LINE
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
