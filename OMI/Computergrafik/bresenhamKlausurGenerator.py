# Generiert Fragen zum Bresenalgorithmus für die Klausur Computergrafik
# Erstellt: 19/10/20

import random

anzahl = 5
sign = lambda x: (1, -1)[x<0]

def BresenhamGerade(p1,p2,Anzahl):
    abbruch = False
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    n = 0
    if dx >= dy:
        e = abs(dx) - 2 * abs(dy)
        while not abbruch:
            n += 1
            x += sign(dx)
            if e > 0:
                e -= 2 * abs(dy)
            else:
                y += sign(dy)
                e += 2 * (abs(dx) - abs(dy))
            print(f"x={x}/y={y} mit e={e}")
            if x == x2 or n == anzahl:
                abbruch = True
    else:
        e = abs(dy) - 2 * abs(dx)
        while not abbruch:
            n += 1
            y += sign(dy)
            if e > 0:
                e -= 2 * abs(dx)
            else:
                x += sign(dx)
                e += 2 * (abs(dy) - abs(dx))
            print(f"x={x}/y={y} mit e={e}")
            if y == y2 or n == anzahl:
                abbruch = True

while True:
    abbruch = False
    while not abbruch:
        p1 = [random.randint(-100,100), random.randint(-100,100)]
        p2 = [random.randint(-100,100), random.randint(-100,100)]
        abbruch = abs(p1[0] - p2[0]) > 5 and abs(p1[1] - p2[1]) > 5
    frage = f"Berechne die ersten {anzahl} Koordinaten einer Geraden vom Startpunkt ({p1[0]}/{p2[0]}) bis zum Endpunkt ({p1[1]}/{p2[1]}) (oder Q für Ende)"
    a = input(frage)
    if a.lower() == "q":
        break
    BresenhamGerade(p1, p2, anzahl)
