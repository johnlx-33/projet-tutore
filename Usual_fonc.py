##projet tutoré
##fonction usuel

from fractions import gcd
import random
from Encode_fonc import *
from Decode_fonc import *

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



def create_error(nb_error,l_modulo,l_reste):
    ## renvoie lk avec au plus nb_error
    for i in range(nb_error):
        j=random.randint(0, len(l_reste)-1)
        l_reste[j]= (l_reste[j]+random.randint(0, len(l_modulo)-1))%l_modulo[j]
    return(l_modulo,l_reste)


def dist_Hamming(l_reste1,l_reste2):
    n=min(len(l_reste1),len(l_reste2))
    m=max(len(l_reste1),len(l_reste2))
    cpt=m-n
    for i in range(n):
        if l_reste1[i] != l_reste2[i]:
            cpt=cpt+1
    return cpt


def calcule_borne(l):
    b=0
    c=1
    for i in range(len(l)):
       b=b+l[i]-1
       c=c*l[i]
    return c//b
