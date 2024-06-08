import json
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

from loguru import logger


def to_isoformat(ms_since_epoch: str) -> str:
    return datetime.fromtimestamp(int(ms_since_epoch[:-3]), timezone.utc).isoformat()


def load_notes() -> dict[str, dict[str, Any]]:
    fn = "output/data/notes.json"
    notes = {}
    try:
        with open(fn) as fh:
            noted_tweets = json.load(fh)
    except FileNotFoundError:
        logger.warning(f"File not found: {fn}")
        return notes
    for noted_tweet in noted_tweets:
        tweet = {
            k: noted_tweet[k]
            for k in ["deleted", "dl", "lang", "rating", "tweet", "tweet_id", "user"]
            if k in noted_tweet
        }
        for note in noted_tweet["notes"]:
            notes[note["note_id"]] = {**note, **tweet}
    return notes


def save_notes(notes: dict[str, dict[str, Any]]) -> None:
    noted_tweets = {}
    for note in notes:
        if note["tweet_id"] not in noted_tweets:
            noted_tweets[note["tweet_id"]] = {
                k: note[k]
                for k in [
                    "deleted",
                    "dl",
                    "lang",
                    "rating",
                    "tweet",
                    "tweet_id",
                    "user",
                ]
                if k in note
            }
            noted_tweets[note["tweet_id"]]["notes"] = []
        noted_tweets[note["tweet_id"]]["notes"].append(
            {
                k: note[k]
                for k in [
                    "created_at",
                    "note_id",
                    "reasons",
                    "removed",
                    "shown",
                    "summary",
                ]
                if k in note
            }
        )
        noted_tweets[note["tweet_id"]]["notes"].sort(
            key=lambda x: x["created_at"],
            reverse=True,
        )
    with open("output/data/notes.json", "w") as fh:
        json.dump(list(noted_tweets.values()), fh)


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
