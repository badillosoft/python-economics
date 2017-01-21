def IMC(p, e):
	return float(p) / e ** 2

imc = IMC(16, 1.7)

if imc < 18.5:
    print "Bajo de peso"
elif imc < 25:
    print "Peso normal"
else:
    print "Sobrepeso"