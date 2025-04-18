"""
This code will fetch player data from Chess.com
First I will do a sync code, and then try it async.

URL to get a player's monthly archive:
https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}
or
https://api.chess.com/pub/player/{username}/games/archives

"""
import time

import requests
import json
import asyncio
import aiohttp

from execution_timer import timer, async_timer

HEADERS = {
    "User-Agent": "MyChessApp/0.1 (contact: arthurpc02@gmail.com)"
}

async def get_archives(session, username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    async with session.get(url, headers=HEADERS) as response:
        response.raise_for_status()
        data = await response.json()
        # print(json.dumps(data, indent=2))
        return data["archives"]


async def get_games(session, archive_url):
    async with session.get(archive_url, headers=HEADERS) as response:
        response.raise_for_status()
        data = await response.json()
        # print(json.dumps(response.json(), indent=2))
        return data["games"]


async def get_all_games_from_all_months(session, all_archives: list[str]):
    tasks = [get_games(session, archive_url) for archive_url in all_archives]
    all_monthly_games = await asyncio.gather(*tasks)
    return [game for monthly in all_monthly_games for game in monthly]


@async_timer
async def main():
    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        archives = await get_archives(session, "arthurpc02") #Tricky_Dicky, Hikaru
        print(f"Found {len(archives)} archives.")
        all_games = await get_all_games_from_all_months(session, archives)

    end_time = time.perf_counter()

    for g in all_games:
        print(f"{g["white"]["username"]}[{g["white"]["result"]}] vs {g["black"]["username"]}[{g["black"]["result"]}]: {g["url"]}")


if __name__ == '__main__':
    asyncio.run(main())

