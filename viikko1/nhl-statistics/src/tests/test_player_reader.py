import unittest
from unittest.mock import patch, MagicMock
from player_reader import PlayerReader
from player import Player

class TestPlayerReader(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_players_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.__iter__.return_value = [
            b"Wayne Gretzky;EDM;1;35;89\n",
            b"Mario Lemieux;PIT;2;45;54\n",
            b"Jari Kurri;EDM;3;37;53\n",
        ]
        mock_urlopen.return_value = mock_response

        reader = PlayerReader("http://test.url")  # Tämä rivi käyttää konstruktoriparametria
        players = reader.get_players()

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Wayne Gretzky")
        self.assertEqual(players[1].name, "Mario Lemieux")
        self.assertEqual(players[2].name, "Jari Kurri")

    @patch('urllib.request.urlopen')
    def test_get_players_empty(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.__iter__.return_value = []
        mock_urlopen.return_value = mock_response

        reader = PlayerReader("http://test.url")  # Tämä rivi käyttää konstruktoriparametria
        players = reader.get_players()

        self.assertEqual(len(players), 0)