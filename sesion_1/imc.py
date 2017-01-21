# Declaramos la función
def IMC(p, e):
	# lo que devuelve la función
	return float(p) / e ** 2

# Declaramos dos variables locales
peso = 80
estatura = 1.54

# LLamada a la función e impresión directa
# pasamos los parámetros p y e por lo que valgan
# las variables peso y estatura
print IMC(peso, estatura)

# Pasamos los parámetros p y e directectamente con
# un valor
print IMC(60, 1.7)