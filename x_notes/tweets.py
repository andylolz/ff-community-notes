import asyncio
import csv
import json
from os import environ
from os.path import exists
from twscrape import API


async def fetch_tweets():
    with open("output/_data/notes.csv") as fh:
        all_tweet_ids = [row["tweet_id"] for row in csv.DictReader(fh)]

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
    await api.pool.add_account(**account_kwargs)
    await api.pool.login_all()

    account = await api.pool.get(account_kwargs["username"])
    environ["COOKIES"] = json.dumps(account.cookies)

    for tweet_id in all_tweet_ids:
        tweet_fpath = f"output/_data/tweet-{tweet_id}.json"
        if exists(tweet_fpath):
            continue
        tweet = await api.tweet_details(int(tweet_id))
        if tweet:
            tweet = tweet.json()
        else:
            tweet = ""
        with open(tweet_fpath, "w") as fh:
            fh.write(tweet)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_tweets())
