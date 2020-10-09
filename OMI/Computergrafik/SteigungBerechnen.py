# Geradensteigung-Berechnen
# Erstellt: 27/09/20

def Steigung(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return (y2-y1)/(x2-x1)

p1 = (1,1)
p2 = (2,4)

print(Steigung(p1,p2))