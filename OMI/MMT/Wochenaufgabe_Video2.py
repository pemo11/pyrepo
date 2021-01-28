#! usr/bin/python3
# Erstellt: 22/01/21
# Wochenausgaben - Zusatzaufgabe Video2  - Berechnen von Abtastraten

def DatenrateBerechnen(rate):
    Q = 10 # Bits
    fY = 74.25E6 / 4
    fG = 0
    for r in rate[::2]:
        fG += int(r) * fY
    fG *= Q / 1E9
    return fG


# Berechnen der Datenrate für 1080i/25
pixel = 1080 * 25 / 4

rate = "4:2:2"
fG = DatenrateBerechnen(rate)
print(f"{fG} GBit/s")

fG2 = fG * pixel
print(f"{fG2} GBit/s")

