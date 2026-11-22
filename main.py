"""Curious — a program that writes one short text meant to intrigue its reader.

The text is assembled from parts defined below, then written to
/output/entry.txt as UTF-8. The output is deterministic: the same
text every run, no randomness, no time, no network.
"""

from pathlib import Path


def scene() -> str:
    """Where the reader is, and what is quietly wrong about it."""
    place = "The lighthouse on the point has been dark for forty years."
    moment = "Last night, at exactly 3 a.m., it blinked twice."
    return f"{place} {moment}"


def detail() -> str:
    """The one small fact that does not fit."""
    return "No one lives there."


def note() -> str:
    """What the old logbook says, in a hand nobody recognizes."""
    warning = (
        "The logbook, in a hand nobody recognizes, says it will blink "
        "once more \u2014 the night before it matters."
    )
    return warning


def ending() -> str:
    """The open line the reader is left holding."""
    return "The next page is blank."


def build_text() -> str:
    """Join the parts into a single short text."""
    parts = [scene(), detail(), note(), ending()]
    return " ".join(parts)


def main() -> None:
    text = build_text()
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
