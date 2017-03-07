import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Y1 = [1, 4, 9, 16, 25, 36, 49, 64, 81]
Y2 = [0, 10, 20, 30, 40, 50, 60, 70, 80]

plt.plot(X, Y1, "#ff66ff")
plt.plot(X, Y2, "#33ffff")

plt.savefig("graficas/grafica.4.png")