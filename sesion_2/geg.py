# -*- coding: utf-8 -*-

def suma(valores):
    s = 0
    for x in valores:
        s = s + x
    return s

def suma2(valores):
    s = 0
    for x in valores:
        s = s + x ** 2
    return s

def promedio(valores):
    s = suma(valores)
    n = len(valores)
    return float(s) / n

def varianza(valores):
    p = promedio(valores)
    
    s = 0

    for x in valores:
        s = s + (x - p) ** 2

    n = len(valores)

    return float(s) / (n - 1)

def linspace(a, b, n):
    d = float(b - a) / (n - 1)
    
    l = []

    for i in range(n):
        l.append(a + i * d)

    return l