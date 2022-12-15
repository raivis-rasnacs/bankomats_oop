from classes.karte import Karte
from random import choice

class Lietotajs:
    
    def __init__(self, vards, uzvards):
        self.karte = Karte()
        self.vards = vards
        self.uzvards = uzvards
        self.naudas_maks = {
            5:[20],
            10:[20],
            20:[20],
            50:[10],
            100:[10],
            200:[10],
            500:[10]
        }

    def ieliek_karti(self, bankomats):
        bankomats.nolasa_karti(self)

    def ievada_PIN_kodu(self):
        pin = input("PIN kods: ")
        return pin

    def ievada_summu(self):
        summa = int(input("Summa: "))
        return summa

    def ievieto_naudu(self):
        pass

    def panem_naudu(self, saskaitita_nauda):
        for nominals in saskaitita_nauda:
            self.naudas_maks[nominals] += saskaitita_nauda[nominals]


class Inkasators(Lietotajs):
    def __init__(self):
        self.atslega = choice([
            333,
            555,
            777
        ])
        super().__init__()

    def papildina_bankomatu(self, bankomats):

        # Katram nominālam pievieno 20 banknotes
        for nominals in bankomats.naudas_konteiners:
            bankomats.naudas_konteiners[nominals] += 20

    def tukso_bankomatu(self, bankomats):

        # No katra nomināla noņem 20 banknotes
        for nominals in bankomats.naudas_konteiners:
            bankomats.naudas_konteiners[nominals] -= 20