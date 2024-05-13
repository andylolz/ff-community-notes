import asyncio

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from .tweets import fetch_tweets

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_tweets())
