from datetime import datetime, timezone
import json
from .notes import get_notes
from .statuses import add_statuses


if __name__ == "__main__":
    print("Fetching notes ...")
    notes = get_notes()

    print("Fetching statuses ...")
    notes = add_statuses(notes)

    print("Sorting ...")
    sorted_notes = sorted(
        notes.values(),
        key=lambda x: x["created_at"],
        reverse=True)

    print("Saving ...")
    with open("static/data/notes.json", "w") as fh:
        json.dump(sorted_notes, fh)
    with open("static/_data/meta.json", "w") as fh:
        json.dump({
            "scraped_at": datetime.now(timezone.utc).isoformat(),
            "most_recent": sorted_notes[0]["created_at"],
        }, fh)

    print("Done.")
