# 3D-Rotation aus Übungsaufgabe im Video 3D-Transformationen
# Erstellt: 22/11/20

import numpy as np

p1 = np.array([1,2,0,1])

w = np.radians(90)

# Schritt 1: Rotation um 90 Grad um x-Achse
MRotX = np.array([[1,0,0,0],[0,np.cos(w),-np.sin(w),0],[0,np.sin(w),np.cos(w),0],[0,0,0,1]])
print("Rotation um die x-Achse:")
p2 = np.dot(MRotX,p1)
print(p2)

# Schritt 2: Rotation um 90 Grad um z-Achse
MRotZ = np.array([[np.cos(w),-np.sin(w),0,0],[np.sin(w),np.cos(w),0,0],[0,0,1,0],[0,0,0,1]])
print("Rotation um die z-Achse:")
p3 = np.dot(MRotZ, p2)
print(p3)

# Schritt 3: Skalierung um Faktor 2 in y-Richtung
MFak2 = np.array([[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]])
p4 = np.dot(MFak2, p3)
print("Skalierung um Faktor 2 in y-Richtung:")
print(p4)

# Schritt 4: Verschiebung um -2 in y-Richtung und -2 in z-Richtung
MTrans = np.array([[1,0,0,0],[0,1,0,-2],[0,0,1,-2],[0,0,0,1]])
p5 = np.dot(MTrans, p4)
print("Verschiebung um -2 in y-Richtung und um -2 in z-Richtung:")
print(p5)

# p5 stimmt !

# Gesamt-Matrix - genial einfach dank @ (wie * in matlab)
MG = MTrans @ MFak2 @ MRotZ @ MRotX

# Stimmt nicht
p6 = np.dot(MG, p1)

print("Ergebnis der Gesamt-Matrix:")
print(p6)