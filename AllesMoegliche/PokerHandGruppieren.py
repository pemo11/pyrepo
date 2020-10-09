# Gruppieren einer Hand von Pokerkarten
# Erstellt: 27/09/20

class Card():

    def __init__(self, Farbe, Wert):
        self.Farbe = Farbe
        self.Wert = Wert

    def __toString__(self):
        return f"{self.Farbe} {self.Wert}"

# Fullhouse
hand1 = [Card("Herz","Vier"),Card("Karo","Vier"),Card("Kreuz","Vier"),Card("Kreuz","Zehn"),Card("Karo","Zehn")]

def WertGruppen(Cards):
    d = {}
    for c in Cards:
        d[c.Wert] = 1 if d.get(c.Wert) == None else d[c.Wert] + 1
    return d

def FarbGruppen(Cards):
    d = {}
    for c in Cards:
        d[c.Farbe] = 1 if d.get(c.Farbe) == None else d[c.Farbe] + 1
    return d

gruppen = WertGruppen(hand1)

for g in gruppen.items():
    print(f"Gruppe: {g[0]} - Zahl: {g[1]}")

gruppen = FarbGruppen(hand1)

for g in gruppen.items():
    print(f"Gruppe: {g[0]} - Zahl: {g[1]}")