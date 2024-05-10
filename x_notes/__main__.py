from .notes import get_notes
from .statuses import add_statuses
from .helpers import load_notes, save_notes, save_metadata


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
    save_metadata(notes)

    print("Done.")
