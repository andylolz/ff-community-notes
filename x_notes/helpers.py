import json
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any


def to_isoformat(ms_since_epoch: str) -> str:
    return datetime.fromtimestamp(int(ms_since_epoch[:-3]), timezone.utc).isoformat()


def load_notes() -> dict[str, dict[str, Any]]:
    try:
        with open("output/data/notes.json") as fh:
            notes = {note["note_id"]: note for note in json.load(fh)}
    except FileNotFoundError:
        notes = {}
    return notes


def save_notes(notes: dict[str, dict[str, Any]]) -> None:
    with open("output/data/notes.json", "w") as fh:
        json.dump(list(notes.values()), fh)


def get_tweets_with_multi_notes(
    notes: dict[str, dict[str, Any]]
) -> dict[str, list[str]]:
    tweet_to_notes = defaultdict(list)
    for note_id, note in notes.items():
        tweet_to_notes[note["tweet_id"]].append(note_id)

    return {
        tweet_id: note_ids
        for tweet_id, note_ids in tweet_to_notes.items()
        if len(note_ids) > 1
    }
