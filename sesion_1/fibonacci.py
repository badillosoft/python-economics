fibo = [1, 1]

n = 2

for i in range(1, n + 1):
    a = fibo[i - 1]
    b = fibo[i]
    c = a + b

    fibo.append(c)

print float(fibo[-1]) / fibo[-2]