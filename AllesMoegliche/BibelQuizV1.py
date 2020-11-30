# Ein kleines Bibel-Quiz für die Konsole
# Erstellt: 14/10/20
# Version 1- Frage/Antwort-Spiel

import random
from os import path
import re

txtPath = path.join(path.dirname(__file__), "Bibelverse.txt")

class BibleVers:

    def __init__(self, vers, origin):
        self.vers = vers
        self.origin = origin

bibleVerses = []

linePattern = "\[([\w,]+)\]"

with open(txtPath, mode="r", encoding="UTF-8") as fh:
    for line in fh:
        line = line[:-1] if line[-1] == "\n" else line
        if re.match(linePattern, line):
            m = re.match(linePattern, line)
            origins = m.groups()[0].split(",")
            origin = f"{origins[0]} {origins[1]}, Vers {origins[2]}"
            bibleVerses.append(BibleVers(verse, origin))
        else:
            verse = line

# print(bibleVerses)

while True:
    z = random.randint(0, len(bibleVerses)-1)
    vers = bibleVerses[z].vers
    origin = bibleVerses[z].origin
    a = input(f"Wo steht \"{vers}\"?")
    if a == "q":
        break
    print(f"Antwort: In {bibleVerses[z].origin}")



