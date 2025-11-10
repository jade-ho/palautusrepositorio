'''
A program that fetches NHL player data and displays the top Finnish players.
'''
import requests
from rich.console import Console
from rich.table import Table
from player import Player

def main():
    '''
    Main function to fetch and display top Finnish NHL players.
    '''
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    players = fetch_players(url)
    display_players(players)

def fetch_players(url):
    '''
    Fetches player data from the given URL and returns top Finnish players.
    '''
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality("FIN")

def display_players(players):
    '''
    Displays the list of players in a formatted table.
    '''
    console = Console()
    table = Table(title="Finnish players")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

    console.print(table)

class PlayerReader:
    '''
    A class to read player data from a given URL.
    '''
    def __init__(self, url):
        self.url = url

    def get_players(self):
        '''
        Fetches player data from the URL and returns a list of Player objects.
        '''
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players

class PlayerStats:
    '''
    A class to analyze player statistics.
    '''
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        '''
        Fetches players by nationality and sorts them by total points (goals + assists).
        '''

        filtered_players = [player for player in self.players if player.nationality == nationality]
        sorted_players = sorted(filtered_players, key=lambda player: player.goals + player.assists, reverse=True)
        return sorted_players

if __name__ == "__main__":
    main()
