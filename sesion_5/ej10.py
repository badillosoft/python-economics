import geg

mat = [
    [1, 2],
    [3, 2],
    [5, 4],
    [6, 7],
    [0, 20],
    [50, -10]
]

# 1. Definir las etiquetas de cada columna
labels = ["A", "B"]

# 2. Obtener las etiquetas de los maximos
maximos = geg.data_max(mat, labels)

print maximos