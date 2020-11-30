# Berechnen einer Rotationsmatrix
# Erstellt: 5/11/20

import numpy as np
from math import *

w = 90
wBogen = radians(w)

# mRot = np.array((cos(wBogen) - sin(wBogen), (sin(wBogen), cos(wBogen))))
mRot = np.array(((0,-1), (1,0)))
mPunkt = np.array((2,3))
pNeu =np.dot(mPunkt, mRot) 
print(pNeu)