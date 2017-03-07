import geg

a = [1, 2, 3, 4, 5]

def filtro(x):
    if x > 2:
        return x ** 2

b = geg.data_map(a, filtro)

print a
print b