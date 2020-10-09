# Eine typische Übungsaufgabe für Programmieranfänger
# Gibt zu einer beliebigen Anzahl an Buchstaben deren Abstände im Alphabet aus
# Schritt 1: Eingabe Schritt 2: Eingabe zerlegen Schritt 3: Alle Buchstaben durchgehend und Abstand vom Nachbarn ausgeben

buchstaben = input("Buchstaben?")

# Alle Buchstaben ohne Komma

'''
# Einfach
for b in buchstaben:
     if b != ",":
        print(b)
# Pythonisch
for b in [b1 for b1 in buchstaben if b1 != ","]:
    print(b)
'''
# Nun die große Frage: Wie stelle ich eine Beziehung zu dem letzten Buchstaben her?
letzterBuchstabe = ""

for b in [b1 for b1 in buchstaben if b1 != ","]:
    print(ord(b) - ord("a") + 1)
    if letzterBuchstabe != "":
        abstand = abs(ord(letzterBuchstabe) - ord(b))
        print("Abstand: %d" % abstand)
    letzterBuchstabe = b
