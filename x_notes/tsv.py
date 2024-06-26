import csv
from datetime import date, timedelta
from io import StringIO
from typing import Generator

import requests


def get_data(date: date, fname: str, index: int = 0) -> Generator:
    url_tmpl = (
        f"https://ton.twimg.com/birdwatch-public-data/{{date}}/{fname}-{index:05d}.tsv"
    )
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


def get_generator(fname: str, index: int = 0) -> Generator:
    today = date.today()
    try:
        return get_data(today, fname, index)
    except Exception:
        pass
    yesterday = today - timedelta(days=1)
    return get_data(yesterday, fname, index)
