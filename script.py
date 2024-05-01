from io import StringIO
import csv
from datetime import datetime, date, timedelta
import requests


def to_isoformat(ms_since_epoch):
    return str(datetime.utcfromtimestamp(int(ms_since_epoch) / 1000))


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


with open("output/data.csv", "w") as fh:
    writer = None
    for row in get_generator():
        if "fullfact" in row["summary"].lower():
            row["createdAt"] = to_isoformat(row["createdAtMillis"])
            del row["createdAtMillis"]
            if not writer:
                writer = csv.DictWriter(fh, fieldnames=row.keys())
                writer.writeheader()
            _ = writer.writerow(row)
