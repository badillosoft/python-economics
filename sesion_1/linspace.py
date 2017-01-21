def linspace(a, b, n):
    d = float(b - a) / (n - 1)
    
    l = []

    for i in range(n):
        l.append(a + i * d)

    return l

print linspace(-1, 1, 5)