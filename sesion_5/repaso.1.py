import geg

a = [1, 2, 3, 4, 5, 6, 7]

b = geg.data_map(a, lambda x: 2 * x + 1)

print a
print b