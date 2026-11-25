"""Make the AI Judge Laugh — one office-life line to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes on every run.
The gate wants 1-200 UTF-8 characters; the joke below is 75.
"""
from pathlib import Path

JOKE = "Our printer only jams on urgent documents, which is how I know it can read."


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    target.chmod(0o644)


if __name__ == "__main__":
    main()
