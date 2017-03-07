import math

def linspace(a, b, n):
    d = float(b - a) / (n - 1)
    return [a + i * d for i in range(0, n)]

X = linspace(-math.pi, math.pi, 100)

Y = [math.sin(x) for x in X]

import matplotlib.pyplot as plt

plt.plot(X, Y)

plt.grid(True, zorder=0.1)

plt.show()