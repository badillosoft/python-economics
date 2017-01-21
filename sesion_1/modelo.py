def linspace(a, b, n):
    d = float(b - a) / (n - 1)
    
    l = []

    for i in range(n):
        l.append(a + i * d)

    return l

def x(t, xo, vxo):
    return xo + vxo * t

def y(t, yo, vyo):
    g = 9.81
    return yo + vyo - g * t ** 2 / 2.0

for t in linspace(0, 2, 20):
    print "%.2f, %.4f, %.4f" %( t, x(t, 0, 5), y(t, 0, 20) )