def pile_vide(p) :
    if p == [] :
        return True
    else :
        return False
    
def empiler(p, valeur) :
    p.append(valeur)

def depiler(p) :
 if pile_vide(p) == False :
    p.pop()