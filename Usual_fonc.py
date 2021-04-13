##projet tutoré
##fonction usuel

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


def check_list(ln,lr):
    lr_out=[]
    ln_out=[]
    
    for i in range(len(lr)):
        if ln[i]<=lr[i] :
            print("erreur à l'indice" ,i)
        else :
            lr_out=lr_out+[lr[i]]
            ln_out=ln_out+[ln[i]]


def fraction_reduite(k,n):
    q1=int(k)
    e1=k%1
    if q1==k:
        return [q1]
    l_q=[q1]
    for i in range(1,n):
        l_q=l_q+[int(1/e1)]
        e1=1/e1-int(1/e1)
    return l_q
    
def list_int_reduite(l):
    h_2=0
    h_1=1
    k_1=0
    k_2=1
    hp=0
    kp=0
    for i in range(len(l)):
        hp=l[i]*h_1+h_2
        kp=l[i]*k_1+k_2
        h_2=h_1
        h_1=hp
        k_2=k_1
        k_1=kp
    return(hp,kp)

def list_include(Big_list,sub_list):
    cpt=0
    for i in range(len(sub_list)):
        for j in range(len(Big_list)):
            if sub_list[i]== Big_list[j]:
                 cpt=cpt+1
    if cpt>= len(sub_list):
        return True
    return False

def decompose_list(n,l_d):
    k=n
    l_decompo=[]
    for i in range(len(l_d)):
        if(k%l_d[i]==0):
            l_decompo=l_decompo+[l_d[i]]
            k=k/l_d[i]
    if(k==1):
        return l_decompo
    return -1

def max_borne_frac(ln,t): ## ln = liste des modulo / t= nombre d'erreur
    borne=1
    for i in range(len(ln)-1,len(ln)-t-1,-1):
        borne=borne*ln[i]
    return borne

    

    
