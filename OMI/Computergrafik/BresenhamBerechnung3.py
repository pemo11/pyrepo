# Berechnung der Linienkoordinaten nach dem Bresenham-Algorithmus (ohne Zeichen)
# Erstellt: 26/09/20 - stimmt mit dem Beispiel auf Seite 56/Skript überein

import math

x1 = 111
x2 = 201
y1 = -113
y2 = 65

x = x1
y = y1

dx = x2 - x1
dy = y2 - y1

xOld = 0
yOld = 0

# int(True) = 1!
sign = lambda x: x and (1, -1)[x<0]
anzahl = 5
n = 0
abbruch = False
if dx >= dy:
    en = abs(dx) - 2 * abs(dy)
    while not abbruch:
        n += 1
        x += sign(dx)
        if en > 0:
            y = yOld
            en -= 2 * dy
        else:
            y = yOld + sign(dy)
            en += 2 * (abs(dx) - abs(dy))
        print(f"x={x}/y={y} mit e={en}")
        yOld = y
        if x >= x2 or n == anzahl:
            abbruch = True
else:
    en = abs(dy) - 2 * abs(dx)
    while not abbruch:
        n += 1
        y += sign(dy)
        if en > 0:
            x = xOld
            en -= 2 * abs(dx)
        else:
            x += sign(dx)
            en += 2 * (abs(dy) - abs(dx))
        print(f"x={x}/y={y} mit e={en}")
        xOld = x
        if y >= y2 or n == anzahl:
            abbruch = True
