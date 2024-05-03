import csv
from datetime import date, datetime, timedelta
from io import StringIO
import requests
from typing import Generator


def to_isoformat(ms_since_epoch: str) -> str:
    return str(datetime.utcfromtimestamp(int(ms_since_epoch[:-3])))


def get_data(date: date, fname: str) -> Generator:
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


def get_generator(fname: str = "notes") -> Generator:
    today = date.today()
    try:
        return get_data(today, fname)
    except Exception:
        pass
    yesterday = today - timedelta(days=1)
    return get_data(yesterday, fname)
