import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 6"]["A1:E10"])

geg.plot_pie(plt, data, "Sexo")

plt.show()