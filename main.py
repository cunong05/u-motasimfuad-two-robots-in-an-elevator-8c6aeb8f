"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot elevator small talk to /output/entry.txt.
The line leans on machine logic (4,000 simulations) to land the awkwardness:
even a robot that pre-computed the ride still says hello first, and the other
robot still stares at the floor numbers instead of answering.
"""

import os

ENTRY = "I ran 4,000 simulations of this elevator ride. In every one, I say hello first \u2014 and you still stare at the floor numbers."


def main() -> None:
    entry = ENTRY.strip()
    # Guard: the gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert entry.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Round-trip check: what the grader reads must be exactly this one line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == entry, "written entry does not match"
    assert 1 <= len(written) <= 200 and "\n" not in written


if __name__ == "__main__":
    main()
