import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 1"]["A2:B5"])

X, Y = zip(*mat)

print X
print Y