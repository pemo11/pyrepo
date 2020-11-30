# Beispiel für eine Cubic-Spline-Berechnung
# Erstellt: 29/11/20

import numpy as np

p1 = (1,3)
p2 = (3,5)
p3 = (5,2)

# Aus 6 Koordinaten resultieren 6 Gleichungen = 2 Gleichungen mit jeweils 2 Ableitungen

# Kurve 1:
# y = a1x3 + b1x2 + cx1 + d1
# y' = 3a1x2 + 2b1x + c1
# y'' = 6a1x + 2b1

# Kurve 2:
# y = a2x3 + b2x2 + cx2 + d2
# y' = 3a2x2 + 2b2x + c2
# y'' = 6a2x + 2b2

# Mit 8 Unbekannten resultieren auch 8 Gleichungen
# 0 = 6ax1 + 2by => y1'' = 0
# y1 = a1x1 3 + b1x1 2 + c1x1 + d1 => y1 = f(x1)
# y2 = a1x2 3 + b1x2 2 + c1x2 + d1 => y2 = f(x2)
# y2 = a2x2 3 + b2x2 2 + c2x2 + d2 => y2 = f(x2)
# 3a1x2 2 + 2b1x2 + c1 = 3a2x2 2 + 2b2x2 + c2
# 6a1x2 + 2b1 = 6a2x2 + 2b2
# y3 = a2x3 3 + b2x3 2 + c2x3 + d2 => y3 => f(x3)
# 0 = 6a2x3 + 2b2 => y3'' = 0

# Beispielrechnung für y = x 3 im Bereich 0 bis 1
x1 = 0
y1 = 0
x3 = 1
y3 = 1

# Ein Stützpunkt wird gewählt
x2 = 0.5
y2 = 0.125

# Die 8 Gleichungen werden in eine Matrix übernommen
g1 = [6*x1,2,0,0,0,0,0,0]
g2 = [pow(x1,3),pow(x1,2),x1,1,0,0,0,0]
g3 = [pow(x2,3),pow(x2,2),x2,1,0,0,0,0]
g4 = [0,0,0,0,pow(x2,3),pow(x2,2),x2,1]
g5 = [3*pow(x2,2),2*x2,1,0,-3*pow(x2,2),-2*x2,-1,0]
g6 = [6*x2,2,0,0,-6*x2,-2,0,0]
g7 = [0,0,0,0,pow(x3,3),pow(x3,2),x3,1]
g8 = [0,0,0,0,6*x3,2,0,0]

m1 = np.array([g1,g2,g3,g4,g5,g6,g7,g8])
m2 = np.array([0,0,0.125,0.125,0,0,1,0])

m3 = np.array([1.5,0,-0.125,0,-1.5,4.5,-2.375,0.375])
# Das Ergebnis ist m2
# print(np.dot(m1,m3))

# Problem: m1 * m3 = m2 - wie erhalte ich m3? - Durch Division?
# Das stimmt nicht
print(np.divide(m1,m2))
