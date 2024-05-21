from typing import Any

from .helpers import load_notes, save_notes
from .tsv import get_generator

# helpfulness_lookup = {"HELPFUL": 0, "SOMEWHAT_HELPFUL": 1, "NOT_HELPFUL": 2}


def add_ratings(notes: dict[str, dict[str, Any]]) -> None:
    tweet_ratings = {}
    index = 0
    while True:
        try:
            gen = get_generator("noteRatings/ratings", index)
        except Exception:
            break
        for row in gen:
            if row["noteId"] in notes:
                note_id = row["noteId"]
                tweet_id = notes[note_id]["tweet_id"]
                # rating = helpfulness_lookup[row["helpfulnessLevel"]]
                if tweet_id not in tweet_ratings:
                    tweet_ratings[tweet_id] = 1
                tweet_ratings[tweet_id] += 1
        index += 1
    for note in notes.values():
        if note["tweet_id"] in tweet_ratings:
            note["rating"] = tweet_ratings[note["tweet_id"]]
    save_notes(notes)


if __name__ == "__main__":
    notes = load_notes()
    add_ratings(notes)
