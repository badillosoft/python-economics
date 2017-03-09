def load_mat_clasica(cells):
    mat = []
    for xrow in cells:
        row = []
        for cell in xrow:
            row.append(cell.value)
        mat.append(row)
    return mat

def load_mat(cells):
    return [([cell.value for cell in xrow]) for xrow in cells]

def data_map(data, fn):
    aux = []

    for x in data:
        y = fn(x) # Pasa el filtro o transformacion?
        if type(y) == bool: # fn es filtro
            if y:
                aux.append(x)
        elif y != None: # fn es transformacion
            aux.append(y)
    
    return aux

def data_count(data, fn):
    return len(data_map(data, fn))

def data_min(data, labels):
    return data_map(data, lambda l: labels[l.index(min(l))])

def data_max(data, labels):
    return data_map(data, lambda l: labels[l.index(max(l))])