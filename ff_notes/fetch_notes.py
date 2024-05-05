import csv
from datetime import datetime, timedelta
import re
from .helpers import to_isoformat, get_generator


url_re = re.compile(r"(https?://[^\s]+)")
one_week_ago = datetime.now() - timedelta(days=7)


def urlize(inp: str) -> str:
    return url_re.sub(r'<a target="_blank" href="\1">\1</a>', inp)


def pp_key(key: str) -> str:
    return key.replace("_", " ").lower().capitalize()


reasons_lookup = {
    "misleadingOther": "Other",
    "misleadingFactualError": "Factual error",
    "misleadingManipulatedMedia": "Manipulated media",
    "misleadingOutdatedInformation": "Outdated information",
    "misleadingMissingImportantContext": "Missing important context",
    "misleadingUnverifiedClaimAsFact": "Unverified claim as fact",
    "misleadingSatire": "Satire",
    "notMisleadingOther": "Other",
    "notMisleadingFactuallyCorrect": "Factually correct",
    "notMisleadingOutdatedButNotWhenWritten": "Outdated (but not when written)",
    "notMisleadingClearlySatire": "Clearly satire",
    "notMisleadingPersonalOpinion": "Personal opinion",
}


if __name__ == "__main__":
    with open("output/_data/notes.csv", "w") as fh:
        writer = None
        for row in get_generator():
            created_at = to_isoformat(row["createdAtMillis"])
            if created_at < one_week_ago:
                continue
            classification = pp_key(row["classification"])
            reasons = ", ".join(
                [v for k, v in reasons_lookup.items() if bool(int(row[k]))]
            )
            output = {
                "tweet_id": row["tweetId"],
                "note_id": row["noteId"],
                "note_author_id": row["noteAuthorParticipantId"],
                "classification": classification,
                "reasons": reasons,
                "summary": urlize(row["summary"]),
                "created_at": str(created_at),
            }
            if not writer:
                writer = csv.DictWriter(fh, fieldnames=output.keys())
                writer.writeheader()
            _ = writer.writerow(output)