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

HEADERS = {
    "User-Agent": "MyChessApp/0.1 (contact: arthurpc02@gmail.com)"
}

def get_archives(username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    # print(json.dumps(data, indent=2))
    return data["archives"]


def get_games(archive_url):
    response = requests.get(archive_url, headers=HEADERS)
    response.raise_for_status()
    # print(json.dumps(response.json(), indent=2))
    return response.json()["games"]


def get_all_games_from_all_months(all_archives: list[str]):
    all_games = []
    for archive in all_archives:
        games_monthly = get_games(archive)
        for games in games_monthly:
            all_games.append(games)
    return all_games


if __name__ == '__main__':
    start_time = time.perf_counter()

    archives = get_archives("arthurpc02")
    print(f"Found {len(archives)} archives.")

    all_games = get_all_games_from_all_months(archives)
    end_time = time.perf_counter()

    for g in all_games:
        print(f"{g["white"]["username"]}[{g["white"]["result"]}] vs {g["black"]["username"]}[{g["black"]["result"]}]: {g["url"]}")


    print("\n##########")
    print(f"I/O tasks total time: {end_time-start_time:.2f} seconds.")
