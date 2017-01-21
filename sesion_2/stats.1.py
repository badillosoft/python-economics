from openpyxl import load_workbook
from geg import *

wb = load_workbook("series.xlsx", data_only=True)

ws = wb.active

inyectar(ws, "A", 2, ["Hola", "Mundo", 1, 2, 3, "=SUM(A4:A6)"])

wb.save("series.xlsx")