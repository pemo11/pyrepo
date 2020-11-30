# Bresenham-Berechnung nach Beispiel aus dem OMI-Video
# In der sehr einfachen Version wird der Algorithmus noch nicht richtig umgesetzt
# Es kommen Fließkommazahlen vor und die Genauigkeit ist nicht gut
# Erstellt: 30/09/20

x1 = 0
x2 = 10
y1 = 0
y2 = 4

x = x1
y = y1

dx = x2 - x1
dy = y2 - y1

steigung = dy / dx

error = 0

sign = lambda x: x and (1, -1)[x<0]

while x < x2:
    print(f"x:{x} y:{y} e:{round(error,1)}")
    x += 1
    error += steigung
    if error > 0.5:
        y += 1
        error -= 1
