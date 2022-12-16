from random import randrange as rnd
from time import sleep

class Bankomats:
    
    def __init__(self, adrese):
        self.adrese = adrese
        self.naudas_konteiners = {nominals:10 for nominals in [5, 10, 20, 50, 100, 200, 500]}
        self.glabatas_kartes = []
        self.aktivais_lietotajs = None

    def darbibas_izvele(self):
        print("""Izvēlies darbību!
        1) Izmaksa
        2) Iemaksa
        3) Bilance
        4) PIN maiņa
        5) Beigt darbu
        """)

        darbiba = int(input("Darbība: "))
        if darbiba == 1:
            self.izdod_naudu()
        elif darbiba == 2:
            self.sanem_naudu()
        elif darbiba == 3:
            self.parada_bilanci()
        elif darbiba == 4:
            self.maina_pin_kodu()
        elif darbiba == 5:
            self.izdod_karti()

    def izdod_naudu(self):
        summa = self.pieprasa_summu(self.aktivais_lietotajs)
        if summa > self.aktivais_lietotajs.karte.bilance:
            print("Summa ir pārāk liela!")
            self.darbibas_izvele()
        saskaitita_nauda = self.skaita_naudu(summa)
        self.aktivais_lietotajs.karte.bilance -= summa

        self.aktivais_lietotajs.panem_naudu(saskaitita_nauda)
        for nominals in saskaitita_nauda:
            self.naudas_konteiners[nominals] -= saskaitita_nauda[nominals]
            
        print(list(self.naudas_konteiners.values()))
        self.darbibas_izvele()

    def parada_bilanci(self):
        print(f"Bilance: {self.aktivais_lietotajs.karte.bilance}")
        self.darbibas_izvele()

    def noglaba_karti(self, karte):
        self.bloke_karti(karte)
        self.glabatas_kartes += [karte]

    def bloke_karti(self, karte):
        karte.bloketa = True

    def izdod_karti(self):
        self.ielade("Izdod karti")
        self.aktivais_lietotajs = None
        print("Paņemiet karti! Gaidīsim jūs atkal!")

    def nolasa_karti(self, lietotajs):
        if lietotajs.karte.bloketa != True:
            if len(lietotajs.karte.numurs) == 11:
                print("Karte atpazīta!")
                self.aktivais_lietotajs = lietotajs
                self.darbibas_izvele()
            else:
                print("Karte nederīga!")
                self.izdod_karti(lietotajs.karte)
        else:
            print("Karte bloķēta!")
            self.izdod_karti(lietotajs.karte)

    def maina_PIN_kodu(self):
        vecais_pin = self.aktivais_lietotajs.ievada_PIN_kodu()
        if vecais_pin == self.aktivais_lietotajs.karte.pin:
            jaunais_pin = input("Jaunais pin: ")
            if len(jaunais_pin) == 4 and jaunais_pin.isdigit():
                self.aktivais_lietotajs.karte.pin = jaunais_pin
                self.ielade("Maina pin kodu")
                print("Pin koda nomaiņa veiksmīga!")

    def pieprasa_PIN_kodu(self, lietotajs):
        pin = lietotajs.ievada_PIN_kodu()
        if pin == lietotajs.karte.pin:
            return True
        else: 
            print("PIN kods kļūdains!")
            return False

    def pieprasa_summu(self, lietotajs):
        print("Ievadiet summu!")
        summa = lietotajs.ievada_summu()
        return summa

    def skaita_naudu(self, summa):
        self.ielade("Skaita naudu")
        bankn500 = summa // 500
        summa -= bankn500 * 500
        bankn200 = summa // 200
        summa -= bankn200 * 200
        bankn100 = summa // 100
        summa -= bankn100 * 100
        bankn50 = summa // 50
        summa -= bankn50 * 50
        bankn20 = summa // 20
        summa -= bankn20 * 20
        bankn10 = summa // 10
        summa -= bankn10 * 10
        bankn5 = summa // 5
        summa -= bankn5 * 5

        saskaitita_nauda = {
            5:bankn5,
            10:bankn10,
            20:bankn20,
            50:bankn50,
            100:bankn100,
            200:bankn200,
            500:bankn500
        }

        return saskaitita_nauda

    def apstiprina_atslegu(self, atslega):
        pass

    def ielade(self, pazinojums):
        print(f"{pazinojums}", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            sleep(1)

class IemaksasBankomats(Bankomats):

    def __init__(self):
        super().__init__()

    def sanem_naudu(self):
        pass