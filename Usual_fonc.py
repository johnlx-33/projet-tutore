

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
    lerrorpos=[]
    lerrormod=[]
    for i in range(nb_error):
        j=random.randint(0, len(l_reste)-1)
        while j in lerrorpos:
            j=random.randint(0, len(l_reste)-1)
        l_reste[j]= (l_reste[j]+random.randint(0, len(l_modulo)-1))%l_modulo[j]
        lerrorpos=lerrorpos+[j]
        lerrormod=lerrormod+[l_modulo[j]]
    print("modulo erroné"+str(sorted(lerrormod)))
    return(l_modulo,l_reste)


def dist_Hamming(l_reste1,l_reste2):
    n=min(len(l_reste1),len(l_reste2))
    m=max(len(l_reste1),len(l_reste2))
    cpt=m-n
    for i in range(n):
        if l_reste1[i] != l_reste2[i]:
            cpt=cpt+1
    return cpt


def calcule_borne(l,nb_error): 
    c=1
    for i in range(len(l)-2*nb_error):
       c=c*l[i]
    return c

def check_list(ln,lr):
    lr_out=[]
    ln_out=[]
    for i in range(len(lr)):
        if ln[i]<=lr[i] :
            print("erreur à l'indice" ,i)
        else :
            lr_out=lr_out+[lr[i]]
            ln_out=ln_out+[ln[i]]
            
def liste_nb_premier(n):
    l=[]
    for i in range(2,n):
        if is_prime(i) :
            l=l+[i]
    return l

def is_prime(i):
    j=2
    while j*j<=i:
        if i%j==0:
           return False
        j=j+1
    return True

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

def fraction_reduite_V2(k,n,p):
    a=k
    b=n
    q=1
    r=1
    l=[]
    n=0
    while n<p:
        q=a//b
        r=a%b
        l=l+[q]
        a=b
        b=r
        n=n+1
        if r==0 :
            print("ordre max reduite =" + str(n) )
            return l
    return l     
  
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


def l_candi_to_pos(l_candidat,ln):
    l_candi_pos=[]
    for i in range(len(l_candidat)):
        tmp=[]
        for j in range(len(l_candidat[i])):
            for k in range(len(ln)):
                if l_candidat[i][j]==ln[k]:
                    tmp=tmp+[k]
        l_candi_pos=l_candi_pos+[tmp]  

    return l_candi_pos


def clear_error(ln,lr,pos):
    ln_out=ln
    lr_out=lr
    for i in range(len(pos)):
        del ln_out[pos[i]]
        del lr_out[pos[i]]
    return (ln_out,lr_out)













