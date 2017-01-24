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

def bloque(ws, col, a, b):
    l = []

    for i in range(a, b + 1):
        c = ws["%s%d" %(col, i)]
        l.append(c.value if c.value != None else 0)

    return l

def inyectar(ws, col, row, values):
    n = len(values)
    for i in range(row, row + n):
        ws["%s%d" %(col, i)] = values[i - row]

def import_excel(ws, ini_cell, fin_cell):
    key_range = "%s:%s" %(ini_cell, fin_cell)
    
    cells = ws[key_range]

    datos = []

    for row in cells:
        p = {
            "Nombre": row[0].value,
            "Edad": row[1].value,
            "Sexo": row[2].value,
            "Categoria": row[3].value,
            "Salario": row[4].value
        }

        datos.append(p)

    return datos