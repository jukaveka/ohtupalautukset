from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly=None):
        super().__init__(tekoaly)

    def pelaa(self):
        return super().pelaa()

    def _tokan_siirto(self, pelaaja1_siirto):
        return self._tekoaly.anna_siirto()
    
    def _pelaaja2_on_tekoaly(self):
        return super()._pelaaja2_on_tekoaly()