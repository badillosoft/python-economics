from openpyxl import load_workbook
from geg import *

wb = load_workbook("puntos.xlsx")

ws = wb.active

puntos = automatic_load_data(ws, "A2")

def f(x, y):
    return x**2 + y**2

for p in puntos:
    x = p["X"]
    y = p["Y"]
    z = f(x, y)
    print "%f, %f, %f" %(x, y, z)