
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirrot(self, siirrot):
        pelaaja1_siirto = siirrot["pelaaja1"]
        pelaaja2_siirto = siirrot["pelaaja2"]
        
        if self._tasapeli(pelaaja1_siirto, pelaaja2_siirto):
            self.tasapelit = self.tasapelit + 1
        elif self._eka_voittaa(pelaaja1_siirto, pelaaja2_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
        else:
            self.tokan_pisteet = self.tokan_pisteet + 1

    def __str__(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"

    # sisäinen metodi, jolla tarkastetaan tuliko tasapeli
    def _tasapeli(self, pelaaja1_siirto, pelaaja2_siirto):
        return pelaaja1_siirto == pelaaja2_siirto

    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _eka_voittaa(self, pelaaja1_siirto, pelaaja2_siirto):
        if pelaaja1_siirto == "k" and pelaaja2_siirto== "s":
            return True
        elif pelaaja1_siirto == "s" and pelaaja2_siirto == "p":
            return True
        elif pelaaja1_siirto == "p" and pelaaja2_siirto == "k":
            return True

        return False
