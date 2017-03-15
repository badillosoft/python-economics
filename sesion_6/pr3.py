import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 7"]["A1:D5"])

G1 = geg.data_column(data, "G1")

p = float(sum(G1)) / len(G1)

G1_2 = geg.data_map(G1, lambda x: (x - p) ** 2)

var = sum(G1_2) / (len(G1) - 1)
desv = var ** 0.5

print "Promedio: %.2f Varianza: %.2f Desviacion: %.2f" %(p, var, desv)