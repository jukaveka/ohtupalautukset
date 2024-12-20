from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")