import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 4"]["A2:B60"])

Tiempos, Muestras = zip(*mat)

# TODO: Contar c1, c2, c3, c4 de muestras
c1 = geg.data_count(Muestras, lambda x: x == 1 or x == 2)
c2 = geg.data_count(Muestras, lambda x: x == 3 or x == 4)

plt.pie([c1, c2],
    labels=["Cines", "Tiendas de Ropa"],
    colors=["c", "m"],
    autopct="%d %%")

plt.axis('equal')

plt.show()