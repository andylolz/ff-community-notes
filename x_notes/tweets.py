import json
from os import environ
from twscrape import API
from .github import update_secret
from .helpers import load_notes


async def fetch_tweets():
    notes = load_notes()

    account_kwargs = {
        "username": environ["USER"],
        "password": environ["PASS"],
        "email": environ["EMAIL"],
        "email_password": "",
    }
    cookies = environ.get("COOKIES")
    if cookies:
        account_kwargs["cookies"] = json.loads(cookies)
    proxy = environ.get("PROXY")
    if proxy:
        account_kwargs["proxy"] = proxy

    api = API()
    try:
        await api.pool.add_account(**account_kwargs)
    except ValueError:
        # cookie is stale. Delete it and retry
        del account_kwargs["cookies"]
        await api.pool.add_account(**account_kwargs)
    await api.pool.login_all()

    account = await api.pool.get(account_kwargs["username"])
    if environ.get("UPDATE_SECRET"):
        print("Updating secret ...")
        update_secret("COOKIES", json.dumps(account.cookies))

    note_ids = list(notes.keys())
    for note_id in note_ids:
        note = notes[note_id]
        if "tweet" in note:
            continue
        try:
            tweet = await api.tweet_details(int(note["tweet_id"]))
        except Exception as e:
            print(e)
            break
        if tweet:
            note["lang"] = tweet.lang
            note["content"] = tweet.rawContent
        else:
            note["lang"] = None
            note["content"] = None
        notes[note_id] = note

    with open("static/data/notes.json", "w") as fh:
        json.dump(list(notes.values()), fh)
