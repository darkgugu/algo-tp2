def enfiler(f, valeur):
    f.append(valeur)

def defiler(f):
    if len(f) == 0:
        raise IndexError("La file est vide")
    return f.pop(0)
