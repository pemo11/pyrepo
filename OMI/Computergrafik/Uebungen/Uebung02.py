# Übung 2 - 2D-Transformation
# Geben Sie eine Matrix M an, die eine Punktspielegung (Rotation um 180 Grad) im Punkt (1,1) durchführt
# Überprüfen Sie die Berechnung mit einem beliebigen Punkt

import numpy as np

# Schritt 1: Translation des Punktes (1,1) in den Ursprung

# Aufstellen der Translationsmatrix T1 bei der der Verschiebevektor (-1,-1) eingesetzt wird

mT1 = np.array([[1,0,-1],[0,1,-1],[0,0,1]])

# Schritt 2: Rotation um 180 Grad
w = 180
w = np.radians(w)
# Austellen der allgemeinen Rotationsmatrix
mRot = np.array([[np.cos(w), -np.sin(w), 0], [np.sin(w), np.cos(w), 0], [0,0,1]])
mRot = np.array([[-1, 0, 0], [0, -1, 0], [0,0,1]])

# Schritt 3: Translation in den Punkt (1,1)

# Erneutes Aufstellen einer Translationsmatrix mit dem Verschiebevektor (1,1)

mT2 = np.array([[1,0,1],[0,1,1],[0,0,1]])

# Ausmultiplizieren der drei Matrizen in der richtigen Reihenfolge 
# mG = MT2 * MRot * MT1
# Wird die Reihenfolge vertauscht, entsteht eine andere Matrix!
mG = np.dot(np.dot(mT2,mRot),mT1)
print(mG)

# Überprüfen mit einem Punkt (2,2), der um 180 Grad um 1/1 rotiert auf den Punkt 0/0 abgebildet wird
# Der Punkt muss in homogenen Koordinaten angegeben werden
mTest = np.dot(mG, np.array([2,2,1]))
mPruef = np.array([0,0,1])
print((mTest == mPruef).all())