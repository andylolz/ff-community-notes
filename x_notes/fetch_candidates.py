import csv
import json
from io import StringIO

import requests

dc_csv = "https://candidates.democracyclub.org.uk/data/export_csv/?election_date=&ballot_paper_id=&election_id=parl.2024-07-04&party_id=&cancelled=&has_twitter_username=yes&extra_fields=twitter_username&format=csv"

r = requests.get(dc_csv, stream=True)
data = list(csv.DictReader(StringIO(r.text)))
handles = [row["twitter_username"].replace('"', "") for row in data]

with open("output/data/ge2024-candidates.json", "w") as fh:
    json.dump(handles, fh)
