##projet tutoré
##fonction de decodage

from fractions import gcd
import random
from Encode_fonc import *
from Usual_fonc import *



def reste_chinois1 (A, N): ##algo de reconstitution
    if len(A)!=len(N):
        return -1
    b=0
    c=1
    for i in range(len(A)):
        a=1
        ni=N[i]
        for j in range(len(N)):
            if j!=i :
                a=a*N[j]
        k= xeuklid(a,ni)
        b=b+k*a*A[i]
    return b%(a*ni)

def détection_1_erreur(l_reste,l_modulo):
    if len(l_reste)!=len(l_modulo):
        return -1
    L1=[]
    for i in range(len(l_reste)):
        L=[]
        for j in range(len(l_reste)):
            l_restei=[] ## l_reste sans le i-ème élément
            l_moduloi=[] ##l_modulo sans ke i-ème élément
            for k in range(len(l_reste)):
                if k!=i and k!=j:
                    l_restei=l_restei+[l_reste[k]]
                    l_moduloi=l_moduloi+[l_modulo[k]]
            l=reste_chinois1(l_restei,l_moduloi)
            L=L+[l]
        L1=L1+[L]
    return L1

## teste tout les cas de 0 a la borne 
def brute_force_hamming(l_modulo,l_reste,nb_erreur):
    n=len(l_reste)
    cpt=0
    N=1
    borne=0
    for i in range(n):
        N=N*l_modulo[i]
        borne=borne + (l_modulo[i]-1)
    borne=N//borne
    (a,L_force)=generateur_de_cas(N,cpt)
    l_candidat=[]
    while cpt<=borne :
        if( dist_Hamming(L_force,l_reste)<=nb_erreur):
            l_candidat=l_candidat+[cpt]
        cpt=cpt+1
        (a,L_force)=generateur_de_cas(N,cpt)

    return l_candidat


def brute_force_hamming_choix_borne(l_modulo,l_reste,nb_erreur,borne):
    n=len(l_reste)
    cpt=0
    N=1
    for i in range(n):
        N=N*l_modulo[i]
    (a,L_force)=generateur_de_cas(N,cpt)
    l_candidat=[]
    while cpt<=borne :
        if (dist_Hamming(L_force,l_reste))<=nb_erreur:
            l_candidat=l_candidat+[cpt]    
        cpt=cpt+1
        (a,L_force)=generateur_de_cas(N,cpt)
        

    return l_candidat

def decode_fraction_continu(r,ln) :
    k=reste_chinois1(r,ln)
    p=1
    n=1
    boul=0
    l_e=[]
    for i in range(len(ln)):
        n=n*ln[i]
    k=k/n
    while p<20 :
        l_am=fraction_reduite(k,p)
        print(k,p)
        (a,b)=list_int_reduite(l_am)
        l_b=liste_nb_fact_premier(b)
        print("a=",a , "b=" ,b,"l_b=",l_b)
        if(a==1):
            for i in range(len(l_b)):
                for j in range(len(ln)):
                    if(l_b[i]==ln[j]):
                        boul=boul+1
                        l_e=l_e+[l_b[i]]
        p=p+1
      
    return l_e



    
