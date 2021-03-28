##projet tutoré
##fonction encodage

from fractions import gcd
import random

from Usual_fonc import *



def generateur_de_cas(n,k):
    ## n>k renvoie 2 liste
    ## liste des facteurs de n
    ## liste de k mod facteur de n
    ln = liste_nb_fact_premier(n)
    lk = []
    for i in range(len(ln)):
        lk = lk + [k%ln[i]]
    
    return (ln,lk)


def generateur_de_cas_liste(l_modulo,k):
    l_reste =[]
    for i in range(len(l_modulo)):
        l_reste = l_reste + [k%l_modulo[i]]
    return (l_modulo,l_reste)
