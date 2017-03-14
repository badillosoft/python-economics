import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 6"]["A1:E10"])

def fn(dic):
    if dic["Edad"] <= 35:
        return "A"
    return "B"

geg.data_append(data, "Cat_Edad", fn)

print data

geg.plot_pie(plt, data, "Cat_Edad")

plt.show()