# Wurzelberechnung durch Reihenentwicklung
import math
a = 120
c = 10
n = 1

for i in range(0,10):
    n = (n + a / n)  / 2

print(n)
print(math.sqrt(a))