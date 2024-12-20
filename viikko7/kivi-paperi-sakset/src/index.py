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


if __name__ == "__main__":
    main()
