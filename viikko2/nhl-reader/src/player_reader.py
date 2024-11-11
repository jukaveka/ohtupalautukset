import requests
from player import Player

class PlayerReader():

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url).json()
        self.players = [Player(player_dict) for player_dict in self.response]
