a = [1, 3, 4, 6, 8, 9, 12, 13, 15, 28, 32, 54, 55]

s = 0

# itera cada elemento de la colección `a`
for x in a:
    # x es el elemento iterado

    # para determinar si x es multiplo de 3
    # basta con saber si el residuo de la division
    # entera es cero (si el módulo de x y 3 es cero)
    r = x % 3

    if r == 0:
        # x es un multiplo de 3 en este bloque
        # porque se ha cumplido la condición x mod 3 = 0
        
        # acumular la x en la variable suma
        s = s + x

# s contiene la suma de los números `x` en `a`
# y que son multiplos de 3
print "La suma es: %d" %(s)