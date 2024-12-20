from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def _pelaaja2_siirto(self):
        return self._tekoaly.anna_siirto()
