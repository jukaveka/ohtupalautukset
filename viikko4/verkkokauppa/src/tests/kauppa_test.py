import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "piimä", 10)
            if tuote_id == 3:
                return Tuote(3, "mehu", 15)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatytty_pankin_metodia_kutsutaan_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_tuotteen_ostoksen_paatyttya_pankin_metodia_kutsutaan_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("marko", "67890")

        self.pankki_mock.tilisiirto.assert_called_with("marko", 42, "67890", "33333-44455", 15)
    
    def test_kahden_varastossa_olevan_saman_tuotteen_ostaminen_onnistuu_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("tarmo", "13579")

        self.pankki_mock.tilisiirto.assert_called_with("tarmo", 42, "13579", "33333-44455", 10)

    def test_varastossa_olevan_ja_varastosta_loppuneen_tuotteen_ostaminen_onnistuu_oikeilla_arvoilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("miika", "24680")

        self.pankki_mock.tilisiirto.assert_called_with("miika", 42, "24680", "33333-44455", 5)

    def test_asioimisen_aloittaminen_nollaa_hinnan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("tomas", "19375")

        self.pankki_mock.tilisiirto.assert_called_with("tomas", 42, "19375", "33333-44455", 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("Phuc", "20486")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, 42, ANY, "33333-44455", 0)

    def test_uusi_maksutapahtuma_vaatii_viitteen_maksutapahtumalle(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Markus", "91735")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Tiitus", "02846")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Vilho", "00000")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_tuotteen_poistaminen_ja_oston_suorittaminen_kutsuu_pankin_metodia_oikeilla_arvoilla(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("Augustus", "99999")

        self.pankki_mock.tilisiirto.assert_called_with("Augustus", 42, "99999", "33333-44455", 5)