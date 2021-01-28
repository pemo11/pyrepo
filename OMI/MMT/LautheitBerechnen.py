#! usr/bin python3
# Berechnen der Lautheit
# Erstellt: 08/12/20

import math

abbruch = False
while not abbruch:
    so = int(input("Lautheit in sone?"))

    Ls = 40 + math.log2(so) * 10

    print(f"Lautstärke={Ls} dBSPL")

    a = input("Weitere Berechnung? (J/N)").lower()

    abbruch = True if a != "j" else False