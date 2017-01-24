from openpyxl import load_workbook
from geg import *

wb = load_workbook("data.xlsx")

ws = wb.active

print get_labels(ws, "C13")