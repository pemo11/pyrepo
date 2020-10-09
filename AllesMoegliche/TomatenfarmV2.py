# Tomatenplantage-Simulation V2
# Erstellt: 02/09/2020
# Diese Variante soll in erster Linie als Modul eingesetzt und auch im Rahmen eines Jupyter-Notebooks
# Dazu muss sie auch über einen längeren Zeitraum laufen können mit Steuerungsparametern, z.B. automatischem Düngen,
# automatischer Ernte, so dass eine größere Datenbasis entsteht, die dann ausgewertet werden kann
# Das Budget kann in diesem Fall auch negativ werden bzw. es geht in erster Linie um die Ernte
# Ausgaben erfolgen in eine Log-Datei

# Definiert die Plantage
class Plantage:

    def __init__(self,Name):
        self.Name = Name
        self.Pflanzen = []
        # Die Formel wird etwas komplizierter, da jede Pflanze n Tomaten und jede Tomate 
        # ihr eigenes Gewicht besitzt
        # Allgemeines Problem: Kilopreis ist noch nicht definiert, da es eine globale Variable sein soll
        # Keine ganz gute Idee - doch wie kann dieser Wert zur verfügung gestellt werden?
        self.Wert = sum([t.Gewicht for t in [p.Tomaten for p in self.Pflanzen]]) / 1000 * Kilopreis
        self.Status = "Optimal"

    def __toString__(self):
        anzahlTomaten = sum([len(p.Tomaten) for p in self.Pflanzen])
        return f"Name: {self.Name} Status: {self.Status} Anzahl Pflanzen: {len(self.Pflanzen)} Anzahl Tomaten: {anzahlTomaten} Wert: {self.Wert:0.2f}€ "

# Definiert eine einzelne Pflanze
# Muss der Preis Teil der Klassendefinition sein? Gehört er zu den Kernndaten, ist er für eine Verarbeitung wichtig?
# Volatile Daten sollten nicht Teil der Kerndefinition sein
# Feuchtigung und Nahrung beschreiben den Zustand der Pflanze und sind daher wichtig, der Preis beschreibt nicht den Zustand der Pflanze,
# sondern spielt nur im Rahmen von Transaktionen und Bewertungen der Plantage eine Rolle
# Lösung, die aber mehr Aufwand erfordert: Separate Klasse, z.B. Transaktion, so dass sich Käufe unabhängig von der 
# Pflanze nachvollziehen lassen - wichtig: Es gibt aber keine klare Trennlinie bei der Frage, was Teil einer 
# Klassendefinition ist und was nicht

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

if __name__ == "__main__":
    pass