"""
This code will fetch player data from Chess.com
First I will do a sync code, and then try it async.

URL to get a player's monthly archive:
https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}
or
https://api.chess.com/pub/player/{username}/games/archives

"""

import requests

HEADERS = {
    "User-Agent": "MyChessApp/0.1 (contact: arthurpc02@gmail.com)"
}

def get_games_by_month_year(player_name: str, month: str, year: str):

    print(f'Get games by month and year')

def get_archives(username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    return data["archives"]

if __name__ == '__main__':
    # get_games_by_month_year('arthurpc02', '11', '2023')

    archives = get_archives("arthurpc02")
    print(f"Found {len(archives)} archives.")



