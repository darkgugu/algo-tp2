def gauche(i):
    return 2*i+1

def droite(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def tamiser(array, node, n) :
    n = n - 1
    k = node
    j = 2*k + 1
    while j < n :
        if j < n and array[j] < array[j + 1] :
            j = j + 1
        if array[k] < array[j] :
            array[k], array[j] = array[j], array[k]
            k = j
            j = 2*k + 1
        else :
            break

def triParTas(array) :
    for i in range(len(array)//2)[::-1] :
        tamiser(array, i, len(array))
    for i in range(len(array), 1, -1) :
        array[i - 1], array[0] = array[0], array[i - 1]
        tamiser(array, 0, i-1)

def construire_tas_max(array) : 
    for i in range(len(array)//2)[::-1] :
        tamiser(array, i, len(array))
    return array