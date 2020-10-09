# Eine kleine Tomatenfarm-Simulation
# Erstellt: 20/08/20

# Mit einem kleinen Startkapital kaufst Du Tomatenplanzen (drei Klassen: A, B und C)
# Wichtig: Eine Tomatenpflanze hat eine Reifezeit in Wochen - vorher können keine Tomaten geerntet werden
# und die Pflanze kostet nur Geld
# Bis dahin muss man durch Kaufen, Gießen und Düngen dafür sorgen, dass möglichst viele Tomaten heranreifen
# Ernte: Pro Pflanze werden alle Tomaten entfernt
# Das Ziel ist es, nach Ablauf der Zeit den maximalen Ertrag zu erzielen

# Stand: 26/08/20 - da ich noch einmal alles grundlegend überarbeiten musste, ist noch nichts fertig

# Es fehlen noch:
#>Ausgabeformatierung (oft Nachkommastellen wo es keine geben dürfte)
#>Überprüfen der Logik
#>Akustische Signale
#>Stand der Simulation speichern

# Wichtig: Jede Pflanze muss eine unterschiedliche Erntezeit besitzen, sonst macht die Unterscheidung auch keinen Sinn
# Dann muss aber berechnet werden, wie viele Tomaten es pro Pflanze geben kann
# 25/08 - mir wird klar, dass die indivuelle Erntezeit pro Tomate berechnet werden muss, und dass es daher
# auch eine Tomate-Klasse mit Erntezeit geben muss - so kann jede Tomate indivuell geerntet werden
# Es gibt also noch etwas zu tun - und der Verlauf wird pro Woche gezählt über ein ein "Erntejahr", das im
# März beginnt und im September ende, also 6 Monate und 24 Wochen, das ist überschauhbar

# Die Version V2 wird interaktiver, so dass sie auch in einem Notebook eingesetzt werden kann:
# >Modul
# >Automatisch laufene Simulation mit einem Aktionsplan, der jeder Woche eine Aktion zugeordnet, z.B.
# w10:Düngen, Gießen, Ernten oder so ähnlich eventuell auch mit Bedingungen
# >Ausgabe der Plantage als BarChar

import random

Kapital = 25
PlantageWert = 0
Kilopreis = 4.5
KostenProPflanze = 0.25
KostenFuerGießen = 2
KostenFuerDüngen = 5

# Definiert eine Plantage
class Plantage:

    def __init__(self,Name):
        self.Name = Name
        self.Pflanzen = []
        # Die Formel wird etwas komplizierter, da jede Pflanze n Tomaten und jede Tomate 
        # ihr eigenes Gewicht besitzt
        self.Wert = sum([t.Gewicht for t in [p.Tomaten for p in self.Pflanzen]]) / 1000 * Kilopreis
        self.Status = "Optimal"

    def __toString__(self):
        anzahlTomaten = sum([len(p.Tomaten) for p in self.Pflanzen])
        return f"Name: {self.Name} Status: {self.Status} Anzahl Pflanzen: {len(self.Pflanzen)} Anzahl Tomaten: {anzahlTomaten} Wert: {self.Wert:0.2f}€ "

# Definiert eine einzelne Pflanze
class Pflanze:

    def __init__(self, Sorte, Reifezeit, Preis, Tomaten):
        self.Sorte = Sorte
        self.Reifezeit = Reifezeit
        self.Preis = Preis
        self.Tomaten = Tomaten
        # Dieser Wert nimmt für die Pflanze ohne Gießen auf 0 ab => Pflanze vertrocknet
        self.Feuchtigkeit = 100
        # Dieser Wert nimmt für die Pflanze ohne Düngen auf 0 ab => Pflanze stirbt
        self.Nahrung = 100   
 
    def __toString__(self):
        # Zahl der Tomaten soll "gerundet" ausgegeben werden
        return f"Sorte: {self.Sorte} Reifezeit: {self.Reifezeit} Anzahl Tomaten: {len(self.Tomaten):.0f} Feuchtigkeit: {self.Feuchtigkeit} Nahrung: {self.Nahrung}"

