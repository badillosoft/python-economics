import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Y1 = [1, 4, 9, 16, 25, 36, 49, 64, 81]
Y2 = [0, 10, 20, 30, 40, 50, 60, 70, 80]

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0][0].plot(X, Y1)
axs[1][1].plot(X, Y2)
axs[0][1].plot(Y1, Y2)
axs[1][0].plot(Y2, Y1)

plt.show()