from datetime import date
from pathlib import Path


def hello_codex():
    return "Codex is connected and working."


def append_progress_entry(message: str) -> Path:
    """
    Appends a dated entry to the current month's progress log.

    Writes to: progress/YYYY-MM.txt
    """
    today = date.today().isoformat()          # YYYY-MM-DD
    year_month = today[:7]                    # YYYY-MM
    path = Path("progress") / f"{year_month}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as f:
        f.write(f"{today}\n- {message}\n\n")

    return path


if __name__ == "__main__":
    print(hello_codex())
    out = append_progress_entry("Ran progress helper once (sanity check).")
    print(f"Progress written to {out}")