# Definiert eine Tomate
class Tomate:

    def __init__(self, Woche):
        self.Woche = Woche
        # Gewicht beginnt mit einem Startwert, z.B. 10g
        self.Gewicht = 10
        # Für künftige Erweiterungen
        self.Farbe = "Rot"

# Preis in €/Bezeichnung/Erntezeit in Wochen
# Die Erntezeit wurde etwas verkürzt, damit eine Ernte  schneller starten kann
Sorten = {"A":(3.5,"Previa",3),"B":(2.5,"Alicante",5),"C":(1.5,"Andenhorn",10)}

# Kaufen von Tomatenpflanzen
def Kaufen():
    global Kapital
    # Erst einmal das aktuelle Kapital ausgeben
    print(f"\n*** Dein aktuelles Kapital {Kapital:.2f}€ ***")
    # So genial!
    inputText = ",".join([k + "=" + Sorten[k][1] + " für " + f"{Sorten[k][0]:.2f}" + "€"
      for k in Sorten.keys()][:-1]) + " oder "
    letztesElement = list(Sorten.items())[-1]
    # bereits etwas spezieller, das ist klar;)
    # Der Hintergrund ist: letztesElement z.B. = ('C', (3.5, 'Previa', 7)) 
    inputText += letztesElement[0] + "=" + letztesElement[1][1] + " für " + f"{letztesElement[1][0]:.2f}" + "€ "
    kategorie = input("\nWelche Sorte willst Du? " + inputText + "?").upper()
    if Sorten.get(kategorie) == None:
        print("!!! Falsche Auswahl - diese Option gibt es nicht !!!")
        return
    sorte = Sorten[kategorie][1]
    anzahl = int(input(f"Wie viele Pflanzen der Sorte {sorte} wilst Du?"))
    preis = Sorten[kategorie][0] 
    reifezeit = Sorten[kategorie][2]
    kaufpreis = preis * anzahl
    # Reicht das Kapital?
    if kaufpreis > Kapital:
        print(f"Leider reicht Dein Kapital von {Kapital:.2f} € nicht zum Kauf der Pflanzen\n")
        return
    kaufen = input(f"{anzahl} Pflanzen der Sorte {sorte} zum Preis von {kaufpreis:.2f}€ kaufen J/N?")
    if kaufen.upper() == "J":
        for _ in range(0, anzahl):
            # Liste mit 10 Tomaten anlegen (die Anfangsausstattung)
            tomaten = [Tomate(Woche) for _ in range(0, 10)]
            # List Comprehension ist immer wieder genial
            # Pflanze zur Plantage hinzufügen
            MeinePlantage.Pflanzen.append(Pflanze(sorte, reifezeit, preis, tomaten))
        Kapital -= kaufpreis
        print(f"Du hast {anzahl} Pflanzen gekauft - Dein aktuelles Kapital {Kapital:.2f}€\n")

# Den Bestand der Plantage und der Pflanzen ausgeben
def AusgabeBestand():
    print("\n*** Der Status der Plantage ***")
    print(MeinePlantage.__toString__())
    print(f"*** Der Status aller {len(MeinePlantage.Pflanzen)} Pflanzen ***")
    for s in MeinePlantage.Pflanzen:
        print(s.__toString__())

# Gießen aller Pflanzen
def Gießen():
    global Kapital
    # In der aktuellen Version wird die Feuchtigkeit aller Pflanzen um den gleichen Betrag erhöht
    for pflanze in MeinePlantage.Pflanzen:
        pflanze.Feuchtigkeit += 20
    # Gießen kostet Geld
    Kapital -= KostenFuerGießen
    print("*** Alle Pflanzen wurden gegossen ***\n")
    # Noch einmal das Kapital checken
    if Kapital <= 0:
        print("*** Du bist leider pleite - die Plantage muss verkauft werden ***")
    exit

# Düngen aller Pflanzen
def Düngen():
    global Kapital
    # In der aktuellen Version wird die Nahrung für alle Pflanzen um den gleichen Betrag erhöht
    for pflanze in MeinePlantage.Pflanzen:
        pflanze.Nahrung += 10
    # Düngen kostet Geld
    Kapital -= KostenFuerDüngen
    print("*** Alle Pflanzen wurden gedüngt ***\n")
    # Noch einmal das Kapital checken
    if Kapital <= 0:
        print("*** Du bist leider pleite - die Plantage muss verkauft werden ***")
    exit

