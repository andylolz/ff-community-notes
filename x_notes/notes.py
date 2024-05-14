import re
from datetime import datetime, timedelta, timezone
from typing import Any

from .helpers import to_isoformat
from .tsv import get_generator

url_re = re.compile(r"(https?://[^\s]+)")
one_week_ago = (datetime.now(timezone.utc) - timedelta(days=7)).timestamp()


def urlize(inp: str) -> str:
    return url_re.sub(r'<a target="_blank" href="\1">\1</a>', inp)


reasons_lookup = {
    "misleadingOther": "Other",
    "misleadingFactualError": "Factual error",
    "misleadingManipulatedMedia": "Manipulated media",
    "misleadingOutdatedInformation": "Outdated information",
    "misleadingMissingImportantContext": "Missing important context",
    "misleadingUnverifiedClaimAsFact": "Unverified claim as fact",
    "misleadingSatire": "Satire",
    # "notMisleadingOther": "Other",
    # "notMisleadingFactuallyCorrect": "Factually correct",
    # "notMisleadingOutdatedButNotWhenWritten": "Outdated (but not when written)",
    # "notMisleadingClearlySatire": "Clearly satire",
    # "notMisleadingPersonalOpinion": "Personal opinion",
}


def get_notes(notes: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    notes_by_tweet_id = {
        note["tweet_id"]: note for note in notes.items() if "dl" in note
    }
    notes = {
        k: v
        for k, v in notes.items()
        if datetime.fromisoformat(v["created_at"]).timestamp() >= one_week_ago
    }
    for row in get_generator("notes"):
        note_id = row["noteId"]
        created_at = to_isoformat(row["createdAtMillis"])
        if float(row["createdAtMillis"]) / 1000 < one_week_ago:
            # exclude old notes
            continue
        if row["classification"] == "NOT_MISLEADING":
            # exclude "not misleading" notes
            if note_id in notes:
                del notes[note_id]
            continue
        reasons = ", ".join([v for k, v in reasons_lookup.items() if bool(int(row[k]))])
        note = notes.get(note_id, {})
        note.update(
            {
                "tweet_id": row["tweetId"],
                "note_id": note_id,
                # "note_author_id": row["noteAuthorParticipantId"],
                "reasons": reasons,
                "summary": urlize(row["summary"]),
                "created_at": created_at,
            }
        )
        if "dl" not in note and note["tweet_id"] in notes_by_tweet_id:
            tweet_note = notes_by_tweet_id[note["tweet_id"]]
            for k in ["dl", "deleted", "lang", "user", "tweet"]:
                if k in tweet_note:
                    note[k] = tweet_note[k]
        notes[note_id] = note
    return notes
