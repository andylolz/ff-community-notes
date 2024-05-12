import asyncio

from .tweets import fetch_tweets

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_tweets())
