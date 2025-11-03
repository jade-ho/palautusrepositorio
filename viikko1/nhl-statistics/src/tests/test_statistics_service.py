import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),    # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),   # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)    # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_top_scorers_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # Eniten pisteitä
        self.assertEqual(top_players[1].name, "Lemieux")  # Toinen eniten
        self.assertEqual(top_players[2].name, "Yzerman")  # Kolmas eniten

    def test_top_scorers_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")  # Eniten maaleja
        self.assertEqual(top_players[1].name, "Yzerman")  # Toinen eniten
        self.assertEqual(top_players[2].name, "Kurri")    # Kolmas eniten

    def test_top_scorers_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # Eniten syöttöjä
        self.assertEqual(top_players[1].name, "Yzerman")  # Toinen eniten
        self.assertEqual(top_players[2].name, "Lemieux")   # Kolmas eniten

    def test_top_scorers_default(self):
        top_players = self.stats.top(3)  # Ilman toista argumenttia
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # Eniten pisteitä
        self.assertEqual(top_players[1].name, "Lemieux")  # Toinen eniten
        self.assertEqual(top_players[2].name, "Yzerman")  # Kolmas eniten

    def test_top_with_invalid_sort(self):
        with self.assertRaises(ValueError):
            self.stats.top(3, "INVALID_SORT")  # Testaa virheellistä sorttausta

    def test_top_with_empty_player_list(self):
        class EmptyPlayerReaderStub:
            def get_players(self):
                return []  # Tyhjät pelaajat

        empty_stats = StatisticsService(EmptyPlayerReaderStub())
        top_players = empty_stats.top(3)
        self.assertEqual(len(top_players), 0)  # Odotetaan, että ei pelaajia

    def test_sort_by_points_with_empty_list(self):
        class EmptyPlayerReaderStub:
            def get_players(self):
                return []  # Tyhjät pelaajat

        empty_stats = StatisticsService(EmptyPlayerReaderStub())
        top_players = empty_stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 0)  # Odotetaan, että ei pelaajia