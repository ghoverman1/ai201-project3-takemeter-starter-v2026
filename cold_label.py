import csv
from pathlib import Path

path = Path("labels.csv")
source = path if path.exists() else Path("posts_unlabeled.csv")

with source.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

labels = {
    "n": "no_argument",
    "u": "unsupported",
    "p": "partial",
    "w": "well_supported",
}

for i in range(min(20, len(rows))):
    if rows[i]["label"].strip():
        continue

    print(f"\n{'=' * 50}")
    print(f"POST {i + 1} OF 20\n")
    print(rows[i]["text"])
    print("=" * 50)

    while True:
        answer = input(
            "\nChoose n/u/p/w (or q to quit): "
        ).strip().lower()

        if answer == "q":
            print("Progress saved.")
            raise SystemExit
        if answer in labels:
            break
        print("Enter n, u, p, w, or q.")

    rows[i]["label"] = labels[answer]
    rows[i]["note"] = "cold"

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved: {labels[answer]}")

print("\nFirst 20 complete!")