# Es werden alle Tomaten von Pflanzen geerntet, die in der Woche w bereits reif sind
def Ernten():
    global Kapital
    anzahlPflanzen = int(input("Wieviele Pflanzen sollen geerntet werden?"))
    anzahlTomaten = 0
    gesamtGewicht = 0
    alleTomaten = []
    # Alle Pflanzen holen, die geernet werden können
    # !!! Formel stimmt noch nicht, da die Wochenzahl der Tomaten berücksichtigt werden muss ???
    allePflanzen = [p for p in MeinePlantage.Pflanzen if p.Reifezeit <= Woche]
    # Gibt es genügend Pflanzen zum Ernten?
    if anzahlPflanzen > len(allePflanzen):
        anzahlPflanzen = len(allePflanzen)
        print(f"!!! Es können nur {anzahlPflanzen} Pflanzen geerntet werden !!!")
    # Die Planzen holen
    allePflanzen = allePflanzen[0:anzahlPflanzen]
    for p in allePflanzen:
        # Tomaten holen, die geerntet werden können
        alleTomaten = [t for t in p.Tomaten if t.Woche >= p.Reifezeit]
        # Gesamtgewicht aufaddieren
        for t in alleTomaten:
            gesamtGewicht += t.Gewicht
        # Alle Tomaten weggenehmen
        for t in alleTomaten:
            p.Tomaten.remove(t)
    # Gab es eine Ernte?
    anzahlTomaten = len(alleTomaten)
    if anzahlTomaten == 0:
        print("\n!!! Es gibt leider keine Tomaten zum Ernten !!!\n")
        return
    ertragPreis = gesamtGewicht / 1000 * Kilopreis
    Kapital += ertragPreis
    print(f"*** Die Ernte von {anzahlTomaten} Tomaten ergibt einen Ertrag von {ertragPreis:.2f}€ ***")
    print(f"*** Dein neues Kapital beträgt {Kapital:.2f}€ ***\n")

# Ausgabe des aktuellen Zustandes der Plantage
def PlantagenStatus():
    global Kapital, PlantageWert, ExitModus
    anzahlPflanzen = len(MeinePlantage.Pflanzen)
    # Auch genial
    anzahlTomaten = sum([len(p.Tomaten) for p in MeinePlantage.Pflanzen])
    gesamtGewicht = 0
    PlantageWert = gesamtGewicht / 1000 * Kilopreis
    # Vom Kapital die Betriebskosten abziehen
    Kapital -=  anzahlPflanzen * KostenProPflanze
    if Kapital <= 0:
        print("*** Du bist leider pleite - die Plantage muss verkauft werden ***")
        ExitModus = True
    DurchschnittsFeuchtigkeit = 0
    DurchschnittsNahrung = 0
    if len(MeinePlantage.Pflanzen) > 0:
        DurchschnittsFeuchtigkeit = sum([p.Feuchtigkeit for p in MeinePlantage.Pflanzen]) / len(MeinePlantage.Pflanzen)
        DurchschnittsNahrung = sum([p.Nahrung for p in MeinePlantage.Pflanzen]) / len(MeinePlantage.Pflanzen)
    print(f"Anzahl Pflanzen: {anzahlPflanzen}")
    print(f"Anzahl Tomaten: {anzahlTomaten}")
    print(f"Durchschnittlicher Nahrungswert: {DurchschnittsNahrung}")
    print(f"Durchschnittliche Feuchtigkeit: {DurchschnittsFeuchtigkeit}")
    print(f"Aktueller Wert der Plantage: {PlantageWert:.2f}€")
    print(f"Dein aktuelles Kapital: {Kapital:.2f}€")

# Sehr praktisch: Ein Dictionary mit einem Buchstaben als Schlüssel und einem Tupel als Wert
# Tupel enthält Beschreibung der Aktion und Name der def function
Aktionsliste = {"A":("Bestand ausgeben", AusgabeBestand), 
                "B":("Pflanzen kaufen", Kaufen),
                "C":("Tomaten ernten", Ernten),
                "D":("Pflanzen giessen", Gießen),
                "E":("Pflanzen düngen", Düngen),
                "F":("Zustand der Plantage", PlantagenStatus)
               }

