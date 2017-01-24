from openpyxl import load_workbook
from geg import load_data

wb = load_workbook("data.xlsx")

ws = wb.active

labels = ["nombre", "edad", "sexo", "color", "salario"]

datos = load_data(ws, "A3", "E10", labels)

h = 0
m = 0

for p in datos:
    if p["sexo"] == "H":
        h = h + 1
    if p["sexo"] == "M":
        m = m + 1

t = h + m

print "Hombres: %d" %h
print "Mujeres: %d" %m
print "Total: %d" %t
print "%% Hombres: %.2f" %(100.0 * h / t)
print "%% Mujeres: %.2f" %(100.0 * m / t)