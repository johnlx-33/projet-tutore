##projet Tutoré

##from fractions import gcd
##import random

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

def generateur_de_cas_liste(l_modulo,k):
    l_reste =[]
    for i in range(len(l_modulo)):
        l_reste = l_reste + [k%l_modulo[i]]
    return (l_modulo,l_reste)

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
        
def dist_Hamming(l_reste1,l_reste2):
    n=min(len(l_reste1),len(l_reste2))
    m=max(len(l_reste1),len(l_reste2))
    cpt=n
    for i in range(n):
        if (l_reste1[i]) == (l_reste2[i]):
            cpt=cpt-1
    return cpt

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
    (a,L_force)=generateur_de_cas(N,cpt)
    l_candidat=[]
    while cpt<=borne :
        if( (dist_Hamming(L_force,l_reste))<=nb_erreur):
            l_candidat=l_candidat+[cpt]
        cpt=cpt+1
        (a,L_force)=generateur_de_cas(N,cpt)

    return l_candidat


def calcule_borne(l):
    b=0
    c=1
    for i in range(len(l)):
       b=b+l[i]-1
       c=c*l[i]
    return c//b

def loop():
    cpt=0
    l=[]
    k=0
    for i in range(271):
        (a,l)=generateur_de_cas(30030,cpt)
        if(dist_Hamming(l,[0, 1, 1, 5, 6, 9])<=2):
            print(cpt,l)
        cpt=cpt+1
def liste_borne(borne):
    cpt=0
    (a,l)=generateur_de_cas(510510,cpt)
    for i in range(borne):
        print(cpt,l)
        cpt=cpt+1
        (a,l)=generateur_de_cas(510510,cpt)





        
liste_borne(858)
loop()
(a,b)=([2, 3, 5, 7, 11, 13] ,[1, 1, 1, 5, 6, 9])##a=30030 ,b=61
(a,c)=([2, 3, 5, 7, 11, 13], [0, 1, 1, 5, 6, 9])
(a,d)=([2, 3, 5, 7, 11, 13], [1, 1, 1, 7, 6, 9])
(a,e)=([2, 3, 5, 7, 11, 13], [1, 2, 1, 7, 6, 9])
(a,f)=([2, 3, 5, 7, 11, 13], [0, 0, 1, 5, 6, 9])
print(dist_Hamming(c,b))
(N1,T1)=generateur_de_cas(30030,858)
T2=[0, 0, 3, 4, 0, 1]
T3=[0, 0, 3, 4, 1, 1]

