# Grenzwert berechnung

import math

# f = lambda x: (math.pow(x, 3) +  7 * math.pow(x, 2) + 4 * x - 12) / (math.pow(x, 2) + 5 * x + 6)

def f(x):
    return  (math.pow(x, 3) +  7 * math.pow(x, 2) + 4 * x - 12) / (math.pow(x, 2) + 5 * x + 6)
    
# Grenzwertberechnung für x geht gegen 0

nullstellen = [-2,-3]

for x in range(-10, 0):
    if x in nullstellen:
        continue
    print("f(%d) = %2.f" % (x,f(x)))


