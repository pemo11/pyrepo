# Berechne mit dem Bresenham-Geraden-Algorithmus die Koordinanten der ersten 3 Pixel einer Geraden
# mit Anfangspixel 1,6 und Endpixel 4,2 und gebe die Entscheidungsvariable en an

sign = lambda x: x and (1, -1)[x<0]

def Bresenham(p1,p2,anzahl=5):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    n = 0
    en = 0
    if abs(dx) >= abs(dy):
        en = abs(dx) - 2 * abs(dy)
        print(f"n={n}: x={x}/y={y} mit e={en}")
        abbruch = False
        while not abbruch:
            n += 1
            x += sign(dx)
            if en > 0:
                en -= 2 * abs(dy)
            else:
                y += sign(dy)
                en += 2 * (abs(dx) - abs(dy))
            print(f"n={n}: x={x}/y={y} mit e={en}")
            if x == x2 or n > anzahl:
                abbruch = True
    else:
        en = abs(dy) - 2 * abs(dx)
        print(f"n={n}: x={x}/y={y} mit e={en}")
        abbruch = False
        while not abbruch:
            n += 1
            y += sign(dy)
            if en > 0:
                en -= 2 * abs(dx)
            else:
                x += sign(dx)
                en += 2 * (abs(dy) - abs(dx))
            print(f"n={n}: x={x}/y={y} mit e={en}")
            if y == y2 or n > anzahl:
                abbruch = True
p1 = (1,6)
p2 = (4,2)


# p1 = (111,-113)
# p2 = (201,65)
Bresenham(p1, p2, 5)