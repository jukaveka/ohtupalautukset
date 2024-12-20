from tuomari import Tuomari

VALIDIT_SIIRROT = ["k", "p", "s"]

class KiviPaperiSakset:
    def __init__(self, tekoaly=None):
        self._tekoaly = tekoaly

    def pelaa(self):
        tuomari = Tuomari()

        siirrot = self._pyyda_siirrot()

        while self._onko_siirrot_ok(siirrot):
            tuomari.kirjaa_siirrot(siirrot)
            print(tuomari)

            if self._pelaaja2_on_tekoaly():
                print(f'Tietokone valitsi: {siirrot["pelaaja2"]}')
                self._tekoaly.aseta_siirto(siirrot["pelaaja1"])
            
            siirrot = self._pyyda_siirrot()

        print("Kiitos")
        print(tuomari)

    def _pyyda_siirrot(self):
        siirrot = {}

        siirrot["pelaaja1"] = self._ekan_siirto()
        siirrot["pelaaja2"] = self._tokan_siirto(siirrot["pelaaja1"])

        return siirrot

    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    def _tokan_siirto(self, pelaaja1_siirto):
        return 0

    def _onko_siirrot_ok(self, siirrot):
        return siirrot["pelaaja1"] in VALIDIT_SIIRROT and siirrot["pelaaja2"] in VALIDIT_SIIRROT
    
    def ohje(self):
        return "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
    
    def _pelaaja2_on_tekoaly(self):
        return self._tekoaly