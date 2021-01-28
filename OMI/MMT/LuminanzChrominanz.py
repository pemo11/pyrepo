#! usr/bin python3
# Erstellt: 11/01/21

import numpy as np

def Luminanz(R,G,B):
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    return round(Y,3)

def Chrominanz(B,R,Y,G):
    mLum = np.array([[0.299, 0.587, 0.114],
                   [-0.299, -0.587, 0.886],
                   [0.701, -0.587, -0.114]])
    mRGB = np.array([R,G,B])

    return mLum @ mRGB

# B - Y = B - (0.299 * R + 0.587 * G + 0.114 * B) = -0.299 * R - 0.587 * G + (1 - 0.114) * B = -0.299 * R - 0.587 * G + 0.886 * B

# R - Y = R - (0.299 * R + 0.587 * G + 0.114 * B) = (1 -0.299) * R - 0.587 * G - 0.114 * B = 0.701 * R - 0.587 * G - 0.114 * B

# Berechnen einer Luminanz
R = 0.9
G = 0.9
B = 0.1

print(Luminanz(R,G,B))

R = 0.5
G = 0.5
B = 0.5

print(Luminanz(R,G,B))

# Vollgesättigtes Gelb
R = 1
G = 1
B = 0
print(Luminanz(R,G,B))

