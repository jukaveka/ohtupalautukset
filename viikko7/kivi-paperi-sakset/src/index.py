from peli import Peli

def main():
    while True:
        Peli.valintaohje()

        pelitila = input()

        if not Peli.validi_pelitila(pelitila):
            break

        peli = Peli.luo_peli(pelitila)
        peli.ohje()

        peli.pelaa()


if __name__ == "__main__":
    main()
