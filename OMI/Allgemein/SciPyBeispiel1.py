# Ein Beispiel für SciPy
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

class Parameter:
    def __init__(self, value):
            self.value = value

    def set(self, value):
            self.value = value

    def __call__(self):
            return self.value

def fit(function, parameters, y, x = None):
    def f(params):
        i = 0
        for p in parameters:
            p.set(params[i])
            i += 1
        return y - function(x)

    if x is None: x = np.arange(y.shape[0])
    p = [param() for param in parameters]
    return optimize.leastsq(f, p)

# giving initial parameters
mu = Parameter(7)
sigma = Parameter(3)
height = Parameter(5)

gaussian = lambda x: 3*np.exp(-(30-x)**2/20.)
data = gaussian(np.arange(100))

X = np.arange(data.size)
x = np.sum(X*data)/np.sum(data)
width = np.sqrt(np.abs(np.sum((X-x)**2*data)/np.sum(data)))

max = data.max()

fit = lambda t : max*np.exp(-(t-x)**2/(2*width**2))

plt.plot(data, '.')
plt.plot(fit(X), '-')
plt.show()
# plt.savefig("Gauss1.png")
