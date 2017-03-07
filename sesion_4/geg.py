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