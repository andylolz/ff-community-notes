import csv
import json
from helpers import get_generator, to_isoformat


if __name__ == "__main__":
    with open("output/_data/notes.csv") as fh:
        all_note_ids = [row["note_id"] for row in csv.DictReader(fh)]

    helpful = "CURRENTLY_RATED_HELPFUL"
    started = False
    with open("output/_data/statuses.json", "w") as fh:
        fh.write("{")
        for row in get_generator("noteStatusHistory"):
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
                # this timestamp often doesn’t appear to be useful.
                # I suspect because there are cases where the status is disputed,
                # so the current status changes frequently
                output["to"] = to_isoformat(row["timestampMillisOfCurrentStatus"]),
            fh.write(json.dumps(output))
            started = True
        fh.write("}")
