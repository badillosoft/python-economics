import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx")

# (wb["Hoja 1"] -> ws) ["A1:B5"] -> cells
mat = geg.load_mat(wb["Hoja 1"]["A2:B5"])

print mat