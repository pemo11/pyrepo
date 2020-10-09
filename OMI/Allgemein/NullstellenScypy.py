# Nullstellen per ScyPy
import math

from scipy.optimize import newton

f = lambda  x: 2 * math.pow(x, 4) - 14 * math.pow(x, 2) - 12 * x
f = lambda  x: -2 * math.pow(x, 3) + 30 * math.pow(x, 2) + 50 * x - 750
f = lambda  x: math.pow(x, 3) - 5 * math.pow(x, 2) + 5 * math.pow(x, 2) + 19 * x - 30
# f1 = lambda x: 8 * math.pow(x, 3) - 28 * x - 12

# Erster Versuch - liefert nur die erste Nullstelle -5
nullies = newton(f, 10)
print(nullies)