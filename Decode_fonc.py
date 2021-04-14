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
    a=1
    ni=1
    for i in range(len(A)):
        a=1
        ni=N[i]
        for j in range(len(N)):
            if j!=i :
                a=a*N[j]
        k= xeuklid(a,ni)
        b=b+k*a*A[i]
    return b%(a*ni)

def erreur1 (A,N): 
    if len(A)!=len(N):
        return 0
    L=[]
    for i in range(len(A)):
        A1=[]
        N1=[]
        for j in range(len(A)):
            if i!=j:
                A1=A1+[A[j]]
                N1=N1+[N[j]]
        l=reste_chinois1(A1,N1)
        L=L+[l]
    return L

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

def decode_fraction_continu(r,ln,nb_error):
    # renvoie la liste des listes de modulo supposé faux
    k=reste_chinois1(r,ln)
    print("k=",k)
    p=1
    n=1
    l_e=[]
    for i in range(len(ln)):
        n=n*ln[i]
    ##print("k/n=",k)
    borne=max_borne_frac(ln,nb_error)
    b=0
    while b<=borne :
        l_am=fraction_reduite_V2(k,n,p)
        (a,b)=list_int_reduite(l_am)
        ##print("k-frac=",abs(k-(a/b)))
        ##print("a=",a , "b=" ,b,"l_b=",l_b)
        l_b=decompose_list(b,ln)
        if(b>borne):
            return l_e
        if l_b!=-1 and l_b!=[]:
            l_e= l_e +[l_b]
        p=p+1
    return l_e

def recontitution_fraction(l_candidat,lr,ln):
    tmp_ln=[]
    tmp_lr=[]
    l_rec=[]
    for i in range(len(l_candidat)):
        for j in range(len(l_candidat[i])):
            for k in range(len(ln)):
                if l_candidat[i][j]!= ln[k]:
                   tmp_ln=tmp_ln+[ln[k]]
                   tmp_lr=tmp_lr+[lr[k]]
        l_rec=l_rec+[reste_chinois1 (tmp_lr,tmp_ln)]
        tmp_lr=[]
        tmp_ln=[]     
    return l_rec






    
