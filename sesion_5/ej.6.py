import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 5"]["B2:E13"])

#Cinemex, Cinepolis, Lumier, Cineteca = zip(*mat)

def seleccionar_cine(row):
    i = row.index(max(row))

    cines = ["Cinemex", "Cinepolis", "Lumier", "Cineteca"]

    return cines[i]

Ganadores = geg.data_map(mat, seleccionar_cine)

cines = ["Cinemex", "Cinepolis", "Lumier", "Cineteca"]
Ganadores = geg.data_map(mat, lambda row: cines[row.index(max(row))])

print Ganadores