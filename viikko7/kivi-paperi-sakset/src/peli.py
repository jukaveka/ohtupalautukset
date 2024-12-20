from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

pelitilat = {
    "a": KPSPelaajaVsPelaaja(),
    "b": KPSTekoaly(Tekoaly()),
    "c": KPSParempiTekoaly(TekoalyParannettu(10))
}

class Peli:
    @staticmethod
    def luo_peli(valinta):
        if Peli.validi_pelitila(valinta):
            return pelitilat[valinta]
        
        return None

    @staticmethod
    def validi_pelitila(valinta):
        return valinta in ("a", "b", "c")
    
    @staticmethod
    def valintaohje():
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )