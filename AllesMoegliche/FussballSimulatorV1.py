# Ein PyFuba-Spielsimulator - V1
# PyFuba - Wie Fußball nur mit etwas anderen Regeln - es gibt nur 6 Feldspieler, keine Ecken und jeder darfs aufs Tor schießen
# Dies ist die erste Version, bei die die Einfachheit im Vordergrund steht
# Die Spieler spielen Pässe, die ins Seitenaus gehen können, begehen Founds und schießen ab und zu aufs Tor
# Es gibt keine gelben Karten und die Entfernung zum Tor spielt keine Rolle
# Jede Minute tritt ein Spielereignis einund am Ende kommt ein Spielstand zustande
# Autor: Peter Monadjemi, www.pyhub.de
# Letzte Aktualisierung: 31/03/2020

import time
import random

# Definiert einen Spieler mit einem Namen
class Spieler:

    def __init__(self, Name, Nr, Torgefahr, Dribbling, Pass, Fairness):
        self.Name = Name
        self.TrikotNr = Nr
        # Wahrscheinlichkeit, dass ein Schuss aufs Tor ein Treffer ist
        self.Torgefahr = Torgefahr
        # Wahrscheinlichkeit, dass der Spieler beim Dribbling den Ball verliert
        self.Dribbling = Dribbling
        # Wahrscheinlichkeit, dass ein Pass nicht beim Mitspieler ankommt
        self.Passgenauigkeit = Pass
        self.Fairness = Fairness

# Definiert ein Team mit einem Namen und Spielern
class Team:

    def __init__(self, Name, Spieler):
        self.Name = Name
        self.Spieler = Spieler

# Definiert die "Umgebung" für ein Spiel        
class SpielkontextA:

    def Spielpass(self, Spieler):
        self.Spielstatus = "Pass"
        Ergebnis = random.randint(0,100) <= Spieler.Passgenauigkeit
        return Ergebnis

    def Torschuss(self, Spieler):
        self.Spielstatus = "Torschuss"
        Ergebnis = random.randint(0,100) <= Spieler.Torgefahr
        return Ergebnis

    def Foulspiel(self, Spieler):
        self.Spielstatus = "Foul"
        Ergebnis = random.randint(0,100) <= Spieler.Fairness
        return Ergebnis

    def LaufMitBall(self, Spieler):
        self.Spielstatus = "Normal"
        Ergebnis = random.randint(0,100) <= Spieler.Dribbling
        return Ergebnis

    def __init__(self, Name, TeamHeim, TeamGast):
        self.Name = Name
        self.TeamHeim = TeamHeim
        self.TeamGast = TeamGast
        self.TeamSpiel = TeamHeim
        self.Spielstatus = "Anpfiff"
        self.ToreHeim = 0
        self.ToreGast = 0
        self.AktuellerSpieler = TeamHeim.Spieler[0]
        self.Aktionsliste = [(self.Spielpass,80), (self.Torschuss,20), (self.Foulspiel,10)]
        self.StandardAktion = self.LaufMitBall

    def SpielAktion(self):
        z = random.randint(0, len(self.Aktionsliste)-1)
        w = random.randint(0, 100)
        if w <= self.Aktionsliste[z][1]:
            return self.Aktionsliste[z][0](self.AktuellerSpieler)
        else:
            return self.StandardAktion(self.AktuellerSpieler)

    def Spielstatus(self):
        return "Spielstatus"

HTeam = Team("Team A", [Spieler("Arnold",1,20,20,20,20), Spieler("Aichstätter",2,30,20,20,20), Spieler("Alaquiz",3,40,20,20,20), Spieler("Arnautovic",4,60,20,20,20),Spieler("Ailton",5,70,20,20,20), Spieler("Asimowich",6,70,20,20,20)])
GTeam = Team("Team B", [Spieler("Beister",1,20,20,20,20), Spieler("Bernandez",2,30,20,20,20), Spieler("Boateng",3,40,20,20,20), Spieler("Bittencour",4,50,20,20,20), Spieler("Bierhoff",9,80,20,20,20), Spieler("Beckenhauer",10,80,20,20,20)])

Spielkontext = SpielkontextA("Standard", HTeam, GTeam)

Spieldauer = 45
Spielzeit = 1

# Spielstart mit einem Heimspieler
z = random.randint(0, len(Spielkontext.TeamSpiel.Spieler) - 1)
spieler = Spielkontext.TeamSpiel.Spieler[z]
Spielkontext.AktuellerSpieler = spieler

