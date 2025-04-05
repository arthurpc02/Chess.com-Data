"""
This code will fetch player data from Chess.com
First I will do a sync code, and then try it async.

URL to get a player's monthly archive:
https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}
or
https://api.chess.com/pub/player/{username}/games/archives

"""

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


if __name__ == '__main__':
    archives = get_archives("arthurpc02")
    print(f"Found {len(archives)} archives.")

    # fetch data from all months:
    for monthly_archive in archives:
        split_date = monthly_archive.split('/')
        print(f"fetching games from {split_date[-1]}/{split_date[-2]}")
        monthly_games = get_games(monthly_archive)
        print(f"  Total games: {len(monthly_games)}.")

        print("    Games' records:")
        for g in monthly_games:
            print(f"      {g["white"]["username"]}[{g["white"]["result"]}] vs {g["black"]["username"]}[{g["black"]["result"]}]: {g["url"]}")