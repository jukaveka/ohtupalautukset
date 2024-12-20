from tekoaly import Tekoaly
from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self, tekoaly=None):
        super().__init__(tekoaly)

    def pelaa(self):
        return super().pelaa()

    def _tokan_siirto(self, pelaaja1_siirto):
        return input("Toisen pelaajan siirto: ")
    
    def _pelaaja2_on_tekoaly(self):
        return super()._pelaaja2_on_tekoaly()
