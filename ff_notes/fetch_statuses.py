import csv
import json
from .helpers import get_generator, to_datetime


helpful = "CURRENTLY_RATED_HELPFUL"
unhelpful = "CURRENTLY_RATED_NOT_HELPFUL"


note_statuses = {}

if __name__ == "__main__":
    with open("output/_data/notes.csv") as fh:
        all_note_ids = [row["note_id"] for row in csv.DictReader(fh)]

    for row in get_generator("noteStatusHistory"):
        note_status = {}
        if row["noteId"] not in all_note_ids:
            continue
        if row["currentStatus"] == unhelpful:
            # this is currently rated unhelpful,
            # so we’ll exclude it
            note_status["status"] = "unhelpful"
        else:
            if (
                row["firstNonNMRStatus"] != helpful
                and row["mostRecentNonNMRStatus"] != helpful
            ):
                continue
            if row["firstNonNMRStatus"] == helpful:
                from_ts = to_datetime(row["timestampMillisOfFirstNonNMRStatus"])
            else:
                from_ts = to_datetime(row["timestampMillisOfLatestNonNMRStatus"])
            note_status["from"] = from_ts.isoformat()
            if row["currentStatus"] != helpful:
                # this timestamp often doesn’t appear to be useful.
                # I suspect because there are cases where the status
                # is disputed, so the current status changes frequently
                note_status["to"] = to_datetime(
                    row["timestampMillisOfCurrentStatus"]
                ).isoformat()
        note_statuses[row["noteId"]] = note_status


with open("output/_data/statuses.json", "w") as fh:
    json.dump(note_statuses, fh)
