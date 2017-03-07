import openpyxl as xl

wb = xl.load_workbook("recursos/datos.xlsx")

ws = wb["Hoja 1"]

cells = ws["A1:B5"]

import geg

mat = geg.load_mat(cells)

print mat