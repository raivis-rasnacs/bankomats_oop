from random import randrange as rnd
from datetime import date

class Karte:
    
    def __init__(self):
        self.numurs = "".join([str(rnd(0, 10)) for _ in range(11)])
        self.pin = "0000"
        self.termins = date(2030, 1, 30)
        self.bloketa = False
        self.bilance = 1000