from flask import Flask, render_template, request, redirect, url_for
from pelitehdas import luo_peli

app = Flask(__name__)

# Tallennetaan pelitilanne globaalisti
peli = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/valitse_peli", methods=["POST"])
def valitse_peli():
    global peli
    valinta = request.form.get("valinta")
    peli = luo_peli(valinta)
    if peli is None:
        return redirect(url_for("index"))
    return redirect(url_for("pelaa"))


@app.route("/pelaa", methods=["GET", "POST"])
def pelaa():
    global peli
    if peli is None:  # Tarkistetaan, onko peli alustettu
        return redirect(url_for("index"))

    if request.method == "POST":
        ensimmaisen_siirto = request.form.get("ensimmaisen_siirto")

        # Tarkistetaan, onko syöte validi
        if not peli._onko_ok_siirto(ensimmaisen_siirto):
            return render_template("pelaa.html", virhe="Virheellinen siirto! Anna k, p tai s.", tulos=str(peli.tuomari))

        # Haetaan toisen pelaajan/tekoälyn siirto
        tokan_siirto = peli._toisen_siirto(ensimmaisen_siirto)
        peli.tuomari.kirjaa_siirto(ensimmaisen_siirto, tokan_siirto)

        # Tarkistetaan, onko peli päättynyt kolmeen voittoon
        if peli.tuomari.ekan_pisteet == 3 or peli.tuomari.tokan_pisteet == 3:
            return render_template("kiitos.html", tulos=str(peli.tuomari))

        return render_template(
            "pelaa.html",
            ensimmaisen_siirto=ensimmaisen_siirto,
            tokan_siirto=tokan_siirto,
            tulos=str(peli.tuomari),
        )
    return render_template("pelaa.html", tulos=str(peli.tuomari))


@app.route("/kiitos")
def kiitos():
    global peli
    return render_template("kiitos.html", tulos=str(peli.tuomari))


if __name__ == "__main__":
    app.run(port=8000)
