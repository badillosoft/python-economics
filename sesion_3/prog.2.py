from openpyxl import load_workbook
from geg import load_data

wb = load_workbook("data.xlsx")

ws = wb.active

datos = load_data(ws, "A3", "E10",
    ["Nombre", "Edad", "Sexo", "Categoria", "Salario"])

datos2 = []

for persona in datos:
    if persona["Edad"] >= 70:
        datos2.append(persona)

print datos2