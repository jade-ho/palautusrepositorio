import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_top_scorers_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 pistettä
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 pistettä
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 pistettä
    def test_top_scorers_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")  # 45 maalia
        self.assertEqual(top_players[1].name, "Yzerman")  # 42 maalia
        self.assertEqual(top_players[2].name, "Kurri")    # 37 maalia

    def test_top_scorers_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 89 syöttöä
        self.assertEqual(top_players[1].name, "Yzerman")  # 56 syöttöä
        self.assertEqual(top_players[2].name, "Lemieux")  # 54 syöttöä

    def test_top_scorers_default(self):
        top_players = self.stats.top(3)  # Oletuksena pisteet
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_with_invalid_sort(self):
        with self.assertRaises(ValueError):
            self.stats.top(3, "INVALID_SORT")

    def test_top_with_empty_player_list(self):
        class EmptyPlayerReaderStub:
            def get_players(self):
                return []

        empty_stats = StatisticsService(EmptyPlayerReaderStub())
        top_players = empty_stats.top(3)
        self.assertEqual(len(top_players), 0)

    def test_sort_by_points_with_empty_list(self):
        class EmptyPlayerReaderStub:
            def get_players(self):
                return []

        empty_stats = StatisticsService(EmptyPlayerReaderStub())
        top_players = empty_stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 0)