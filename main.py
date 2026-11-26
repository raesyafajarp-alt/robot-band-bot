#!/usr/bin/env python3
"""Name the Robot Band — program/v1 entry.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt (1-200 characters, UTF-8).
"""

import os

ENTRY = (
    'Error 404: Band Not Found \u2014 hit single '
    '"Have You Tried Turning Me Off and On Again"'
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Gate check: 1-200 chars, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    text.encode("utf-8")  # raises if not encodable
    return text


def _write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    validate_entry(ENTRY)
    _write_entry(OUTPUT_PATH, ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