while Spielzeit <= Spieldauer:
    # Aktuellen Spielstatus abfragen
    if Spielkontext.Spielstatus == "Anpfiff":
        print(f"Minute {Spielzeit}: Anpfiff  - Anstoß durch Spieler {Spielkontext.AktuellerSpieler.Name}")
    elif Spielkontext.Spielstatus == "Foul":
        print(f"Minute {Spielzeit}: Spieler {Spielkontext.AktuellerSpieler.Name} begeht ein Foul.")
        # Das andere Team kommt zum Zug
        Spielkontext.TeamSpiel = Spielkontext.TeamGast if Spielkontext.TeamSpiel.Name == Spielkontext.TeamHeim.Name else Spielkontext.TeamHeim
        # Spieler aus dem anderen Team festlegen
        z = random.randint(0, len(Spielkontext.TeamSpiel.Spieler) - 1)
        Spielkontext.AktuellerSpieler = Spielkontext.TeamSpiel.Spieler[z]
        print(f"Minute {Spielzeit}: Freistoß fuer {Spielkontext.TeamSpiel.Name}")
        Spielkontext.Spielstatus == "Normal"
    elif Spielkontext.Spielstatus == "Torschuss":
        print(f"Minute {Spielzeit}: Spieler {Spielkontext.AktuellerSpieler.Name} schießt auf das Tor.")
        if SpielErgebnis:
            print(f"Minute {Spielzeit}: Tor fuer {Spielkontext.TeamSpiel.Name} durch Spieler {Spielkontext.AktuellerSpieler.Name}")
            if Spielkontext.TeamSpiel.Name == Spielkontext.TeamHeim.Name:
                Spielkontext.ToreHeim += 1
            else:
                Spielkontext.ToreGast += 1
            print(f"Minute {Spielzeit}: Neuer Spielstand: {str(Spielkontext.ToreHeim)}:{str(Spielkontext.ToreGast)}")
        # Das andere Team kommt zum Zug
        Spielkontext.TeamSpiel =  Spielkontext.TeamGast if Spielkontext.TeamSpiel.Name == Spielkontext.TeamHeim.Name else Spielkontext.TeamHeim
        # Spieler aus dem anderen Team festlegen
        z = random.randint(0, len(Spielkontext.TeamSpiel.Spieler) - 1)
        Spielkontext.AktuellerSpieler = Spielkontext.TeamSpiel.Spieler[z]
        if SpielErgebnis:
            print(f"Minute {Spielzeit}: Anstoß für Team {Spielkontext.TeamSpiel.Name} durch Spieler {Spielkontext.AktuellerSpieler.Name}")
        else:
            print(f"Minute {Spielzeit}: Abstoß für Team {Spielkontext.TeamSpiel.Name}")
    elif Spielkontext.Spielstatus == "Pass":
        if not SpielErgebnis:
            print(f"Minute {Spielzeit}: Pass von Spieler {Spielkontext.AktuellerSpieler.Name} gehts in Seitenaus")
            # Das andere Team kommt zum Zug
            Spielkontext.TeamSpiel =  Spielkontext.TeamGast if Spielkontext.TeamSpiel.Name == Spielkontext.TeamHeim.Name else Spielkontext.TeamHeim
            # Spieler aus dem anderen Team festlegen
            z = random.randint(0, len(Spielkontext.TeamSpiel.Spieler) - 1)
            Spielkontext.AktuellerSpieler = Spielkontext.TeamSpiel.Spieler[z]
            print(f"Minute {Spielzeit}: Einwurf fuer {Spielkontext.TeamSpiel.Name}  durch Spieler {Spielkontext.AktuellerSpieler.Name}")
        else:
            # Pass muss einen anderen Spieler aus dem Team erreichen
            SpielerAlt = Spielkontext.AktuellerSpieler
            while True:
                z = random.randint(0, len(Spielkontext.TeamSpiel.Spieler) - 1)
                if Spielkontext.TeamSpiel.Spieler[z].Name != Spielkontext.AktuellerSpieler.Name:
                    Spielkontext.AktuellerSpieler = Spielkontext.TeamSpiel.Spieler[z]
                    break
            print(f"Minute {Spielzeit}: Spieler {SpielerAlt.Name} spielt einen Pass zu {Spielkontext.AktuellerSpieler.Name}")
    else:
        print(f"Minute {Spielzeit}: Spieler {Spielkontext.AktuellerSpieler.Name} läuft mit dem Ball")
        if not SpielErgebnis:
            # Das andere Team kommt zum Zug
            Spielkontext.TeamSpiel =  Spielkontext.TeamGast if Spielkontext.TeamSpiel.Name == Spielkontext.TeamHeim.Name else Spielkontext.TeamHeim
            AlterSpieler = Spielkontext.AktuellerSpieler
            # Spieler aus dem anderen Team festlegen
            z = random.randint(0, len(Spielkontext.TeamSpiel.Spieler) - 1)
            Spielkontext.AktuellerSpieler = Spielkontext.TeamSpiel.Spieler[z]
            print(f"Minute {Spielzeit}: Spieler {AlterSpieler.Name} verliert den Ball an Spieler {Spielkontext.AktuellerSpieler.Name}")

    # Nächste Aktion festlegen
    SpielErgebnis = Spielkontext.SpielAktion()

    time.sleep(1)
    Spielzeit += 1

print(f"Minute {Spielzeit}: Schlusspfiff")
print(f"Minute {Spielzeit}: Endstand {Spielkontext.TeamHeim.Name} gegen {Spielkontext.TeamGast.Name} {str(Spielkontext.ToreHeim)}:{str(Spielkontext.ToreGast)}")
