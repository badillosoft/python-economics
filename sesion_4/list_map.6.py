import geg

a = ["Hombre", "Mujer", "Hombre", "Mujer", "Hombre"]

b = geg.data_map(a, lambda x: x if x == "Mujer" else None)

print a
print b