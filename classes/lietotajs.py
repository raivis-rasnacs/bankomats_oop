from classes.karte import Karte
from random import choice

class Lietotajs:
    
    def __init__(self, vards, uzvards):
        self.karte = Karte()
        self.vards = vards
        self.uzvards = uzvards
        self.naudas_maks = {nominals:1 for nominals in [5, 10, 20, 50, 100, 200, 500]}

    def ieliek_karti(self, bankomats):
        bankomats.nolasa_karti(self)

    def ievada_PIN_kodu(self):
        pin = input("PIN kods: ")
        return pin

    def ievada_summu(self):
        summa = int(input("Summa: "))
        return summa

    def ievieto_naudu(self):
        for nominals in self.naudas_maks:
            skaits = int(input(f"Cik {nominals}€ banknotes ievietosi?"))
            while skaits > self.naudas_maks[nominals]:
                print("Makā nepietiek banknošu!")
                skaits = int(input(f"Cik {nominals}€ banknotes ievietosi?"))
            self.naudas_maks[nominals] += skaits

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
