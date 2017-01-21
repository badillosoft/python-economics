a = [(1, 2), (3, 4), (9, 8)]

def regla(p):
    print p
    x, y = p
    return x + y

b = map(regla, a)

print b