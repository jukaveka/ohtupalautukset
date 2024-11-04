import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_correct_search_works(self):
        player = self.stats.search("Gretzky")

        self.assertAlmostEqual(player.name, "Gretzky")

    def test_incorrect_search_works(self):
        player = self.stats.search("Tikkanen")

        self.assertEqual(player, None)

    def test_correct_team_search(self):
        team = self.stats.team("PIT")

        for player in team:
            name = player.name

        self.assertEqual(name, "Lemieux")
    
    def test_top_scorer_player_amount(self):
        list = self.stats.top(3)

        self.assertAlmostEqual(len(list), 4)