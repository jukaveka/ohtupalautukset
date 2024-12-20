from peli import Peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        pelitila = input()

        if not Peli.validi_pelitila(pelitila):
            break

        peli = Peli.luo_peli(pelitila)
        print(peli.ohje())

        peli.pelaa()

        '''
        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = peli.pelaaja_vs_pelaaja()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = peli.pelaaja_vs_tekoaly()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = peli.pelaaja_vs_parempi_tekoaly()
            haastava_yksinpeli.pelaa()
        else:
            break
        '''


if __name__ == "__main__":
    main()
