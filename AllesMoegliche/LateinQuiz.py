# Ein Latein-Merkquiz
import os
import random

basePfad = os.path.dirname(__file__)
txtPfad = os.path.join(basePfad, "LateinZitate.txt")

zitate = []
with open(txtPfad, encoding="UTF-8") as fh:
    for zitat in fh:
        if zitat[-1] == "\n":
            zitat = zitat[:-1]
        zitate.append(zitat.split(":"))

anzahl = 10
fragen = []

for i in range(1, anzahl+1):
    while True:
        z = random.randint(0, len(zitate)-1)
        frage = zitate[z][0]
        if len([f for f in fragen if f[0] == frage]) == 0:
            antworten = ["","","",""]
            aIndex = random.randint(0, 3)
            antworten[aIndex] = zitate[z][1]
            # Drei weitere Antworten suchen, die nicht gleich der Frage sind
            for j in [k for k in range(0,4) if k != aIndex]:
                while True:
                    z1 = random.randint(0, len(zitate)-1)
                    antwort = zitate[z1][1]
                    if not antwort in antworten:
                        break
                antworten[j] = antwort
            fragen.append((frage, antworten, aIndex))
            break
print(f"Das Quiz ist mit {anzahl} Fragen bereit.")

print(fragen)

anzahlRichtig = 0
anzahlFalsch = 0

for i in range(1, anzahl):
    print("Was bedeutet %s?" % fragen[i][0])
    for j, antwort in enumerate(fragen[i][1]):
        print(chr(j+65) + ". " + antwort)
    a = input("A,B,C oder D oder Q für Abbruch?")
    if a == "Q":
        break
    antwort = fragen[i][2]
    if ord(a)-65 == antwort:
        print("Die Antwort war richtig!")
        anzahlRichtig += 1
    else:
        print("Leider falsch!")
        print("Richtig wäre %s" % fragen[i][1][antwort])
        anzahlFalsch += 1

print(f"Richtige Antworten: {anzahlRichtig} Falsche Antworten: {anzahlFalsch} - Deine Quote: {(anzahlRichtig/anzahl):.0%}")

