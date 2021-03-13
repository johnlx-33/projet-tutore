##projet Tutoré

from fractions import gcd
import random

def xeuklid(a,b):
    # calcul de l'inverse modulo b du nombre a
    xs0, xs1, ys0, ys1, s, d = 1, 0, 0, 1, 1, b
    while b!=0:
        q, r = divmod(a,b)      
        a, b = b, r
        x, y = xs1, ys1
        xs1, ys1 = q*xs1 + xs0, q*ys1 + ys0
        xs0, ys0 = x, y
        s = -s
    return s*xs0 + ((1-s)//2)*d

def entree_entiers(a,vrai):
    try:
        entree=int(a)
        if entree >0:
            vrai=1
    except ValueError:
        vrai=0
    return entree,vrai

def algo_reste_chinois(reste,module):
    
    return

def liste_nb_fact_premier(n):
    ##int(n) renvoie la liste des facteurs premier composant n
    l=[]
    i=2
    while(n!=1):
        c=1
        while(n%i==0):
            n=n//i
            c=c*i
        if ((n*c)%i==0):
            l=l+[c]
        i=i+1
    return l

def generateur_de_cas(n,k):
    ## n>k renvoie 2 liste
    ## liste des facteurs de n
    ## liste de k mod facteur de n
    ln = liste_nb_fact_premier(n)
    lk = []
    for i in range(len(ln)):
        lk = lk + [k%ln[i]]
    
    return (ln,lk)

def create_error(nb_error,ln,lk):
    ## renvoie lk avec au plus nb_error
    for i in range(nb_error):
        j=random.randint(0, len(lk)-1)
        lk[j]= (lk[j]+random.randint(0, len(ln)-1))%ln[j]
    return(ln,lk)





