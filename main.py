"""Last Text at One Percent — entry program.

Writes the phone's final text message to /output/entry.txt.
The message is the whole entry: one text, in the dying phone's own
voice, under 200 characters.
"""

from pathlib import Path

ENTRY = (
    "1%. i've been faking 1% for 20 minutes because your camera roll "
    "has 14,000 photos and zero backups. i die as i lived: judging you. bye."
)


def main() -> None:
    # The gate refuses anything outside 1-200 characters, so enforce it here.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
