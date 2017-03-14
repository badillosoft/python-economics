# personas = [
#     {
#         "Nombre": "Ana",
#         "Edad": 23,
#         "Sexo": "Mujer",
#         "Ingresos": 17000,
#         "Gastos": 12000
#     },
#     {
#         "Nombre": "Beto",
#         "Edad": 32,
#         "Sexo": "Hombre",
#         "Ingresos": 15000,
#         "Gastos": 8000
#     }
# ]

import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 5"]["A1:E13"])

print labels

print data