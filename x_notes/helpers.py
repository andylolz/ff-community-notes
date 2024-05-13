import csv
import json
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from io import StringIO
from typing import Any, Generator

import requests


def to_isoformat(ms_since_epoch: str) -> str:
    return datetime.fromtimestamp(int(ms_since_epoch[:-3]), timezone.utc).isoformat()


def get_data(date: date, fname: str) -> Generator:
    url_tmpl = f"https://ton.twimg.com/birdwatch-public-data/{{date}}/{fname}/{fname}-00000.tsv"
    url = url_tmpl.format(date=date.strftime("%Y/%m/%d"))
    r = requests.get(url, stream=True)
    r.raise_for_status()

    def _data_generator() -> Generator:
        headers = None
        for line in r.iter_lines():
            cols = next(csv.reader(StringIO(line.decode()), delimiter="\t"))
            if not headers:
                headers = cols
                continue
            yield dict(zip(headers, cols))

    return _data_generator()


def get_generator(fname: str) -> Generator:
    today = date.today()
    try:
        return get_data(today, fname)
    except Exception:
        pass
    yesterday = today - timedelta(days=1)
    return get_data(yesterday, fname)


def load_notes() -> dict[str, dict[str, Any]]:
    try:
        with open("output/data/notes.json") as fh:
            notes = {note["note_id"]: note for note in json.load(fh)}
    except Exception:
        notes = {}
    return notes


def save_notes(notes: dict[str, dict[str, Any]]) -> None:
    with open("output/data/notes.json", "w") as fh:
        json.dump(list(notes.values()), fh)


def save_metadata(notes: dict[str, dict[str, Any]]) -> None:
    with open("output/_data/meta.json", "w") as fh:
        json.dump(
            {
                "scraped_at": datetime.now(timezone.utc).isoformat(),
                "most_recent": list(notes.values())[0]["created_at"],
            },
            fh,
        )


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
