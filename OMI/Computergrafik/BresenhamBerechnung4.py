# Berechnung der Linienkoordinaten nach dem Bresenham-Algorithmus (ohne Zeichen)
# Erstellt: 19/10/20 -  wie Beispiel 3, nur ohne xOld/yOld, da beide Hilfsvariablen doch nicht benötigt werden
# Der Umstand, dass es im Skript xn und xn-1 gibt, muss nicht bei der Umsetzung berücksichtigt werden, das
# ergibt sich automatisch aus z.B. x -= 1 => xn = xn - 1 - 1

import math

x1 = 111
x2 = 201
y1 = -113
y2 = 65

x = x1
y = y1

dx = x2 - x1
dy = y2 - y1

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
            en -= 2 * dy
        else:
            y += sign(dy)
            en += 2 * (abs(dx) - abs(dy))
        print(f"x={x}/y={y} mit e={en}")
        if x == x2 or n == anzahl:
            abbruch = True
else:
    en = abs(dy) - 2 * abs(dx)
    while not abbruch:
        n += 1
        y += sign(dy)
        if en > 0:
            en -= 2 * abs(dx)
        else:
            x += sign(dx)
            en += 2 * (abs(dy) - abs(dx))
        print(f"x={x}/y={y} mit e={en}")
        if y == y2 or n == anzahl:
            abbruch = True
