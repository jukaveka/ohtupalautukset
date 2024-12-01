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
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku: int,):

        return luku in self.ljono

    def lisaa(self, luku):

        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.kasvata_alkioiden_lukumaaraa()

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.lista_taynna():
                self.luo_uusi_lista()

    def poista(self, luku):
        
        while luku in self.ljono:
            self.ljono.remove(luku)
            self.vahenna_alkioiden_lukumaaraa()

    def kopioi_lista(self, alkuperainen: list, kopio: list):

        for i in range(0, self.alkioiden_lkm):
            kopio[i] = alkuperainen[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        self.kopioi_lista(self.ljono, taulu)

        return taulu

    @staticmethod
    def yhdiste(a, b):

        yhdiste = IntJoukko()

        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste.lisaa(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
        
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

        return self.alkioiden_lkm % len(self.ljono) == 0
    
    def luo_uusi_lista(self):

        alkuperainen = self.ljono
        self.kopioi_lista(self.ljono, alkuperainen)
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(alkuperainen, self.ljono)