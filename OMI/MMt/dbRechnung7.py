# Absolute Pegelmasse
# Erstellt: 30/10/20

import math

def DbuBerechnung(Ueff):
    return 20 * math.log10(Ueff/0.775)

dBu = DbuBerechnung(1)

print("dBu=%.2f" % dBu)