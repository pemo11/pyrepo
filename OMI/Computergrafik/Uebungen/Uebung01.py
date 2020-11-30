# Übung 1 - Drehung um 90 Grad, aus dem Chat vom 24.10.20
# Gegeben ist das Dreieck ABC mit den Punkten A(0,1),B(3,2) und C(1,3)
# Gesucht ist die Drehung mit w=90 Grad um den Ursprung

import numpy as np

mRot = np.array([[0,-1],[1,0]])
m1 = np.array([[0,3,1], [1,2,3]])

# Stimmt
print(np.dot(mRot, m1))

# Geht nicht wegen unterschiedlicher Dimensionen
# print(np.dot(m1, mRot))

punkte = [(0,1),(3,2),(1,3)]
# Stimmt auch
for p in punkte:
    print(np.dot(mRot, p))