import math

def linspace(a, b, n):
    d = float(b - a) / (n - 1)
    return [a + i * d for i in range(0, n)]

X = linspace(-2 * math.pi, 2 * math.pi, 100)

Y1 = [math.sin(x) for x in X]
Y2 = [math.cos(x) for x in X]

import matplotlib.pyplot as plt

plt.plot(X, Y1, "r")
plt.plot(X, Y2, "b")

plt.xticks(linspace(-2 * math.pi, 2 * math.pi, 10))
plt.yticks(linspace(-1, 1, 10))
plt.grid(True)

plt.show()