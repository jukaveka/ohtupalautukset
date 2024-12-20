from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def _tokan_siirto(self):
        return self._tekoaly.anna_siirto()