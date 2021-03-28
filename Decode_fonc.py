##projet tutoré
##fonction de decodage

from fractions import gcd
import random
from Encode_fonc import *
from Usual_fonc import *



def reste_chinois1 (A, N): ##algo de reconstitution
    if len(A)!=len(N):
        return 0
    b=0
    c=1
    AI=[]
    NI=[]
    for i in range(len(N)): ## on enlève les 0
        if A[i]==0:
            c=c*N[i]
        else:
            AI=AI+[A[i]]
            NI=NI+[N[i]]
    for i in range(len(AI)):
        a=1
        ni=NI[i]
        for j in range(len(NI)):
            if j!=i :
                a=a*NI[j]
        k= xeuklid(a,ni)
        b=b+k*a*AI[i]
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