# Ausgabe des Auswahlmenüs
def MenueAusgabe():
    for k in Aktionsliste.keys():
        print(k, Aktionsliste[k][0])
    inputtext = ",".join(Aktionsliste.keys()) + " oder Q?"
    a = input(inputtext)
    return a

# Berechnet den Wachstumsfaktor anhand des Zustandes Plantage
# Plantagenzustand = Nahrung, Feuchtigkeit usw.
# Generell eine Übungsaufgabe: Wie kombiniert man zwei oder mehrere Werte zu einer Note?
# Beispiel: Feuchtigkeit = 10, Nahrung = 30 => 10+30/2 = 20%
# Beispiel: Feuchtigkeit = 100, Nahrung = 100 => 100+100/2 = 100%
def BerechneWachstumsfaktor():
    global Wachstumsfaktor
    # Gibt es bereits Pflanzen?
    if len(MeinePlantage.Pflanzen) == 0:
        return
    feuchtigkeit = sum([p.Feuchtigkeit for p in MeinePlantage.Pflanzen]) / len(MeinePlantage.Pflanzen)
    nahrung = sum([p.Nahrung for p in MeinePlantage.Pflanzen]) / len(MeinePlantage.Pflanzen)
    gesamt = feuchtigkeit + nahrung // 2
    # PlantagenStatus festlegen
    if gesamt == 100:
        MeinePlantage.Status = "Optimal"
        Wachstumsfaktor = 2
    elif gesamt > 80:
        MeinePlantage.Status = "Gut"
        Wachstumsfaktor = 1.6
    elif gesamt > 60:
        MeinePlantage.Status = "OK"
        Wachstumsfaktor = 1.2
    elif gesamt > 30:
        MeinePlantage.Status = "Problematisch"
        Wachstumsfaktor = 1.0
    elif gesamt > 10:
        MeinePlantage.Status = "Kritisch"
        Wachstumsfaktor = 0.8
    else:
        MeinePlantage.Status = "Schlecht"
        Wachstumsfaktor = 0.5

# Aktualisierung des Zustandes der Plantage
def PlantagenUpdate():
    # Wachstumsfaktor vor (!) dem Aktualisieren von Nahrung von Feuchtigkeit berechnen
    BerechneWachstumsfaktor()
    # Nahrung und Feuchtigkeit herabsetzen, da beide pro Woche weniger werden
    for p in MeinePlantage.Pflanzen:
        if p.Nahrung >= 10: 
            p.Nahrung -= 10
        if p.Feuchtigkeit >= 15:
            p.Feuchtigkeit -= 15
    # Anzahl der Tomaten anhand des Wachstumsfaktors für alle Pflanzen neu berechnen
    for p in MeinePlantage.Pflanzen:
        aktuelleAnzahl = len(p.Tomaten)
        neueAnzahl = int(aktuelleAnzahl * Wachstumsfaktor)
        # Sind es mehr oder weniger geworden?
        if neueAnzahl > aktuelleAnzahl:
            differenz = abs(neueAnzahl - aktuelleAnzahl)
            neueTomaten = [Tomate(Woche) for _ in range(0, differenz) ]
            p.Tomaten += neueTomaten
        elif neueAnzahl < aktuelleAnzahl:
            p.Tomaten = p.Tomaten[0:neueAnzahl]
        # Alle Tomaten müssen wachsen
        for t in p.Tomaten:
            t.Gewicht *= Wachstumsfaktor

# Es können verschiedene Ereignisse eintreten
# Ein Hagel reduziert die Anzahl der Tomaten oder Pflanzen?
def Hagelschaden():
    anzahlTomaten = 0
    for p in MeinePlantage.Pflanzen:
        #  Anzahl der Tomaten berechnen, die zerstört wurden
        verlust = int(len(p.Tomaten) * 0.2)
        # Anzahl der Tomaten um den Verlust reduzieren
        p.Tomaten = p.Tomaten[0:verlust]
        anzahlTomaten += verlust
    print(f"*** Der Hagelschaden hat {anzahlTomaten} Tomaten vernichtet ***\n")

