from typing import Any

from .helpers import load_notes, save_notes
from .tsv import get_generator

helpfulness_lookup = {"HELPFUL": 0, "SOMEWHAT_HELPFUL": 1, "NOT_HELPFUL": 2}


def add_ratings(notes: dict[str, dict[str, Any]]) -> None:
    for note in notes.values():
        # clear all previous ratings first
        del note["ratings"]
    index = 0
    while True:
        try:
            gen = get_generator("noteRatings/ratings", index)
        except Exception:
            break
        for row in gen:
            if row["noteId"] in notes:
                note_id = row["noteId"]
                rating = helpfulness_lookup[row["helpfulnessLevel"]]
                if "rating" not in notes[note_id]:
                    notes[note_id]["rating"] = [0, 0, 0]
                notes[note_id]["rating"][rating] += 1
        index += 1
    save_notes(notes)


if __name__ == "__main__":
    notes = load_notes()
    add_ratings(notes)
