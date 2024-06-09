from typing import Any

from .helpers import load_notes, save_notes
from .tsv import get_generator

# helpfulness_lookup = {"HELPFUL": 0, "SOMEWHAT_HELPFUL": 1, "NOT_HELPFUL": 2}


def add_ratings(notes: dict[str, dict[str, Any]]) -> None:
    index = 0
    while True:
        try:
            gen = get_generator("noteRatings/ratings", index)
        except Exception:
            break
        for row in gen:
            if row["noteId"] in notes:
                note = notes[row["noteId"]]
                # rating = helpfulness_lookup[row["helpfulnessLevel"]]
                if "rating" not in note:
                    note["rating"] = 0
                note["rating"] += 1
        index += 1
    save_notes(notes)


if __name__ == "__main__":
    notes = load_notes()
    add_ratings(notes)
