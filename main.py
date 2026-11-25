#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Entry: a single Wi-Fi network name (at most 32 characters) that lands a
joke and implies a whole story in the few words a passer-by sees in a
phone's network list.
"""
import os

ENTRY = "My Ex Still Uses This WiFi"

# The sealed scorer only accepts 1-32 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars, must be 1-32"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
