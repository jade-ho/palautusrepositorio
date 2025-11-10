from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader

def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt")
    )

    print("Top point getters:")
    for player in stats.top(5, SortBy.POINTS):
        print(player)

    print()
    for player in stats.top(5):
        print(player)

    print("Top point goal scorers:")
    for player in stats.top(5, SortBy.GOALS):
        print(player)

    print("Top by assists:")
    for player in stats.top(5, SortBy.ASSISTS):
        print(player)

if __name__ == "__main__":
    main()
