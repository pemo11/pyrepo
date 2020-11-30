# Bresenham-Kreis nach Fellner-Buch
# Erstellt: 17/10/20
# Gilt für den 2. Oktanden, liefert auch nicht die Werte der Tabelle auf Seite im Skript
xMitte = 100
yMitte = 1003
r = 10

y = r
x = 0
e = 1 - r

while x < y:
    print(x,y,e)
    x += 1
    if e < 0:
        y -= 1
        e -= 2 * x * y
    e += 2 * x + 1
