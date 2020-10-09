# Zeichnen von mathematischen Funktionen
import math
import numpy as np
import matplotlib.pyplot as plt

# x2 - -1
def f1(x):
    return  x * x - 1

def f2(x):
    return  x*x

x = np.linspace(-10, 10, 20, True)
y = f2(x)
plt.axis([-20, 20, 0, 100])
plt.plot(x, y, color="blue", linewidth=1.5)
plt.show()

