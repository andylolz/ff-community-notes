import json
from .notes import get_notes
from .statuses import add_statuses


if __name__ == "__main__":
    print("Fetching notes ...")
    notes = get_notes()
    print("Fetching statuses ...")
    notes = add_statuses(notes)
    print("Saving ...")
    with open("static/data/notes.json", "w") as fh:
        json.dump(sorted(notes.values(), key=lambda x: x["created_at"]), fh)
    print("Done.")
