class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

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

class Operaatio():
    def __init__(self, sovelluslogiikka, arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._arvo = arvo 

class Summa(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)

    def suorita(self):
        self._sovelluslogiikka.plus(self._arvo())

class Erotus(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)

    def suorita(self):
        self._sovelluslogiikka.miinus(self._arvo())

class Nollaus(Operaatio):
    def __init__(self, sovelluslogiikka, arvo):
        super().__init__(sovelluslogiikka, arvo)
    
    def suorita(self):
        self._sovelluslogiikka.nollaa()