# Eine Hitzewelle reduziert die Feuchtigkeit der Pflanzen um 15
def Hitzewelle():
    for p in MeinePlantage.Pflanzen:
        if p.Feuchtigkeit > 15:
            p.Feuchtigkeit -= 15
    # Neue Durchschnittsfeuchtigkeit berechnen
    feuchtigkeit = sum([p.Feuchtigkeit for p in MeinePlantage.Pflanzen]) / len(MeinePlantage.Pflanzen)
    print(f"!!! Nach der Hitzewelle beträgt die Durchschnittsfeuchtigkeit der Pflanzen {feuchtigkeit} !!!\n")

# Schädlinge reduzieren die Anzahl der Tomaten um 10%
# Anders als beim Hagel geht es hier um die Tomaten nicht um die Pflanzen
def Schaedlinge():
    # In jeder Pflanze 10% weniger Tomaten
    anzahlTomaten = 0
    # Alle Pflanze durchgehen
    for s in MeinePlantage.Pflanzen:
        # Verluste berechnen
        verlust = int(len(s.Tomaten) * 0.1)
        # Verluste pro Pflanze aufaddieren
        anzahlTomaten += verlust
        # Verluste von Anzahl der Tomaten der Pflanze abziehen, in dem die Liste einfach verkleinert wird
        s.Tomaten = s.Tomaten[0:len(s.Tomaten)-verlust]
    # Schadensbericht
    print(f"!!! Durch Schädlinge wurden {anzahlTomaten} zu Nichte gemacht !!!")

# Der Preis pro Kilo Tomaten steigt
def Nachfagesteigerung():
    global Kilopreis
    # preisSteigerung = random.randint(10,30)
    preisSteigerung = 20
    Kilopreis *= 1 + preisSteigerung / 100
    print(f"*** Durch eine Tomatenknappheit steigt der Preis pro Kg auf {Kilopreis:.2f}€ ***")

# Ereignis, Wahrscheinlichkeit, Aktion
# Beschreibung der Aktion/Eintrittswahrscheinlichkeit/Name der def function
# Eventuell Auswirkung per Zufallszahlengenerator in einem Bereich festlegen
Ereignisse = [(">>> Ein Hagelschauer hat 20% der Pflanzen zerstört<<<", 25, Hagelschaden),
              (">>> Eine Hitzewelle hat die Feuchtigkeit weiter reduziert<<<", 25, Hitzewelle),
              (">>> Fiese Schädlingen haben 10% der Tomaten ungenießbar gemacht<<<", 20, Schaedlinge),
              (">>> Die Nachfrage nach Tomaten steigt, der Preis steigt um 20%<<<", 30, Nachfagesteigerung)
             ]

# **************************** Hier beginnt die Programmausführung *********************************

# Anlegen der Plantage mit einem beliebigen Namen
MeinePlantage = Plantage("High Desert One")

ExitModus = False

# Die Pflanzzeit Woche für Woche durchgehen
AnzahlWochen = 15
for Woche in range(1, AnzahlWochen + 1):
    print(f"\n***Heute ist die {Woche}te Woche von {AnzahlWochen} Wochen auf der Tomatenfarm. ***")
    print("Was möchtest Du tun?\n")
    a = MenueAusgabe()
    if a == "Q":
        ExitModus = True
    else:
        # Wurde eine Aktion gewählt?
        if a != "":
            # Gibt es die Aktion überhaupt?
            if Aktionsliste.get(a) == None:
                print("\n!!! Diese Eingabe verstehe ich nicht - probiere es noch einmal !!!")
                continue 
            # Ausführen der Aktion
            Aktionsliste[a][1]()
    # Soll ein Ereignis eintreten?
    if random.randint(1,10) > 5:
        r = random.randint(0, len(Ereignisse) - 1)
        ereignis = Ereignisse[r]
        # Hole die Wahrscheinlichkeit
        w = ereignis[1]
        r = random.randint(0, 100)
        if r <= w:
            print(ereignis[0])
            ereignis[2]()
    # Den Status der Plantage aktualisieren (u.a. die Anzahl der Tomaten)
    PlantagenUpdate()
    # Den Status der Plantage ausgeben
    PlantagenStatus()
    # Abbruch?
    if ExitModus:
        break
