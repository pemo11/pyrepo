# Übung 3: Einsetzen eines Fensters

import numpy as np

x1 = 4
y1 = 3
z1 = -2

x2 = 3
y2 = 2
z2 = -1

p1 = np.array([x1,y1,z1,1])
p2 = np.array([x2,y2,z2,1])

mT1 = np.array([[1,0,0,-x1],[0,1,0,-y1],[0,0,1,-z1],[0,0,0,1]])
mT2 = np.array([[1,0,0,-x2],[0,1,0,-y2],[0,0,1,-z2],[0,0,0,1]])

# p1A = p1*
p1A = np.dot(mT1, p1)
p2A = np.dot(mT2, p2)
l1 = np.sqrt(np.power(x2-x1,2)+np.power(z2-z1,2))

mDy = np.array([[(z2-z1)/l1,0,(x2-x1)/l1,0],[0,1,0,0],[-(x2-x1)/l1,0,(z2-z1)/l1,0],[0,0,0,1]])

p2B = np.dot(mDy, p2A)

D = np.sqrt(np.power(x2-x1,2)+np.power(y2-y1,2)+np.power(z2-z1,2))

mDx = np.array([[1,0,0,0],[0,l1/D,(y2-y1)/D,0],[0,-(y2-y1)/D,l1/D,0],[0,0,0,1]])
p2C = np.dot(mDx,p2B)

p4 = np.array([4,4,-2,1])
p4C = np.dot(np.dot(np.dot(mDx, mDy),mT2), p4)

# Woher kommen die Werte von x4*** und y4***? In der Zeichnung sind keine Werte enthalten
x4C = 1
y4C = 1

mDz = np.array([[y4C/D,x4C/D,0,0],[0,l1/D,(y2-y1)/D,0],[0,-(y2-y1)/D,l1/D,0],[0,0,0,1]])

print(mDz)
