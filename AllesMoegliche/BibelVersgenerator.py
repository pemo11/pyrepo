# Ausgabe eines Bibelverses per Zufallszahlengenerator
# Erstellt: 14/10/20

import random
from os import path
import re

txtPfad = path.join(path.dirname(__file__), "Bibelverse.txt")

bibleVerses = []

with open(txtPfad, mode="r", encoding="UTF-8") as fh:
    originText = ""
    for zeile in fh:
        zeile = zeile[:-1] if zeile[-1] == "\n" else zeile
        if re.match("\[([\w,]+)\]", zeile):
            m = re.match("\[([\w,]+)\]", zeile)
            origins = m.groups()[0].split(",")
            originText = f"{origins[0]} {origins[1]}, Vers {origins[2]}"
        elif originText != "":
            bibleVerses.append((zeile, originText))
            originText = ""

# print(bibleVerses)

z = random.randint(0, len(bibleVerses))

print(f"{bibleVerses[z][0]} ({bibleVerses[z][1]})")



