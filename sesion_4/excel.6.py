import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 2"]["A2:D16"])

X, Y1, Y2, Y3 = zip(*mat)

print X
print Y1
print Y2
print Y3

##################################
# Grafica                        #
##################################

import matplotlib.pyplot as plt

plt.plot(X, Y1, "r")
plt.plot(X, Y2, "b")
plt.plot(X, Y3, "y")

plt.show()