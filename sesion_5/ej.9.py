import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 5"]["B2:E13"])

labels = ["Cinemex", "Cinepolis", "Lumier", "Cineteca"]
Ganadores = geg.data_max(mat, labels)

cinemex = geg.data_count(Ganadores, lambda g: g == "Cinemex")
cinepolis = geg.data_count(Ganadores, lambda g: g == "Cinepolis")
lumier = geg.data_count(Ganadores, lambda g: g == "Lumier")
cineteca = geg.data_count(Ganadores, lambda g: g == "Cineteca")

plt.pie([cinemex, cinepolis, lumier, cineteca], labels=labels)

plt.show()