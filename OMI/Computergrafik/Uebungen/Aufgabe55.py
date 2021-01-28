#! python3
# Aufgabe 5.5, Erstellt 09/12/20
# Ein Punkt P = (3,2,4) soll mit dem Winkel 2pi/3 um die Achse g = (0,0,1) + lambda/Wurzel3 (1,1,1) gedreht werden.
# Berechnen Sie den Bildpunkt

import numpy as np
from math import sqrt,sin,cos

# Schritt 1: Verschieben der Rotationsachse in den Ursprung mit Hilfe einer Translationsmatrix

Mt = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,-1],[0,0,0,1]])

# Wie wird Mt hoch -1 gebildet?

Mt1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])

# Schritt 2: Rotation um die x-Achse in der (x,z)-Ebene mit dem Drehwinkel pi/4  - warum pi/4?

# cos(pi/4) = 1 / Wurzel 2 und sin(pi/4) = 1 / Wurzel 2

Mdx = np.array([[1,0,0,0],[0, 1/sqrt(2),1/sqrt(2),0],[0,1/sqrt(2),-1/sqrt(2), 0],[0,0,0,1]])

# Wie wird Mdx hoch -1 gebildet?

Mdx1 = np.array([[1,0,0,0],[0, -1/sqrt(2),-1/sqrt(2),0],[0,-1/sqrt(2),1/sqrt(2), 0],[0,0,0,1]])

# Schritt 3: Rotation um die y-Achse mit dem Drehwinkel -Beta, die den gedrehten Richtungsvektor r = (1,0,Wurzel2) auf die z-Achse abbildet

# MDz(pi/4) hoch -1 = MDz(-pi/4)

Mdy = np.array([[1,0,0,0],[0,1/sqrt(2),1/sqrt(2),0],[0,-1/sqrt(2),1/sqrt(2),0],[0,0,0,1]])
# Wie wird Mdz hoch -1 gebildet?
Mdy1 = np.array([[1,0,0,0],[0,-1/sqrt(2),-1/sqrt(2),0],[0,-1/sqrt(2),1/sqrt(2),0],[0,0,0,1]])

# Rotation der X-Achse um den Winkel gamma?
sinG = sin(2 * 3.14/3)
cosG = cos(2 * 3.14/3)
Mdg = np.array([[1,0,0,0],[0,cosG,-sinG,0],[0,sinG,cosG,0],[0,0,0,1]])

# Was ist der Winkel gamma?
# Hier fehlt noch ein Operand??? aber mit ihm stimmt das Ergebnis überhaupt nicht mehr!
# Mt1 @ Mdx1 @ Mdy1 @ Mdx @ Mdy @ Mt
Mg = Mt1 @ Mdx1 @ Mdy1 @ Mdx @ Mdy @ Mt
# Mg = Mt1 @ Mdx1 @ Mdy1 @ Mdg @ Mdy @ Mdx @ Mt
print(Mg)

p = np.array([3,2,4,1])

MErgebnis = Mg @ p

# Ergebnis stimmt, aber die Matrix Mg stimmt noch nicht - hier sind Zeile 1 und Zeile 2 vertauscht ???
print(MErgebnis)