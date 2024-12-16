class Chainon :
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant

def inserer(l, cle) :
    return Chainon(cle, l)

def rechercher_liste(l, cle) :
    current = l
    while current is not None:
        if current.valeur == cle :
            return current
        current = current.suivant
    return None

def supprimer_liste(l, cle) :
    if l == None :
        return None
    if l.valeur == cle :
        return l.suivant
    else :
        return Chainon(l.valeur, supprimer_liste(l.suivant, cle))
