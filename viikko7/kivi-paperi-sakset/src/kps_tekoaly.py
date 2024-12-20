from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def _tokan_siirto(self):
        return self._tekoaly.anna_siirto()