import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 4"]["A2:B60"])

Tiempos, Muestras = zip(*mat)

plt.hist(Muestras, bins=4, color="r", normed=True)

plt.show()