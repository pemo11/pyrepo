# Matrix-Multiplikation mit numpy
# Erstellt: 09/11/20

import numpy as np

punkte = [(20,20), (140,20), (140,60), (120,80), (60,80), (40, 220), (20,80)]

def MatrixMul(m, v):
    # Leere Matrix mit Nullen anlegen
    vR = [0 for _ in range(len(v))]
    for i  in range(len(m)):
        for j in range(len(m)):
            vR[i] += m[i][j] * v[j]
    return vR

def Rotate1(t, w):
    p = [t[0],t[1]]
    m = [[np.cos(w),-np.sin(w)],[np.sin(w),np.cos(w)]]
    m3 = MatrixMul(m, p)
    return m3

def Rotate2(p, w):
    w = np.radians(w)
    # Auch hier: Liste =  Zeile
    mRot = np.array([[np.cos(w),-np.sin(w)], [np.sin(w),np.cos(w)]])
    return np.dot(mRot,punkt)

for punkt in punkte:
    punktNeu = Rotate1(punkt, 90)
    print(f"Aus {punkt} wird {punktNeu}")
