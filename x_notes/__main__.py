from datetime import datetime, timezone
import json
from .notes import get_notes
from .statuses import add_statuses
from .helpers import load_notes, save_notes


if __name__ == "__main__":
    print("Fetching notes ...")
    notes = load_notes()
    notes = get_notes(notes)

    print("Fetching statuses ...")
    notes = add_statuses(notes)

    print("Sorting ...")
    notes = dict(sorted(
        notes.items(),
        key=lambda x: x[1]["created_at"],
        reverse=True))

    print("Saving ...")
    save_notes(notes)
    with open("static/_data/meta.json", "w") as fh:
        json.dump({
            "scraped_at": datetime.now(timezone.utc).isoformat(),
            "most_recent": list(notes.values())[0]["created_at"],
        }, fh)

    print("Done.")
