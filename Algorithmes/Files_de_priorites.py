def maximum(t):
    return t[0] # toujours le premier élément

def extraire_max(t):
    max_element = t[0]
    t[0] = t[-1]

    t.pop()
    tas_maxifier(t, 0)
    return max_element

def augmenter_cle(t, i, cle):
    t[i] = cle

    while i > 0 and t[(i-1)//2] < t[i]:
        parent = (i-1)//2
        t[i], t[parent] = t[parent], t[i]
        i = parent

def insérer(t, cle):
    t.append(float('-inf'))
    augmenter_cle(t, len(t) - 1, cle)

def tas_maxifier(t, i):
    gauche = 2 * i + 1
    droite = 2 * i + 2
    plus_grand = i

    if gauche < len(t) and t[gauche] > t[plus_grand]:
        plus_grand = gauche
    if droite < len(t) and t[droite] > t[plus_grand]:
        plus_grand = droite

    if plus_grand != i:
        t[i], t[plus_grand] = t[plus_grand], t[i]
        tas_maxifier(t, plus_grand)