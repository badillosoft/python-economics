import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx")

mat = geg.load_mat(wb["Hoja 3"]["A2:B10"])

Nombres, Sexos = zip(*mat)

print Nombres
print Sexos

Hombres = geg.data_count(Sexos, lambda sexo: sexo == "Hombre")

Mujeres = geg.data_count(Sexos, lambda sexo: sexo == "Mujer")

print Hombres
print Mujeres

plt.pie([Hombres, Mujeres],
    labels=["Hombres", "Mujeres"],
    colors=["#f0f730", "g"])

plt.show()