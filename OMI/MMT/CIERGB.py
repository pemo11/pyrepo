#! usr/bin/python3
# Erstelllt: 16/01/21
# CIE RGB Color Matching
# Könnte stimmen, stimmt aber vermutlich noch nicht, da die Ergebnisse für alle Lambdas sehr ähnlich sind
# Formel setzt die Gauss-Formel für die Normalverteilung um
# X = "ergibt" sich aus Rezeptorkurven und ist nicht negativ
# Y = Luminanz
# Z = entspricht dem Blau-Anteil
from math import exp,pow

l = [
    [[1056,5998,370,310],[362,4420,160,287],[-65,5011,204,262]],
    [[821,5888,489,405],[286,5389,163,311]],
    [[1217,4370,118,368],[681,4590,260,138]]
]

# in Angström ?
w = 5000
for l1 in l:
    # print([g[0] / 1000 * exp(-((w - g[1])/pow(g[2] if w < g[1] else g[3],2) / 2)) for g in l1])
    x = sum([g[0] / 1000 * exp(-((w - g[1])/pow(g[2] if w < g[1] else g[3],2) / 2)) for g in l1])
    print(x)

# Verbesserte Version mit Generator ?
def calcXYZ(vars):
    l = vars[0]
    u = vars[1]
    s1 = vars[2]
    s2 = vars[3]
    yield sum([u / 1000 * exp(-((w - s1) / pow(s1 if l < u  else s2, 2) / 2)) for g in l1])

