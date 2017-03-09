import matplotlib.pyplot as plt

plt.pie([10, 4, 3], labels=["A", "B", "C"],
    autopct="%d %%", startangle=180, explode=[0, 0.2, 0.1])

plt.show()