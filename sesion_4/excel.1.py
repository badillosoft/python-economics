import openpyxl as xl

wb = xl.load_workbook("recursos/datos.xlsx")

ws = wb["Hoja 1"]

cells = ws["A1:C5"]

print cells