import pytest
from app import app
from unittest.mock import patch


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Tervetuloa pelaamaan Kivi-Paperi-Sakset!" in response.data


def test_valitse_peli(client):
    response = client.post("/valitse_peli", data={"valinta": "b"})
    assert response.status_code == 302  # Redirect to /pelaa


def test_pelaa_invalid_input(client):
    client.post("/valitse_peli", data={"valinta": "b"})
    response = client.post("/pelaa", data={"ensimmaisen_siirto": "x"})
    assert b"Virheellinen siirto! Anna k, p tai s." in response.data


def test_pelaa_valid_input(client):
    client.post("/valitse_peli", data={"valinta": "b"})
    response = client.post("/pelaa", data={"ensimmaisen_siirto": "k"})
    assert b"1. pelaajan siirto: k" in response.data
    assert b"2. pelaajan siirto:" in response.data


def test_pelaa_until_three_wins(client):
    client.post("/valitse_peli", data={"valinta": "b"})
    # Mockataan tekoälyn siirrot niin, että ne aina häviävät ensimmäisen pelaajan siirroille
    with patch("tekoaly.Tekoaly.anna_siirto", side_effect=["s", "s", "s"]):
        for _ in range(3):
            response = client.post(
                "/pelaa", data={"ensimmaisen_siirto": "k"})  # "k" voittaa "s"
            assert b"Pelitilanne:" in response.data
        response = client.get("/kiitos")
        assert b"Kiitos pelaamisesta!" in response.data
        assert b"Pelitilanne: 3 - 0" in response.data
