# Ein kleines Bibel-Quiz für die Konsole
# Erstellt: 14/10/20
# Version 2 - Multiplechoice-Antwort

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

while True:
    # Vier Fragen per Zufallsgenerator ausgewählten
    choices = []
    for _ in range(0,4):
        while True:
            z = random.randint(0,len(bibleVerses) - 1)
            if not z in choices:
                choices.append(z)
                break
    # Aus der Liste mit Indices eine Liste mit Objekten machen
    choices = [bibleVerses[i] for i in choices]
    # Den Vers für die Frage auswählen
    z = random.randint(0,len(choices) - 1)
    question = choices[z]
    # Den Vers ausgeben
    print(question.vers + "\n")
    # Die vier möglichen Antworten ausgeben
    for i, choice in enumerate(choices):
        print(f"{chr(i+65)}) {choice.origin}")
    prompt = "\n" + ",".join([chr(i+65) for i in range(0, len(choices))])
    prompt += f" oder Q für Abbruch?"
    lastChoice = chr(len(choices) + 64)
    inp = input(prompt)
    if inp.upper() == "Q":
        break
    # Im erlaubten Bereich?
    if inp < "A" or inp > lastChoice:
        print(f"Die Auswahl muss im Bereich A bis {lastChoice} liegen.")
        continue
    # Richtig oder Falsch?
    a = ord(inp) - 65
    if question.origin == choices[a].origin:
        print("\nDie Antwort war richtig!\n")
    else:
        print(f"\nLeider falsch! - richtig ist {question.origin} \n")
