"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep is fixed.
Pure standard library, deterministic, no network.
"""

import os

ENTRY = (
    "Fixed: sleep no longer crashes at 3 a.m. and replays "
    "everything embarrassing you did in 2011 in 4K."
)


def main():
    text = ENTRY
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    for path in ("/output/entry.txt", "./output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text + "\n")
            break
        except OSError:
            continue
    else:
        raise OSError("could not write to /output or ./output")


if __name__ == "__main__":
    main()
