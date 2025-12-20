from tuomari import Tuomari


class KiviPaperiSakset:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            # Päätetään peli, kun toinen pelaajista saavuttaa kolme voittoa
            if self.tuomari.ekan_pisteet == 3 or self.tuomari.tokan_pisteet == 3:
                break

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        raise NotImplementedError

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]
