# Auteurs : Hugo Thouraud de Lavignére et Cheikh Tidiane Fall | My First Chat Bot 
# Ce fichier contient les fonctions constituant le calcul de similaritée
from math import sqrt
def scalar_product(a, b):
    ''' Calcul du produit scalaire '''
    assert type(a) is list and type(b) is list, "a et b ne respectent pas les conditions"
    if len(a) != len(b):
        return None
    else:
        produit_scalaire = 0
        for i, j in zip(a, b): # On combine les deux liste en distinguant leurs valeurs pour pouvoir les additionées
            produit_scalaire += i * j
        return produit_scalaire

def norm(a):
    ''' Calcul de la norme du vecteur'''
    assert type(a) is list , "a ne respecte pas les conditions"
    somme = 0
    for e in a:
        somme+= e**2
    return sqrt(somme)


def similarity(a,b):
    ''' Calcul de la similaritée avec la (cosine similarity)'''
    scal =  scalar_product(a,b)
    nor = norm(a) * norm(b)
    return scal/nor