import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 7"]["A1:D5"])

geg.data_append(data, "Suma",
    lambda r: r["G1"] + r["G2"] + r["G3"])

geg.save_data(data, ["Planta", "G3", "G2", "G1", "Suma"],
    "resultado.xlsx", "Hoja 7", "A7")