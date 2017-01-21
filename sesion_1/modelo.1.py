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
    return yo + vyo * t - g * t ** 2 / 2.0

f = open("puntos.csv", "w")

for t in linspace(0, 4.077, 20):
    f.write("%.2f, %.4f, %.4f\n" %( t, x(t, 0, 5), y(t, 0, 20) ))
    print "%.2f, %.4f, %.4f" %( t, x(t, 0, 5), y(t, 0, 20) )

f.close()