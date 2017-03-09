import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 4"]["A2:B60"])

Tiempos, Muestras = zip(*mat)

# TODO: Contar c1, c2, c3, c4 de muestras
c1 = geg.data_count(Muestras, lambda x: x == 1)
c2 = geg.data_count(Muestras, lambda x: x == 2)
c3 = geg.data_count(Muestras, lambda x: x == 3)
c4 = geg.data_count(Muestras, lambda x: x == 4)

plt.pie([c1, c2, c3, c4],
    labels=["Cinemex", "Cinepolis", "CA", "Zara"],
    colors=["r", "b", "w", "g"],
    autopct="%d %%")

plt.axis('equal')

plt.show()