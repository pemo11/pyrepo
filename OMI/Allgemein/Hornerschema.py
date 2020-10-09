# Hornerschema ganz einfach

def horner(Ac, Ax, x):
        y = 0
        for i in range(len(Ax) - 1, 0, -1):
            y *= (x - Ax[i] + Ac[i])
        return y

# Nur wie wird sie aufgerufen???

# Bsp. 2x3 - 4x2 + 8x - 4
Ac = [2,-4,8,4]
Ax = [3,2,1,0]
x = 0

# ??? noch nicht getestet
horner(Ac, Ax, x)
