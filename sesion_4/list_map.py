def linspace(a, b, n):
    d = float(b - a) / (n - 1)
    return [a + i * d for i in range(0, n)]

def linspace_clasico(a, b, n):
    d = float(b - a) / (n - 1)
    
    aux = []

    for i in range(0, n):
        aux.append(a + i * d)

    return aux

x = linspace(-1, 1, 5)

print x