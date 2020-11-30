# Matrix-Multiplikation mit numpy
# Erstellt: 06/11/20

import numpy as np

# Auch hier: Liste =  Zeile

m1 = np.array([[8,12,-11],[14,7,3],[-6,4,21]])
m2 = np.array([[3,9,-1],[16,7,3],[-6,-4,13]])

m3 = m1.dot(m2)

print(m3)

# Multiplikation für eine Translation um den Ursprung

w = 180
w = np.radians(w)
m1 = np.array([[int(np.cos(w)), int(-np.sin(w)), 0], [int(np.sin(w)), int(np.cos(w)), 0], [0,0,1]])

print(m1)