# Vigenére Chiffre
# Umsetzung am 9.06.2020 - eventuell mache ich daraus ein Büchlein
# Python-Programme für das OMI-Studium
# Oder ein Buch: Python fürs Studium mit diesen Beispielen

# Schritt 1: 26x26 Feld mit den jeweils pro Spalte um einen Buchstaben versetzen Buchstaben von A bis Z

# Thereotisch ließe sich das Fels auch gleich per List Comprehension passend füllen
vigFeld = [[0 for i in range(0,26)] for j in range(0,26)]

offset = 0

# Ergebnis stimmt, kann aber eventuell vereinfacht werden
for i in range(0,26):
    for j in range(0,26):
        c = j + offset + 65
        c = c - 26 if c > 90 else c
        vigFeld[i][j] = chr(c)
    offset += 1
 
for i in range(0,26):
    print(vigFeld[i])

# Das Wort "SEMESTER" soll verschüsselt werden
wort = "SEMESTER"
wort = "INFORMATIONSSICHERHEITSMANAGEMENTSYSTEM"
schluessel = "SICHER"
geheim = ""

k = 0
for c in wort:
    i = ord(c) - 65
    j = ord(schluessel[k]) - 65
    k = k + 1 if k < len(schluessel) - 1 else 0
    geheim += vigFeld[i][j]

# Stimmt - aus SEMESTER wird KMOLWKWZ
print(geheim)

# Wie muss eine Entschlüsselungsfunktion aussehen?
wort = geheim
schluessel = "SICHER"
klartext = ""

k = 0
for c in wort:
    # Hole die Nr der Zeile
    j = ord(schluessel[k]) - 65
    # Hole die Nr Spalte, in der der Buchstabe c enthalten ist
    # Die Variable _ ist nur der Form halber dabei, um den Index zu erhalten
    i = [l for l,_ in enumerate(vigFeld[j]) if vigFeld[j][l] == c][0] 
    klartext += chr(i+65)
    k = k + 1 if k < len(schluessel) - 1 else 0

print(klartext)

