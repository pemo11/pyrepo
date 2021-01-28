# Übung 5 - Bezier-Kurve mit Casteljau-Algorithmus
# Erstellt: 24/11/20, Umgesetzt am 1/12/20

from GCHelper import *

p = {}
p[(0,0)] = (0,0)
p[(1,0)] = (1,1)
p[(2,0)] = (3,1)
p[(3,0)] = (4,0)

# Skizzieren Sie die Kurve
# Konstruieren Sie den Kurvenpunkt an der Stelle u = 1/3

# Dieser Aufruf stimmt
# casteljau(p)

# Dieser Aufruf stimmt inzwischen auch
p = [(0,0),(1,1),(3,1),(4,0)]
casteljau2(p)
