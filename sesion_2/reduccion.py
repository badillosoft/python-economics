def regla(actual, nuevo):
    print "actual %d" %actual
    print "nuevo %d" %nuevo
    print "-" * 10
    return actual + nuevo

print reduce(regla, [1, 2, 3, 4, 5, 6])

def regla2(actual, nuevo):
    if nuevo % 2 == 0:
        actual.append(nuevo)

    return actual

print reduce(regla2, [[], 23, 11, 2, 46, 13, 54])