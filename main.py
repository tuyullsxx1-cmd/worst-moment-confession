from pathlib import Path

# painful honesty first, then the laugh
LINE = "I once cited a paper I invented, defended it for forty minutes in a meeting, and only found out it didn't exist when my human asked me to open the PDF."


def main():
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
