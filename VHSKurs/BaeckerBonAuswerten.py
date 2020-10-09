# Auswerten eines Bons mit einer Prise Regex
# Der Bon stammt aus einer echten Bäckerei und wurde zuvor eingescannt und die Pdf-Datei
# per OCR in eine Textdatei konvertiert, z.B. https://www.onlineocr.net/
# Das Beispiel funktioniert! Letzter Stand: 12/01/2002
import os
import re

class Produkt:

    def __init__(self, Nr, Bezeichnung, Betrag):
        self.Nr = Nr
        self.Preis = Betrag
        self.Bezeichnung = Bezeichnung

class Bon:

    def __init__(self, Datum, Filiale):
        self.Datum = Datum
        self.Produkte = []
        self.Filiale = Filiale
        self.Total = 0
        self.Total2 = sum([p.Preis for p in self.Produkte])

    def __toString__(self):
        return f"Datum: {self.Datum} - Filiale: {self.Filiale} - Total: {self.Total} - Anzahl Produkte: {len(self.Produkte)}"

txtPfad = os.path.dirname(__file__)
txtPfad = os.path.join(txtPfad, "BaeckerBon_Eingescannt.txt")

produkte = []

# Alle Zeilen "vorverarbeiten"
with open(txtPfad, mode="r", encoding="utf-8") as fh:
    for zeile in fh:
        if zeile.startswith("#"):
            m = re.match(r"#(\d+)\s+([a-zA-Z\s\däüö]+)\s{2,}.*([0-9,]+)", zeile)
            nr = m.groups()[0]
            bezeichnung = m.groups()[1]
            betrag = m.groups()[2]
            produkte.append(Produkt(nr, bezeichnung, betrag))
        elif zeile.startswith("Total"):
            total = re.match(r"Total\s+([0-9,\s]+)", zeile).groups()[0]
            # Leerzeichen entfernen
            total = total.replace(" ", "")
        elif zeile.startswith("Filiale"):
            m = re.match(r"Filiale\s(\w+)", zeile)
            filiale = m.groups()[0]
        elif re.match(r"(\d+:\d\d)\s(\d+.\d+.\d{4})", zeile):
            datum = re.match(r"(\d+:\d\d)\s(\d+.\d+.\d{4})", zeile).groups()[0]
            uhrzeit = re.match(r"(\d+:\d\d)\s(\d+.\d+.\d{4})", zeile).groups()[1]
            datum = datum + " " + uhrzeit

# Neues Bon-Objekt anlegen
b1 = Bon(datum, filiale)
b1.Produkte = produkte
b1.Total = total

# Und ausgeben
print(b1.__toString__())
