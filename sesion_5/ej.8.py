import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 5"]["B2:E13"])

labels = [1, 2, 3, 4]
Ganadores = geg.data_max(mat, labels)

plt.hist(Ganadores, bins=4)

plt.show()