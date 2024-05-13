import json
from os import environ
from typing import Any

from loguru import logger
from twscrape import API, NoAccountError

from .github import update_secret
from .helpers import get_tweets_with_multi_notes, load_notes, save_notes


def get_next_unfetched_note(notes: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    return next((note for note in notes.values() if "dl" not in note), None)


def log_stats(notes: dict[str, dict[str, Any]]) -> None:
    total_notes = len(notes)
    total_unfetched = len([1 for note in notes.values() if "dl" not in note])
    logger.info(f"Total notes: {total_notes}")
    logger.info(f"Total to be fetched: {total_unfetched}")


async def login() -> API:
    api = API(
        proxy=environ.get("TW_PROXY"),
        raise_when_no_account=True,
    )

    username = environ["TW_USER"]
    account_kwargs = {
        "username": username,
        "password": environ["TW_PASS"],
        "email": environ["TW_EMAIL"],
        "email_password": "",
    }
    cookies = environ.get("TW_COOKIES")
    if cookies:
        logger.info("Cookie found. No need to log in")
        account_kwargs["cookies"] = cookies

    await api.pool.add_account(**account_kwargs)
    if not cookies:
        logger.info("Attempting to log in")
        await api.pool.login_all()
        account = await api.pool.get(username)
        if environ.get("UPDATE_SECRET"):
            logger.info("Updating secret ...")
            update_secret("COOKIES", json.dumps(account.cookies))
    return api


async def fetch_tweets() -> None:
    notes = load_notes()
    if not get_next_unfetched_note(notes):
        logger.info("No tweets to fetch")
        return

    tweets_with_multi_notes = get_tweets_with_multi_notes(notes)

    api = await login()

    total_fetched = 0
    while True:
        note = get_next_unfetched_note(notes)
        if not note:
            logger.info("No more tweets to fetch")
            break
        note_id = note["note_id"]
        try:
            tweet = await api.tweet_details(int(note["tweet_id"]))
        except NoAccountError:
            logger.info("Rate limited – giving up")
            break
        account = await api.pool.get(environ["TW_USER"])
        if not account.active:
            logger.info("Failed to fetch tweet")
            if environ.get("TW_COOKIES"):
                await api.pool.delete_inactive()
                del environ["TW_COOKIES"]
                api = await login()
            continue
        note_update = {
            "dl": 1,
        }
        total_fetched += 1
        if tweet:
            note_update["lang"] = tweet.lang
            note_update["user"] = tweet.user.username
            note_update["tweet"] = tweet.rawContent
        else:
            note_update["deleted"] = 1
        for update_note_id in tweets_with_multi_notes.get(note["tweet_id"], [note_id]):
            notes[update_note_id] = {**note, **note_update}

    if total_fetched == 0:
        raise Exception("Failed to fetch any tweets")

    logger.info(f"Total tweets fetched: {total_fetched}")
    log_stats(notes)

    save_notes(notes)
