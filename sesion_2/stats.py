from openpyxl import load_workbook
from geg import *

wb = load_workbook("series.xlsx", data_only=True)

ws = wb.active # wb["Hoja 1"]

a = bloque(ws, "C", 6, 14)
b = bloque(ws, "F", 4, 18)

print a
print b

print suma(a)
print suma2(a)
print promedio(a)
print varianza(a)

print suma(b)
print suma2(b)
print promedio(b)
print varianza(b)