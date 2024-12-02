KAPASITEETTI = 5
OLETUSKASVATUS = 5

vakioarvot = {
    "kapasiteetti": KAPASITEETTI,
    "kasvatuskoko": OLETUSKASVATUS
}

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        
        self.kapasiteetti = self.kasittele_syote(kapasiteetti, "kapasiteetti")
        self.kasvatuskoko = self.kasittele_syote(kasvatuskoko, "kasvatuskoko")
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku: int):

        return luku in self.lukujono

    def lisaa(self, luku):

        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.kasvata_alkioiden_lukumaaraa()

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.lista_taynna():
                self.luo_uusi_lista()

    def poista(self, luku):
        
        self.lukujono.remove(luku)
        self.vahenna_alkioiden_lukumaaraa()

    def kopioi_lista(self, alkuperainen: list, kopio: list):
 
        for i in range(0, self.alkioiden_lkm):
            kopio[i] = alkuperainen[i]

    def mahtavuus(self):

        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        self.kopioi_lista(self.lukujono, taulu)

        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):

        yhdiste = IntJoukko()

        lista_a = joukko_a.to_int_list()
        lista_b = joukko_b.to_int_list()

        yhdiste_lista = lista_a
        yhdiste_lista.extend(luku for luku in lista_b if luku not in yhdiste_lista)

        yhdiste.lisaa_lista_joukkoon(yhdiste, yhdiste_lista)

        return yhdiste

    @staticmethod
    def leikkaus(joukko_a, joukko_b):

        leikkaus = IntJoukko()
        
        sarja_a = set(joukko_a.to_int_list())
        sarja_b = set(joukko_b.to_int_list())

        leikkaus_sarja = sarja_a.intersection(sarja_b)

        leikkaus.lisaa_lista_joukkoon(leikkaus, leikkaus_sarja)

        return leikkaus

    @staticmethod
    def erotus(joukko_a, joukko_b):

        erotus = IntJoukko()
        
        sarja_a = set(joukko_a.to_int_list())
        sarja_b = set(joukko_b.to_int_list())

        erotus_sarja = sarja_a - sarja_b

        erotus.lisaa_lista_joukkoon(erotus, erotus_sarja)

        return erotus

    def lisaa_lista_joukkoon(self, joukko, luvut):

        for luku in luvut:
            joukko.lisaa(luku)

    def __str__(self):

        luvut = self.to_int_list()
        merkkijonot = self.muuta_lukulista_merkkijonolistaksi(luvut)

        merkkijono = self.muuta_lista_merkkijonoksi(merkkijonot)

        return merkkijono
        
    def kasittele_syote(self, syote, tyyppi: str):

        if syote == None:
            return vakioarvot[tyyppi]

        if self.tarkista_kokonaisluku(syote) and self.tarkista_positiivinen_luku:
            return syote
        
        raise Exception("Kapasiteetin ja kokonaisluvun on oltava positiivisia kokonaislukuja")

    def tarkista_kokonaisluku(self, luku):

        return isinstance(luku, int)
    
    def tarkista_positiivinen_luku(self, luku):

        return luku < 0
    
    def kasvata_alkioiden_lukumaaraa(self):

        self.alkioiden_lkm += 1

    def vahenna_alkioiden_lukumaaraa(self):

        self.alkioiden_lkm -= 1
    
    def lista_taynna(self):

        return self.alkioiden_lkm % len(self.lukujono) == 0
    
    def luo_uusi_lista(self):

        alkuperainen = self.lukujono
        self.kopioi_lista(self.lukujono, alkuperainen)
        self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(alkuperainen, self.lukujono)
    
    def muuta_lukulista_merkkijonolistaksi(self, lukulista):

        merkkijono_lista = [str(luku) for luku in lukulista]

        return merkkijono_lista

    def muuta_lista_merkkijonoksi(self, lista):
        
        merkkijono = "{"
        merkkijono += ", ".join(lista)
        merkkijono += "}"

        return merkkijono