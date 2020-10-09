# Ausgabe einer Hand von Pokerkarten als Text
# Erstellt: 03/10/20

class Card():

    def __init__(self, Farbe, Wert):
        self.Farbe = Farbe
        self.Wert = Wert

    def __toString__(self):
        return f"{self.Farbe} {self.Wert}"

hand1 = [Card("Herz","Vier"),Card("Karo","Vier"),Card("Kreuz","Vier"),Card("Kreuz","Zehn"),Card("Karo","Zehn")]

handText = ",".join([f"{c.Farbe}-{c.Wert}" for c in hand1])

print(handText)

cardList = [Card("Herz","Zwei"),Card("Herz","Drei"),Card("Herz","Vier"),Card("Herz","FÜnf"),Card("Herz","Sechs"),
 Card("Herz","Sieben"),Card("Herz","Acht"),Card("Herz","Neun"),Card("Herz","Zehn"), Card("Herz","Bube"),
 Card("Herz","Dame"),Card("Herz","König"),Card("Herz","Ass")]

# Jetzt etwas schwerer, in dem die Hand aus den Karten-Index-Nummern besteht
hand2 = [(1,1),(2,4),(3,7),(4,9),(5,10)]

handText = ",".join([f"{cardList[t[1]].Farbe}-{cardList[t[1]].Wert}" for t in hand2])

print(handText)
