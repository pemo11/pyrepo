# Pufferzeiten bei einem Netzplan berechnen
# Autor: Peter Monadjemi, info@activetraining.de
# Letzte Aktualisierung: 01/02/2020
#!/usr/bin/env python3
import os
import sys

# Repräsentiert einen Vorgang
class Vorgang:

    def __init__(self, Name, Beschreibung, Dauer, Vorgaenger, Nachfolger):
        self.Name = Name
        self.Beschreibung = Beschreibung
        self.Dauer = int(Dauer)
        self.Vorgaenger = Vorgaenger
        self.AnzahlVorgaenger = 0 if Vorgaenger[0] == "" else len(Vorgaenger)
        self.Nachfolger = Nachfolger
        self.AnzahlNachfolger = 0 if Nachfolger[0] == "" else len(Nachfolger)
        self.FAZ = 0
        self.SAZ = 0
        self.FEZ = 0
        self.SEZ = 0
        self.GP = 0
        self.FP = 0

    def __toString__(self):
        if len(self.Beschreibung) == 0:
            return f"{self.Name}: Dauer: { self.Dauer} FAZ/FEZ: {self.FAZ}/{self.FEZ} SAZ/SEZ: {self.SAZ}/{self.SEZ} GP/FP: {self.GP}/{self.FP}"
        else:
            return f"{self.Beschreibung}: Dauer: { self.Dauer} FAZ/FEZ: {self.FAZ}/{self.FEZ} SAZ/SEZ: {self.SAZ}/{self.SEZ} GP/FP: {self.GP}/{self.FP}"

def ErstelleNetzplan(Dateipfad):

    print(f"*** Verarbeite {Dateipfad} ***")

    netzplan = {}

    with open(Dateipfad, encoding="Utf-8") as fh:
        for zeile in fh:
            if zeile == "":
                break
            if zeile[-1] == "\n":
                zeile = zeile[:-1]
            name, beschreibung, dauer, vor, nach =  zeile.split(",")
            # Es soll immer eine Liste der Vorgänger und Nachfolger gebildet werden
            vor = vor.split(":")
            nach = nach.split(":")
            netzplan[name] = Vorgang(name,beschreibung,dauer,vor,nach)

    # Schritt 1: FAZ und FEZ im Vorwärtsgang berechnen
    for pk in netzplan:
        p = netzplan[pk]
        # Gibt es mehrere Vorgänger?
        if p.AnzahlVorgaenger == 1:
            v = netzplan[p.Vorgaenger[0]]
            p.FAZ = v.FEZ
        # elif len(p.Vorgaenger) > 0:
        elif p.AnzahlVorgaenger > 1:
            maxFEZ = max([netzplan[pv].FEZ for pv in p.Vorgaenger])
            p.FAZ = maxFEZ
        else:
            p.FAZ = 0
        p.FEZ = p.FAZ + p.Dauer

    # Schritt 2: SAZ und SEZ im Rückwärtsgang berechnen
    # Und bei der Gelegenheit auch GP und FP
    pKeys = list(netzplan.keys())
    pKeys.reverse()

    for pk in pKeys:
        p = netzplan[pk]
        # if len(p.Nachfolger) == 0:
        if p.AnzahlNachfolger == 0:
            # Weitere Randbedingung - es kann mehrere Vorgänger ohne Nachfolger geben,
            # es muss daher der größte FEZ genommen werden
            maxFEZ = max([netzplan[pn].FEZ for pn in pKeys if netzplan[pn].AnzahlNachfolger == 0])
            p.SEZ = maxFEZ # p.FEZ
        elif p.AnzahlNachfolger == 1:
            nv = netzplan[p.Nachfolger[0]]
            p.SEZ = nv.SAZ
            p.FP = nv.FAZ - p.FEZ
        else:
            minSAZ = min([netzplan[pn].SAZ for pn in p.Nachfolger])
            minFAZ = min([netzplan[pn].FAZ for pn in p.Nachfolger])
            p.SEZ = minSAZ
            p.FP = minFAZ - p.FEZ
        p.SAZ = p.SEZ - p.Dauer
        p.GP = p.SAZ - p.FAZ


    for p in netzplan.values():
        print(p.__toString__())

    # Schritt 3: Kritischen Pfad ermitteln
    # Also alle Vorgänge, bei denen GP und FP 0 sind
    kritischerPfad = []
    # Das erste Element holen
    # Weitere Randbedingung  - gibt es mehrere Vorgänge ohne Vorgänger, hole den mit GP=0
    p = [a for a in netzplan.values() if a.AnzahlVorgaenger == 0][0]
    kritischerPfad.append(p.Beschreibung if len(p.Beschreibung) > 0 else p.Name)
    while p.AnzahlNachfolger > 0:
        # Gibt es einen Nachfolger und sind GP und FP gleich 0?
        if p.AnzahlNachfolger == 1 and p.GP == 0 and p.FP == 0:
            p = netzplan[p.Nachfolger[0]]
            kritischerPfad.append(p.Beschreibung if len(p.Beschreibung) > 0 else p.Name)
        else:
            l = [netzplan[np] for np in p.Nachfolger if netzplan[np].GP == 0 and netzplan[np].FP == 0]
            # Gibt es keinen Knoten mehr?
            if len(l) == 0:
                print("*** Es kann kein kritischer Pfad gebildet werden! ***")
                break
            p = l[0]
            kritischerPfad.append(p.Beschreibung if len(p.Beschreibung) > 0 else p.Name)
 
    if len(kritischerPfad) > 1:
        print("Der kritische Pfad:",end=" ")
        print(",".join(kritischerPfad))

# Prüfen, ob Datei als Modul ausgeführt wird
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("!!! Aufruf: Netzplan.py Dateiname")
        exit(1)
    dateiPfad = sys.argv[1]
    # nur bei VS Code erforderlich
    dateiPfad = os.path.join(os.path.dirname(__file__), dateiPfad)
    ErstelleNetzplan(dateiPfad)

