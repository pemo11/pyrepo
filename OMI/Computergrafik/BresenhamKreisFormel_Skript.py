# Kreisberechnung nach Bresenham - Formel aus dem Skript
# Erstellt: 17/10/20
# Stimmt noch nicht, Übungsaufgabe 3.4 lässt sich damit nicht nachvollziehen

xMitte = 100
yMitte = 1003
r = 10

xOffset = 10

x = 0
y = r
n = 0
anzahl = 5

e = 5 - 4 * r

yAlt = y
xAlt = x
eAlt = e
while x < y and n <= anzahl:
    n += 1
    x += 1
    if e > 0:
        y = yAlt - 1
        e = eAlt + 8 * (xAlt-yAlt) + 20
    else:
        y = yAlt
        e = eAlt + 8 * xAlt + 12
    print(f"n={n} e={e} x={x} y={y} x+xMitte={x+xMitte} y+yMitte={y+yMitte}")
    xAlt = x
    yAlt = y
    eAlt = e

