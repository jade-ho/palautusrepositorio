from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top(self, how_many, sort_by=SortBy.POINTS):
        def sort_key(player):
            if sort_by == SortBy.POINTS:
                return player.points
            elif sort_by == SortBy.GOALS:
                return player.goals
            elif sort_by == SortBy.ASSISTS:
                return player.assists
            else:
                raise ValueError("Unknown sort criteria")

        sorted_players = sorted(self._players, key=sort_key, reverse=True)

        return sorted_players[:how_many]  # Palautetaan haluttu määrä pelaajia