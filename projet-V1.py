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
    cpt=m-n
    for i in range(n):
        if l_reste1[i] != l_reste2[i]:
            cpt=cpt+1
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
    L_force=generateur_de_cas(N,cpt)
    while cpt<=borne :
        if( dist_Hamming(L_force,l_reste)==nb_erreur):
            return (l_modulo,L_force,cpt)
        cpt=cpt+1
        L_force=generateur_de_cas(N,cpt)

    return -1





(a,b)=([2, 3, 5, 7, 11, 13] ,[1, 1, 1, 5, 6, 9])
(c,d)=([2, 3, 5, 7, 11, 13], [0, 1, 1, 5, 6, 9])
(e,f)=([2, 3, 5, 7, 11, 13], [1, 1, 1, 7, 6, 9])
