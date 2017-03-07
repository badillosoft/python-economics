import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 3"]["A2:B10"])

Nombres, Sexos = zip(*mat)

print Nombres
print Sexos