"""
print(brute_force_hamming_choix_borne(a,b,0,210))
print(brute_force_hamming_choix_borne(a,c,1,210))
print(brute_force_hamming_choix_borne(a,d,2,210))
print(brute_force_hamming_choix_borne(a,e,2,210))
print(brute_force_hamming_choix_borne(a,f,2,210))
print(reste_chinois1(f,a))
print(N1,T1)
print(brute_force_hamming(a,T2,1))
print(brute_force_hamming(a,T3,2))
print(reste_chinois1(T3,a))  ##T3=4148

print(calcule_borne([2,3,5,7,11,13]))
print(calcule_borne([2,3,5,7,11,13,17]))
print(calcule_borne([2,3,5,7,11,13,17,19]))
print(calcule_borne([2,3,5,7,11,13,17,19,23]))
print(calcule_borne([2,3,5,7,11,13,17,19,23,29]))
print(calcule_borne([2,3,5,7,11,13,17,19,23,29,31]))
print(calcule_borne([2,3,5,7,11,13,17,19,23,29,31,37]))

N1=[2,3,5,7,11,13]
N2=[2,3,5,7,11,13,17]
N3=[2,3,5,7,11,13,17,19]
N4=[2,3,5,7,11,13,17,19,23]
N5=[2,3,5,7,11,13,17,19,23,29]
N6=[2,3,5,7,11,13,17,19,23,29,31]
N7=[2,3,5,7,11,13,17,19,23,29,31,37]


(a,T1)=generateur_de_cas_liste(N4,61)
(a,T2)=generateur_de_cas_liste(N4,610)
(a,T3)=generateur_de_cas_liste(N4,2451570)
(a,T4)=generateur_de_cas_liste(N4,3451570)
(a,T5)=generateur_de_cas_liste(N5,61)
(a,T6)=generateur_de_cas_liste(N5,610)
(a,T7)=generateur_de_cas_liste(N5,54367170)
(a,T8)=generateur_de_cas_liste(N5,64367170)
(a,T9)=generateur_de_cas_liste(N6,61)
(a,T10)=generateur_de_cas_liste(N6,610)
(a,T11)=generateur_de_cas_liste(N6,1346043557)
(a,T12)=generateur_de_cas_liste(N6,1346044557)
(a,T13)=generateur_de_cas_liste(N7,61)
(a,T14)=generateur_de_cas_liste(N7,610)
(a,T15)=generateur_de_cas_liste(N7,401120980267)
(a,T16)=generateur_de_cas_liste(N7,401220980267)
print("T1=",T1)
print("T2=",T2)
print("T3=",T3)
print("T4=",T4)
print("T5=",T5)
print("T6=",T6)
print("T7=",T7)
print("T8=",T8)
print("T9=",T9)
print("T10=",T10)
print("T11=",T11)
print("T12=",T12)
print("T13=",T13)
print("T14=",T14)
print("T15=",T15)
print("T16=",T16)
T1e1=[1, 1, 1, 5, 6, 9, 10, 4, 16]
T2e1=[0, 1, 0, 1, 5, 12, 15, 2, 13]
T3e1=[0, 0, 0, 2, 0, 4, 0, 0, 1]
T4e1=[0, 1, 0, 3, 1, 5, 9, 11, 7]
T5e1=[1, 1, 1, 5, 6, 9, 10, 4, 15, 4]
T6e1=[0, 1, 0, 1, 5, 12, 15, 2, 12, 2]
T7e1=[0, 0, 0, 4, 0, 0, 14, 0, 0, 1]
T8e1=[0, 1, 0, 0, 10, 10, 2, 15, 14, 18]
T9e1=[1, 1, 1, 5, 6, 9, 10, 4, 15, 3, 31]
T10e1=[0, 1, 0, 1, 5, 12, 15, 2, 12, 1, 22]
T11e1=[1, 2, 2, 5, 1, 1, 13, 14, 21, 2, 29]
T12e1=[1, 0, 2, 4, 0, 0, 10, 7, 9, 16, 6]
T13e1=[1, 1, 1, 5, 6, 9, 10, 4, 15, 3, 30, 25]
T14e1=[0, 1, 0, 1, 5, 12, 15, 2, 12, 1, 21, 19]
T15e1=[1, 1, 2, 0, 7, 7, 7, 7, 7, 7, 7, 30]
T16e1=[1, 2, 2, 2, 8, 3, 6, 5, 9, 3, 21, 19]


print("T1e1",brute_force_hamming(N4,T1e1,1))
print("T2e1",brute_force_hamming(N4,T2e1,1))
print("T3e1",brute_force_hamming(N4,T3e1,1))
print("T4e1",brute_force_hamming(N4,T4e1,1))
print("T5e1",brute_force_hamming(N5,T5e1,1))
print("T6e1",brute_force_hamming(N5,T6e1,1))
print("T7e1",brute_force_hamming(N5,T7e1,1))
print("T8e1",brute_force_hamming(N5,T8e1,1))
print("T9e1",brute_force_hamming(N6,T9e1,1))
print("T10e1",brute_force_hamming(N6,T10e1,1))
print("T11e1",brute_force_hamming(N6,T11e1,1))
print("T12e1",brute_force_hamming(N6,T12e1,1))
print("T13e1",brute_force_hamming(N7,T13e1,1))
print("T14e1",brute_force_hamming(N7,T14e1,1))
print("T15e1",brute_force_hamming(N7,T15e1,1))
print("T16e1",brute_force_hamming(N7,T16e1,1))
"""

