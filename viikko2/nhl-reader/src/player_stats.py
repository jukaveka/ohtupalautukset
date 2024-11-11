from player import Player

class PlayerStats():

    def __init__(self, data):
        self.data = data

    def top_scorers_by_nationality(self, nationality):
        nationality_players = sorted([player for player in self.data.players if player.nationality == nationality], key=lambda x: x.points, reverse=True)

        return nationality_players