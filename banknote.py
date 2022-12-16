from random import randrange as rnd

class Banknote:

    global krasas
    krasas = {
        5: "zaļa",
        10: "sarkana",
        20: "zila",
        50: "orange",
        100: "zaļa",
        200: "dzeltena",
        500: "violeta"
    }

    def __init__(self, nominals):
        self.valuta = "€"
        self.nominals = nominals
        self.krasa = krasas[nominals]
        self.serijas_nr = "SC" + "".join([str(rnd(0, 10)) for _ in range(10)])
        