#! usr/bin python3
# Übung Nr. 5
# Ein Bild hängt schief und soll gerade gerückt werden
# Koordinate einer Ecke ist (5,8,-7)
# Dazu soll es im Uhrzeigersinn um pi/4 gedreht werden
# Die Drehachse hat die Richtung D = 1/5 * (4,0,3)
# Diese Richtung entspricht der Flächennormalen des Bildes
# Gesucht ist die Rotationsmatrix Mt

# FLächennormale = 90 Grad


import numpy as np

# 1 da Ortsvektor
E = np.array([5,8,-7,1])

# 0 da Richtungsvektor
D = np.array([4,0,3,0])

# Schritt 1: Aufstellen der Translationsmatrix

Mt1 = np.array([1,0,0,5],[0,1,0,-8],[0,0,1,7],[0,0,0,1])

# Schritt 2: Rotation um x-Achse kann entfallen, da die Drehachse bereits in der xz-Ebene liegt

# Schritt 3: Rotationsmatrix für Rotation um y-Achse

# Rechte Randregel ergibt, dass Winkel negativ ist (Drehung im Uhrzeigersinn)

a = 4 / 5
l = 3 / 5

# D = Wurzel aus a2 + b2

# cos -Beta = cos Beta = l / |D| = 3/5

Mdy = np.array([[3/5,0,-4/5],
                [0,1,0,0],
                [4/5,0,3/5,0],
                [0,0,0,1]])

# Schrit 4: Rotation um z-Achse, so dass das Bild gerade steht

w = -pi/4 # 45Grad

Mdz = np.aprray([0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0])

# Schritt 5: Rücktransformation des gesamten Bildes, d.h. der Schritte 3 und 1 - 2 wurde ja nicht durchgeführt

# Es fehlen noch Mdy-1 und Mt-1 ???

Mg = Mt @ Mdy @ Mdz @ Mt1
