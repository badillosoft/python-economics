import geg

a = [1, 2, 3, 4, 5]

def trans(x):
    return x ** 2

b = geg.data_map(a, trans)

print a
print b