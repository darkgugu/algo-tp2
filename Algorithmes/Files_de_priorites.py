def maximum_tas(t):
    # Retourne l'élément du tas ayant la clé maximale.
    # Le maximum est toujours à l'indice 0 dans un tas max.
   
    if len(t) == 0:
        raise IndexError("Le tas est vide.")
    return t[0]

def extraire_max_tas(t):
    # Supprime et retourne l'élément du tas ayant la clé maximale.
    
    if len(t) == 0:
        raise IndexError("Le tas est vide.")
    
    # Échanger le premier et le dernier élément
    max_element = t[0]
    t[0] = t[-1]
    t.pop()  # Supprimer l'ancien maximum (dernier élément)
    tas_maxifier(t, 0)  # Rééquilibrer le tas
    return max_element

def augmenter_clé_tas(t, i, cle):
    # Accroît la valeur de l'élément d'indice i à la nouvelle valeur 'cle'.
    # La nouvelle clé doit être plus grande que l'ancienne.

    if i < 0 or i >= len(t):
        raise IndexError("Indice hors des limites.")
    if cle < t[i]:
        raise ValueError("La nouvelle clé est plus petite que la clé actuelle.")
    
    t[i] = cle
    # Remonter l'élément pour maintenir la propriété du tas
    while i > 0 and t[(i - 1) // 2] < t[i]:
        parent = (i - 1) // 2
        t[i], t[parent] = t[parent], t[i]
        i = parent

def insérer_tas_max(t, cle):
    # Insère un nouvel élément dans le tas.

    t.append(float('-inf'))  # Ajouter une valeur très petite pour permettre l'augmentation
    augmenter_clé_tas(t, len(t) - 1, cle)

def tas_maxifier(t, i):
    # Maintient la propriété du tas max en partant de l'indice i.
    # Assure que l'élément à l'indice i est plus grand que
    # ses enfants et rééquilibre si nécessaire.
    
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