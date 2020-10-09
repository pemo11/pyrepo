# Bresenham-Berechnung nach Beispiel aus dem OMI-Video
# Die offizielle Version ohne Fließkommazahlen und mit Einbeziehung des Vorgängerwertes
# Erstellt: 30/09/20

x1 = 0
x2 = 10
y1 = 0
y2 = 4

'''
x1 = 111
x2 = 201
y1 = -113
y2 = 65
'''
x = x1
y = y1

dx = x2 - x1
dy = y2 - y1

error = abs(dx) - 2 * abs(dy)

sign = lambda x: x and (1, -1)[x<0]

if abs(dx) >= abs(dy):
    while x < x2:
        x = x1 + sign(dx)
        if error > 0:
            y = y1
            error -= 2 * abs(dy)
        else:
            y = y1 + sign(dy)
            error += 2 * (abs(x) - abs(y))
        print(f"x:{x} y:{y} e:{error}")
        x1 = x
        y1 = y
else:
    # x und y vertauscht
    while y < y2:
        y = y1 + sign(dy)
        if error > 0:
            x = x1
            error -= 2 * abs(dx)
        else:
            x = x1 + sign(dx)
            error += 2 * (abs(x) - abs(y))
        print(f"x:{x} y:{y} e:{error}")
        y1 = y
        x1 = x
