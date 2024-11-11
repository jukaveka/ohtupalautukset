class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.games = dict['games']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name + ' ' * (22 - len(self.name)) + self.team + ' ' * (4 - len(str(self.goals))) + str(self.goals) + ' +' + ' ' * (3 - len(str(self.assists))) + str(self.assists) + ' =' + ' ' * (4 - len(str(self.points))) + str(self.points)}"