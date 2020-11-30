# Geben Sie die Abbildungsmatrix Mt einer 2D-Transformation an, die den Punkt
# [6,8,2] auf den Punkt [-9,6,3] abbildet

import numpy as np

# Gleich in homogenen Koordinaten angeben
p1 = np.array([6,8,2,1])
p1n = np.array([3,4,1])
p2 = np.array([-9,6,3,1])
p2n = np.array([-3,2,1])

mT = np.array([[1,0,p2n[0]-p1n[0]],[0,1,p2n[1]-p1n[1]],[0,0,1]])

# Sollte stimmen, da der Punkt [-3,2,1] resultiert
print(np.dot(mT,p1n))