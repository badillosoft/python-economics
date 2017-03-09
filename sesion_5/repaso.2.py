import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 2"]["A2:B16"])

print mat

X, Y = zip(*mat)

print X
print Y

import matplotlib.pyplot as plt

plt.plot(X, Y)

plt.show()