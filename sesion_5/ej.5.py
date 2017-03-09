import openpyxl as xl
import matplotlib.pyplot as plt
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

mat = geg.load_mat(wb["Hoja 5"]["B2:E13"])

#Cinemex, Cinepolis, Lumier, Cineteca = zip(*mat)

def seleccionar_cine(row):
    mayor = row[0]
    indice_mayor = 0

    for i in range(0, len(row)):
        if row[i] > mayor:
            mayor = row[i]
            indice_mayor = i

    cines = ["Cinemex", "Cinepolis", "Lumier", "Cineteca"]

    return cines[indice_mayor]

Ganadores = geg.data_map(mat, seleccionar_cine)

print Ganadores