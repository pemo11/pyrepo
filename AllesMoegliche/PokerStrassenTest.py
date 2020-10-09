# Feststellen, ob und wenn ja, was eine Poker-Hand für Straßentyp ist

# Erstellt: 28/09/20

class Card():

    def __init__(self, Farbe, Wert):
        self.Farbe = Farbe
        self.Wert = kartenWerte[Wert]

    def __toString__(self):
        return f"{self.Farbe} {self.Wert}"


kartenWerte = {"Eins":1,"Zwei":2,"Drei":3,"Vier":4,"Fünf":5,"Sechs":6,"Sieben":7,"Acht":8,"Neun":9,"Zehn":10,
 "Bube":11,"Dame":12,"König":13,"Ass":14}

def IstReihe(Cards):
    okFlag = True
    c1 = Cards[0]
    for c in Cards[1:]:
        okFlag = okFlag and abs(c.Wert - c1.Wert) == 1
        c1 = c
    return okFlag

def StrassenTyp(Cards):
    if IstReihe(Cards):
        if Cards[4].Wert == kartenWerte["Ass"]:
            return 2
        else:
            return 1
    else:
        return 0

# Kleine Strasse
hand1 = [Card("Herz","Vier"),Card("Karo","Fünf"),Card("Kreuz","Sechs"),Card("Kreuz","Sieben"),Card("Karo","Acht")]
print(StrassenTyp(hand1))

# Große Strasse
hand2 = [Card("Herz","Zehn"),Card("Karo","Bube"),Card("Kreuz","Dame"),Card("Kreuz","König"),Card("Karo","Ass")]
print(StrassenTyp(hand2))

# Keine Strasse
hand3 = [Card("Herz","Vier"),Card("Karo","Fünf"),Card("Kreuz","Sechs"),Card("Kreuz","Sieben"),Card("Karo","Zehn")]
print(StrassenTyp(hand3))
