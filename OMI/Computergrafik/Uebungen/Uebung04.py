# Übung 4 - 3D-Translation
# Gegegeben ist der Punkt P (1,0,1)
# P wird um 2 Einheiten in x- und y-Richtung verschoben, um 90Grad im Uhrzeigersinn um die z-Achse gedreht 
# und dann mit der orthografischen Projektion auf die xy-Ebene projiziert.
# Gesucht sind Matrix und der projizierte Punkt

import numpy as np

mT = np.array([[1,0,0,2],[0,1,0,2],[0,0,1,0],[0,0,0,1]])

# Rotation um 90 Grad => -90 da Uhrzeigersinn cos(-90) = 0 sin(-90) = 1

w = np.radians(-90)
mRot = np.array([[np.cos(w),-np.sin(w),0,0],[np.sin(w),np.cos(w),0,0],[0,0,1,0],[0,0,0,1]])

mOrto = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]])

mGes = np.dot(mOrto, np.dot(mRot, mT))

pNeu = np.dot(mGes, np.array([1,0,1,1]))

print(pNeu)