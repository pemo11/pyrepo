# Berechnen von Bernstein-Polynomen
# Erstellt: 05/12/20

import numpy as np
from math import pow, factorial

u = 2

# Es kommt ein Ergebnis heraus, aber welchen Sinn ergibt es?
for i in range (1,10):
    b = factorial(3)/(factorial(i)*factorial(3-u)) * pow(u, i) * pow(1-u, 3-i)
    print(b)