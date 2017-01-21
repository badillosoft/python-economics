def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)

def cos(x):
    N = 10
    
    s = 0

    for i in range(0, N):
        s = s + ((-1) ** i) * (x ** (2.0 * i)) / fact(2 * i)

    return s

print cos(0)
print cos(1.57)
print cos(0.78)
print cos(3.141592)