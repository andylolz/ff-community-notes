import csv
from datetime import datetime, date, timedelta
from io import StringIO
import json
import re
import requests
from typing import Generator, Tuple


url_re = re.compile(r"(https?://[^\s]+)")


def to_isoformat(ms_since_epoch: str) -> str:
    return str(datetime.utcfromtimestamp(int(ms_since_epoch[:-3])))


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


def get_data(date: date, fname: str = "notes") -> Generator:
    url_tmpl = f"https://ton.twimg.com/birdwatch-public-data/{{date}}/{fname}/{fname}-00000.tsv"
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


def get_generator() -> Tuple[date, Generator]:
    today = date.today()
    try:
        return today, get_data(today)
    except Exception:
        pass
    yesterday = today - timedelta(days=1)
    return yesterday, get_data(yesterday)


all_note_ids = []
with open("output/_data/notes.csv", "w") as fh:
    writer = None
    latest_data_date, generator = get_generator()
    for row in generator:
        if "fullfact" not in row["summary"].lower():
            # filter out non-fullfact stuff
            continue
        all_note_ids.append(row["noteId"])
        classification = pp_key(row["classification"])
        reasons = ", ".join([v for k, v in reasons_lookup.items() if bool(int(row[k]))])
        output = {
            "tweet_id": row["tweetId"],
            "note_id": row["noteId"],
            "note_author_id": row["noteAuthorParticipantId"],
            "classification": classification,
            "reasons": reasons,
            "summary": urlize(row["summary"]),
            "trustworthy_source": bool(row["trustworthySources"]),
            "created_at": to_isoformat(row["createdAtMillis"]),
        }
        if not writer:
            writer = csv.DictWriter(fh, fieldnames=output.keys())
            writer.writeheader()
        _ = writer.writerow(output)


helpful = "CURRENTLY_RATED_HELPFUL"
started = False
with open("output/_data/statuses.json", "w") as fh:
    fh.write("{")
    for row in get_data(latest_data_date, "noteStatusHistory"):
        if row["noteId"] not in all_note_ids:
            continue
        if row["firstNonNMRStatus"] != helpful and row["mostRecentNonNMRStatus"] != helpful:
            continue
        if started:
            fh.write(",")
        fh.write(f'"{row["noteId"]}":')
        if row["firstNonNMRStatus"] == helpful:
            from_ts = to_isoformat(row["timestampMillisOfFirstNonNMRStatus"])
        else:
            from_ts = to_isoformat(row["timestampMillisOfLatestNonNMRStatus"])
        output = {
            "from": from_ts,
        }
        if row["currentStatus"] != helpful:
            # this timestamp doesn’t appear to be correct… Possibly it’s updated very frequently
            output["to"] = to_isoformat(row["timestampMillisOfCurrentStatus"]),
        fh.write(json.dumps(output))
        started = True
    fh.write("}")
