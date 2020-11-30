# Berechnen des dezibel-Wertes
import math

pWatt = 2.51188643150958

# Berechnen des elektrischen Leistungspegel aus der elektrischen Leistung
dbWert = math.log10(pWatt) * 10

print(f"{pWatt} => {dbWert}dB")

# Berechnen des Spannungspegels

U = 1.2589254117941673

dbVWert = math.log10(U) * 20

print(f"{U} => {dbVWert}dBV")

