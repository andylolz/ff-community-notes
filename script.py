import csv
from datetime import datetime, date, timedelta
from io import StringIO
import re
import requests


url_re = re.compile(r"(https?://[^\s]+)")


def to_isoformat(ms_since_epoch):
    return str(datetime.utcfromtimestamp(int(ms_since_epoch[:-3])))


def urlize(inp):
    return url_re.sub(r'<a target="_blank" href="\1">\1</a>', inp)


reasons = {
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
def get_reasons(row):
    return ", ".join([
        v for k, v in reasons.items()
        if bool(int(row[k]))
    ])


def get_data(date):
    url_tmpl = "https://ton.twimg.com/birdwatch-public-data/{date}/notes/notes-00000.tsv"
    url = url_tmpl.format(date=date.strftime("%Y/%m/%d"))
    r = requests.get(url, stream=True)
    r.raise_for_status()

    def _data_generator():
        headers = None
        for line in r.iter_lines():
            cols = next(csv.reader(StringIO(line.decode()), delimiter="\t"))
            if not headers:
                headers = cols
                continue
            yield dict(zip(headers, cols))

    return _data_generator()


def get_generator():
    today = date.today()
    try:
        return get_data(today)
    except Exception:
        pass
    yesterday = today - timedelta(days=1)
    return get_data(yesterday)


with open("output/_data/notes.csv", "w") as fh:
    writer = None
    for row in get_generator():
        if "fullfact" not in row["summary"].lower():
            # filter out non-fullfact stuff
            continue
        output = {
            "tweet_id": row["tweetId"],
            "note_id": row["noteId"],
            "note_author_id": row["noteAuthorParticipantId"],
            "classification": row["classification"].replace("_", " ").lower().capitalize(),
            "reasons": get_reasons(row),
            "summary": urlize(row["summary"]),
            "trustworthy_source": bool(row["trustworthySources"]),
            "created_at": to_isoformat(row["createdAtMillis"]),
        }
        if not writer:
            writer = csv.DictWriter(fh, fieldnames=output.keys())
            writer.writeheader()
        _ = writer.writerow(output)
