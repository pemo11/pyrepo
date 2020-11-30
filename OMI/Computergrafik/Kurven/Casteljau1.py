# Kurvenberechnung nach Casteljau
# Erstellt: 29/11/20

import numpy as np
import decimal
p1 = (1,1)
p2 = (2,4)
p3 = (4,3)
p4 = (5,0)
l = np.array([p1,p2,p3,p4])

def casteljau(l):
    n = 3   # Kurvengrad, in der Regel 3 
    a = len(l)
    du = 1 / (a - 1)
    u = du
    while u < 1:
        for j in range(0,n):
            for i in range(0,n-j):
                pNeu = (1-u) * l[i] + u * l[i+1]
            print(f"p={pNeu}")
        u += du

casteljau(l)