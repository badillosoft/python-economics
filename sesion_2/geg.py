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