import openpyxl as xl
import geg

wb = xl.load_workbook("recursos/datos.xlsx", data_only=True)

labels, data = geg.load_data(wb["Hoja 6"]["A1:E10"])
mat = geg.load_mat(wb["Hoja 6"]["A2:E10"])

print "Personas: %d" %len(data)

f1 = geg.data_map(data, lambda p: p["Ingresos"] >= 20000)
f1p = geg.data_map(mat, lambda p: p[3] >= 20000)

print f1
print f1p