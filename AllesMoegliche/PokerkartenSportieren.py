# Sortieren von Pokerkarten
# Erstellt: 27/09/20

kartenWerte = {"Eins":1,"Zwei":2,"Drei":3,"Vier":4,"Fünf":5,"Sechs":6,"Sieben":7,"Acht":8,"Neun":9,"Zehn":10,
 "Bube":11,"Dame":12,"König":13,"Ass":14}

class Card():

    def __init__(self, Farbe, Wert):
        self.Farbe = Farbe
        self.Wert = Wert

    def __toString__(self):
        return f"{self.Farbe} {self.Wert}"


karten = [Card("Herz","Vier"),Card("Karo","Bube"),Card("Karo","König"),Card("Kreuz","Zehn")]

# Jetzt wird sortiert - dank Lambda eigentlich nicht so schwer;)

# sort() sortiert "in place"
karten.sort(key=lambda k: kartenWerte[k.Wert])

for karte in karten:
    print(karte.__toString__())

karten = [Card("Herz","Vier"),Card("Karo","Bube"),Card("Karo","König"),Card("Kreuz","Zehn")]
kartenSortiert = sorted(karten,key=lambda k: kartenWerte[k.Wert])

for karte in kartenSortiert:
    print(karte.__toString__())
