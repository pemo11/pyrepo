# Bresenham-Berechnung nach Beispiel aus dem OMI-Video
# Die offizielle Version ohne Fließkommazahlen und mit Einbeziehung des Vorgängerwertes
# Erstellt: 30/09/20
# AKtualisiert: 20/11/20 - ist (endlich) mit der Tabelle auf Seite 56 im Skript identisch

'''
x1 = 1
x2 = 4
y1 = 6
y2 = 2

x1 = 111
y1 = -113
x2 = 201
y2 = 65
'''
x1 = 9
y1 = 18
x2 = 14
y2 = 22

x = x1
y = y1

dx = x2 - x1
dy = y2 - y1

xAlt = x1
yAlt = y1

# warum x and?
# lambda x: (1, -1)[x<0] müsste doch reichen?
sign = lambda x: x and (1, -1)[x<0]
n = 0
anzahl = 5

if abs(dx) >= abs(dy):
    abbruch = False
    errorAlt = abs(dx) - 2 * abs(dy)
    error = errorAlt
    print(f"n={n}\tx={x}\ty={y}\te=0")
    while not abbruch:
        n += 1
        x = xAlt + sign(dx)
        if error > 0:
            y = yAlt
            error = errorAlt - 2 * abs(dy)
        else:
            y = yAlt + sign(dy)
            error = errorAlt + 2 * (abs(dx) - abs(dy))
        print(f"n={n}\tx={x}\ty={y}\te={errorAlt}")
        xAlt = x
        yAlt = y
        errorAlt = error
        if x == x2 or n == anzahl:
            abbruch = True
else:
    # x und y vertauscht
    errorAlt = abs(dy) - 2 * abs(dx)
    error = errorAlt
    abbruch = False
    print(f"n={n}\tx={x}\ty={y}\te=0")
    while not abbruch:
        n += 1
        y = yAlt + sign(dy)
        if error > 0:
            x = xAlt
            error = errorAlt - 2 * abs(dx)
        else:
            x = xAlt + sign(dx)
            error = errorAlt + 2 * (abs(dy) - abs(dx))
        print(f"n={n}\tx={x}\ty={y}\te={errorAlt}")
        xAlt = x
        yAlt = y
        errorAlt = error
        if y == y2 or n == anzahl:
            abbruch = True
