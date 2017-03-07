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
        y = fn(x)
        if y != None:
            aux.append(y)
    
    return aux