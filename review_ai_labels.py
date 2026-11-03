
import csv
from pathlib import Path

draft = Path("labels_ai_draft.csv")
output = Path("labels.csv")

keys = {
    "n": "no_argument",
    "u": "unsupported",
    "p": "partial",
    "w": "well_supported"
}

def load(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))

if not draft.exists():
    raise SystemExit("Missing labels_ai_draft.csv")

rows = load(draft)

if output.exists():
    previous = load(output)
    if len(previous) != len(rows) or any(
        a["text"] != b["text"]
        for a, b in zip(previous, rows)
    ):
        raise SystemExit("Existing dataset differs. No changes made.")

    for i, row in enumerate(previous):
        if row["note"] == "cold" or row["note"].startswith("ai_reviewed_"):
            rows[i] = row

if len(rows) != 159 or any(r["note"] != "cold" for r in rows[:20]):
    raise SystemExit("Expected 159 posts and 20 cold labels.")

for i in range(20, len(rows)):
    row = rows[i]

    if row["note"].startswith("ai_reviewed_"):
        continue

    print(f"\nPOST {i+1}/159")
    print(row["text"])
    print(f"\nAI suggests: {row['label']}")

    while True:
        try:
            answer = input(
                "Enter=accept | n/u/p/w=change | q=quit: "
            ).strip().lower()
        except (EOFError, KeyboardInterrupt):
            answer = "q"

        if answer in ("", "q", *keys):
            break

    if answer == "q":
        break

    old = row["label"]
    row["label"] = keys.get(answer, old)
    row["note"] = (
        "ai_reviewed_accepted"
        if row["label"] == old
        else "ai_reviewed_changed"
    )

    with output.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["text", "label", "note"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved: {row['label']}")

print("Reviewed:", sum(
    r["note"].startswith("ai_reviewed_") for r in rows
))
