from urllib import request
from player import Player

class PlayerReader:
    def __init__(self, url):  # Muutettu init -> init
        self._url = url

    def get_players(self):
        players = []
        players_file = request.urlopen(self._url)
        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 4:  # Tarkista, että tarvittavat tiedot ovat saatavilla
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )
                players.append(player)
        return players