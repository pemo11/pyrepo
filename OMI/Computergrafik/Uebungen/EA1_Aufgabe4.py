# Eine quadratische Fensterscheibe mit 1m Kantenlänge soll in einer Wand eingesetzt werden
# Eckpunkte der Scheibe sind F1=(0,0,1) F2=(0,0,2) F3=(1,0,2) F4=(1,0,1)
# Eckpunkte des Fensterrahmens sind R1=(-1,1,0) R2=(-1,1,1) R3=(-1,2,1) R4=(-1,2,0)
# Gesucht sind die Matrixen für die einzelnen Transformationen und die Gesamtmatrix

# Stand: 21/11/20 - könnte stimmen - das Egebnis "stimmt" jedenfalls
import numpy as np

# Schritt 1: Umstellen aller Punkte auf homogene Koordinaten
f1 = np.array([0,0,1,1])
f2 = np.array([0,0,2,1])
f3 = np.array([1,0,2,1])
f4 = np.array([1,0,1,1])

r1 = np.array([-1,1,0,1])
r2 = np.array([-1,1,1,1])
r3 = np.array([-1,2,1,1])
r4 = np.array([-1,2,0,1])

# Schritt 2: Translationsmatrix für Translation in den Urpsrung
x1 = f1[0]
y1 = f1[1]
z1 = f1[2]

mT1 = np.array([[1,0,0,-x1],[0,1,0,-y1],[0,0,1,-z1],[0,0,0,1]])

# f1A = np.dot(mT1, f1)

# Schritt 3: Rotation um 90 Grad um die Z-Achse
w = 90
wr = np.radians(w)
mRot = np.array([[np.cos(wr),-np.sin(wr),0,0],[np.sin(wr),np.cos(wr),0,0],[0,0,1,0],[0,0,0,1]])

# f1B = np.dot(mRot, f1A)

# Schritt 4: Translationsmatrix für Translation in den Zielpunkt
# nur x geht in die negative Richtung
x1 = -r1[0]
y1 = r1[1]
z1 = r1[2]

mT2 = np.array([[1,0,0,x1],[0,1,0,y1],[0,0,1,z1],[0,0,0,1]])

# mG = mT1 * mRot * mT2
mG = np.dot(mT1, np.dot(mRot, mT2))
print(np.dot(mG, f1))
print(np.dot(mG, f2))
print(np.dot(mG, f3))
print(np.dot(mG, f4))
