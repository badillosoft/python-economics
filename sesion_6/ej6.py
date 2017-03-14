import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 6"]["A1:E10"])

geg.data_cat(data, "Cat_Edad", {
    "0-20": lambda dic: dic["Edad"] <= 20,
    "21-40": lambda dic: dic["Edad"] > 20 and dic["Edad"] <= 40,
    "40-60": lambda dic: dic["Edad"] > 40 and dic["Edad"] <= 60,
    "60+": lambda dic: dic["Edad"] > 60,
})

geg.data_cat(data, "Cat_Ingresos", {
    "Pobre": lambda dic: dic["Ingresos"] <= 6000,
    "Medio": lambda dic: dic["Ingresos"] > 6000 and dic["Ingresos"] <= 12000,
    "Alto": lambda dic: dic["Ingresos"] > 12000
})

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)

geg.plot_pie(ax1, data, "Cat_Edad")
geg.plot_pie(ax2, data, "Cat_Ingresos")
geg.plot_pie(ax3, data, "Sexo")

plt.show()