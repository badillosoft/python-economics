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

def load_data(cells):
    mat = load_mat(cells)

    labels = mat[0]

    data = []

    for i in range(1, len(mat)):
        row = mat[i]

        dic = {}
        for k, v in zip(labels, row):
            dic[k] = v

        data.append(dic)

    return labels, data

def plot_pie(ax, data, label):
    cats = {}

    for dic in data:
        k = dic[label]
        if cats.has_key(k):
            cats[k] += 1
        else:
            cats[k] = 1

    labels, sizes = zip(*[(k, cats[k]) for k in cats])

    ax.pie(sizes, labels=labels)

