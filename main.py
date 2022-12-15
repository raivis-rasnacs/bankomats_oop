from classes.bankomats import Bankomats
from classes.banknote import Banknote
from classes.karte import Karte
from classes.lietotajs import Lietotajs, Inkasators

Dace = Lietotajs("Dace", "Zemīte")
bankomats = Bankomats("Zaļā iela 5")
Dace.ieliek_karti(bankomats)