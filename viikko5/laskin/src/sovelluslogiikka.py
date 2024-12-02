class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = 0

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def historia(self):
        return self._historia

    def aseta_edellinen_arvo(self):
        self._edellinen_arvo = self._arvo
    
    def edellinen_arvo(self):
        return self._edellinen_arvo

class Operaatio():
    def __init__(self, sovelluslogiikka, arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._arvo = arvo

class Summa(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)

    def suorita(self):
        self._sovelluslogiikka.aseta_edellinen_arvo()
        self._sovelluslogiikka.plus(self._arvo())

class Erotus(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)

    def suorita(self):
        self._sovelluslogiikka.aseta_edellinen_arvo()
        self._sovelluslogiikka.miinus(self._arvo())

class Nollaus(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)
    
    def suorita(self):
        self._sovelluslogiikka.aseta_edellinen_arvo()
        self._sovelluslogiikka.nollaa()

class Kumoa(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)
    
    def suorita(self):
        self._sovelluslogiikka.aseta_arvo(self._sovelluslogiikka.edellinen_arvo())
