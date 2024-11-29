class TennisGame:

    WRITTEN_SCORES={
        "0": "Love",
        "1": "Fifteen",
        "2": "Thirty",
        "3": "Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        result = ""

        if self.is_score_tied():
            result = self.get_tied_score()

        elif self.is_game_won():
            result = self.get_winner()

        elif self.is_advantage():
            result = self.get_advantage()

        else:
            result = self.get_other_score()

        return result

    def is_score_tied(self):

        return self.player1_score == self.player2_score

    def get_tied_score(self):

        if self.player1_score >= 3:
            return "Deuce"

        player1_written_score = self.WRITTEN_SCORES[str(self.player1_score)]

        return f"{player1_written_score}-All"

    def is_game_won(self):

        if self.is_score_potential_win_or_advantage():
            score_difference = self.get_score_difference()

            return score_difference >= 2

        return False

    def get_winner(self):

        return f"Win for {self.get_leading_player_name()}"

    def is_advantage(self):

        return self.is_score_potential_win_or_advantage() and self.get_score_difference() == 1

    def get_advantage(self):

        return f"Advantage {self.get_leading_player_name()}"

    def is_score_potential_win_or_advantage(self):

        return self.player1_score >= 4 or self.player2_score >= 4

    def get_other_score(self):

        player1_written_score = self.WRITTEN_SCORES[str(self.player1_score)]
        player2_written_score = self.WRITTEN_SCORES[str(self.player2_score)]

        return f"{player1_written_score}-{player2_written_score}"

    def get_score_difference(self):

        return abs(self.player1_score - self.player2_score)

    def is_player1_leading(self):

        return self.player1_score > self.player2_score

    def get_leading_player_name(self):

        if self.player1_score > self.player2_score:
            return self.player1_name

        return self.player2_name
