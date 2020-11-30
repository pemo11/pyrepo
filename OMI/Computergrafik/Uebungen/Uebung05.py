# Übung 5 - Bezier-Kurve mit Casteljau-Algorithmus
# Erstellt: 24/11/20

import numpy as np

P0 = np.array([0,0])
P1 = np.array([1,1])
P2 = np.array([3,1])
P3 = np.array([4,0])

# Skizzieren Sie die Kurve
# Konstruieren Sie den Kurvenpunkt an der Stelle u = 1/3
pListe = [P0,P1,P2,P3]

u = 1/3
pAlt = P0
for P in pListe[1:]:
    pNeu = (1-u) * pAlt + u * P
    print(pNeu)
    pAlt = P
