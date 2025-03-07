import requests
from dotenv import load_dotenv
import os

load_dotenv()

steam_key = os.getenv("STEAM_KEY")

request = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_key}&steamid=76561197960434622&format=json")

print(request)
