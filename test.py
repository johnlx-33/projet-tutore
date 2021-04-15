
from fractions import gcd
import random
from Encode_fonc import *
from Usual_fonc import *
from Decode_fonc import *

### Definition des N
L_modulo_1=[2,3,5,7,11,13]                                              ##30030         #borne  = 210
L_modulo_2=[2,3,5,7,11,13,17]                                           ##510510        #       = 2310
L_modulo_3=[2,3,5,7,11,13,17,19]                                        ##9699690       #       = 30030
L_modulo_4=[2,3,5,7,11,13,17,19,23]                                     ##223092870     #       = 510510
L_modulo_5=[2,3,5,7,11,13,17,19,23,29]                                  ##6469693230    #       = 9699690 
L_modulo_6=[2,3,5,7,11,13,17,19,23,29,31]                               ##20056049010   #       = 223092870
L_modulo_7=[2,3,5,7,11,13,17,19,23,29,31,37]                            ##742073813500  #       = 6469693230
L_modulo_8=[2,3,5,7,11,13,17,19,23,29,31,37,41]
L_modulo_9=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
L_modulo_10=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
L_modulo_11=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
L_modulo_12=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
L_modulo_13=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
L_modulo_14=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
L_modulo_15=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]   
L_modulo_16=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]  
L_modulo_17=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]  
L_modulo_18=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83]
L_modulo_19=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]
L_modulo_20=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
L_modulo_21=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
L_modulo_22=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
L_modulo_23=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107]
L_modulo_24=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
L_modulo_25=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,173,179,181,191,193,197,199,211,223,227,229,233,239]



a=61   ##[1, 1, 1, 5, 6, 9, 10]
b=610  ##[0, 1, 0, 1, 5, 12, 15]
c=547  ##[1, 1, 2, 1, 8, 1, 3]
d=858  ##[0, 0, 3, 4, 0, 0, 8]
e=1453 ##[1, 1, 3, 4, 1, 10, 8]
f=1958 ##[0, 2, 3, 5, 0, 8, 3]
g=2300 ##[0, 1, 0, 1, 3, 4, 1]
h=2500          ##
i=5000          ## [0, 2, 0, 2, 6, 8, 2, 3, 9, 12, 9, 5, 39, 12, 18, 18, 44, 59, 42, 30, 36, 23, 20, 16, 53, 51, 56
                ##, 78, 95, 28, 47, 22, 68, 135, 83, 17, 133, 110, 156, 167, 113, 34, 175, 75, 25, 147, 94, 6, 191, 107, 220]
j=10000         ## [0, 1, 0, 4, 1, 3, 4, 6, 18, 24, 18, 10, 37, 24, 36, 36, 29, 57, 17, 60,
                ##  72, 46, 40, 32, 9, 1, 9, 49, 81, 56, 94, 44, 136, 131, 17, 34, 109, 57, 139, 155, 45, 68, 157, 150, 50, 83, 188, 12, 153, 214, 201]
                
k=15000         ##
l=20000         ## 
m=165165        ##
n=6468468       ## 
o=86842888231   ##


## test avec N=510510
(aa,l_a)=generateur_de_cas(510510,a)
(aa,l_b)=generateur_de_cas(510510,b)
(aa,l_c)=generateur_de_cas(510510,c)
(aa,l_d)=generateur_de_cas(510510,d)
(aa,l_e)=generateur_de_cas(510510,e)
(aa,l_f)=generateur_de_cas(510510,f)
(aa,l_h)=generateur_de_cas(510510,h)


## test avec 51 nb premier
(bb,l_i)= generateur_de_cas_liste(L_modulo_25,i)
(bb,l_j)= generateur_de_cas_liste(L_modulo_25,j)
(bb,l_k)= generateur_de_cas_liste(L_modulo_25,k)
(bb,l_l)= generateur_de_cas_liste(L_modulo_25,l)
(bb,l_m)= generateur_de_cas_liste(L_modulo_25,m)
(bb,l_n)= generateur_de_cas_liste(L_modulo_25,n)
(bb,l_o)= generateur_de_cas_liste(L_modulo_25,o)


## test 1
"""
print(l_a)
print(l_b)
print(l_c)
print(l_d)
print(l_e)
print(l_f)
print(l_h)
print("")
print(l_i)
print(l_j)
print(l_k)
print(l_l)
print(l_m)
print(l_n)
print(l_o)
"""
## liste erroné

##1 erreur

lr_1a=[0, 1, 1, 5, 6, 9, 10] ## pos 0
lr_2a=[1, 2, 1, 5, 6, 9, 10] ## pos 1
lr_3a=[1, 1, 2, 5, 6, 9, 10] ## pos 2
lr_4a=[1, 1, 1, 4, 6, 9, 10] ## pos 3
lr_7a=[1, 1, 1, 5, 2, 9, 10] ## pos 4
## 2 erreur
lr_5a=[1, 1, 1, 5, 1, 9, 16] ## pos 4 et 6 (mod 11 / 17)
lr_6a=[0, 1, 4, 5, 6, 9, 10] ## pos 0 et 2 (mod 2 / 5)

## 1 erreur 
lr_1b=[0, 1, 0, 1, 5, 12, 0] ## pos 6 (mod 17)
lr_2b=[0, 1, 0, 1, 5, 9, 15] ## pos 5 (mod 13)
lr_3b=[0, 1, 0, 4, 5, 12, 15]## pos 3 (mod 7)


## 1 erreur
lr_1c=[0, 1, 2, 1, 8, 1, 3] ## pos 0 mod 2
lr_2c=[1, 2, 2, 1, 8, 1, 3] ## pos 1 mod 3

lr_3c=[1, 1, 4, 1, 8, 1, 3] ## pos 2 mod 5
lr_4c=[1, 1, 2, 6, 8, 1, 3] ## pos 3 mod 7
lr_5c=[1, 1, 2, 1, 3, 1, 3] ## pos 4 mod 11


lr_1d=[0, 0, 3, 4, 0, 0, 8]
lr_1e=[0, 1, 0, 1, 3, 4, 1]
lr_1f=[0, 1, 0, 1, 3, 4, 1]
lr_1h=[0, 1, 0, 1, 3, 4, 2]
lr_2h=[0, 1, 1, 1, 3, 4, 1]

## lr_1i erreur pos 0,1 mod 2 3
lr_1i=[1, 0, 0, 2, 6, 8, 2, 3, 9, 12, 9, 5, 39, 12, 18, 18, 44, 59, 42, 30, 36, 23, 20, 16, 53, 51, 56, 78, 95, 28, 47, 22, 68, 135, 83, 17, 133, 110, 156, 167, 113, 34, 175, 75, 25, 147, 94, 6, 191, 107, 220]
## lr_2i erreur pos  2 5 mod 5 13
lr_2i=[0, 2, 3, 2, 6, 3, 2, 3, 9, 12, 9, 5, 39, 12, 18, 18, 44, 59, 42, 30, 36, 23, 20, 16, 53, 51, 56, 78, 95, 28, 47, 22, 68, 135, 83, 17, 133, 110, 156, 167, 113, 34, 175, 75, 25, 147, 94, 6, 191, 107, 220]
## lr_3i erreur pos  9 12 mod 29 41
lr_3i=[0, 2, 0, 2, 6, 8, 2, 3, 9, 2, 9, 5,12, 12, 18, 18, 44, 59, 42, 30, 36, 23, 20, 16, 53, 51, 56, 78, 95, 28, 47, 22, 68, 135, 83, 17, 133, 110, 156, 167, 113, 34, 175, 75, 25, 147, 94, 6, 191, 107, 220]

## lr_4i erreur pos 2 9 12 mod 5 29 41
lr_4i=[0, 2, 1, 2, 6, 8, 2, 3, 9, 2, 9, 5,12, 12, 18, 18, 44, 59, 42, 30, 36, 23, 20, 16, 53, 51, 56, 78, 95, 28, 47, 22, 68, 135, 83, 17, 133, 110, 156, 167, 113, 34, 175, 75, 25, 147, 94, 6, 191, 107, 220]

## lr_5i erreur pos 2 9 12 15 mod 5 29 41 53
lr_5i=[0, 2, 1, 2, 6, 8, 2, 3, 9, 2, 9, 5,12, 12, 18, 30, 44, 59, 42, 30, 36, 23, 20, 16, 53, 51, 56, 78, 95, 28, 47, 22, 68, 135, 83, 17, 133, 110, 156, 167, 113, 34, 175, 75, 25, 147, 94, 6, 191, 107, 220]


## test avec N=510

"""
print("lr_1a",détection_1_erreur(lr_1a,aa))
print("lr_2a",détection_1_erreur(lr_2a,aa))
print("lr_3a",détection_1_erreur(lr_3a,aa))
print("lr_4a",détection_1_erreur(lr_4a,aa))

print("lr_5a",détection_1_erreur(lr_5a,aa))

print("lr_1h",détection_1_erreur(lr_1h,aa))
print("lr_2h",détection_1_erreur(lr_2h,aa))


print(reste_chinois1 (lr_1d, aa))

print(brute_force_hamming_choix_borne(aa,lr_1h,2,2310))
print(brute_force_hamming_choix_borne(aa,lr_2h,2,2310))
"""
print("test sur 61 <->[1, 1, 1, 5, 6, 9, 10] ")
print("")

print("n-uplet corespondant <-> [0, 1, 1, 5, 6, 9, 10] ")
tmp=decode_fraction_continu(lr_1a,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_1a,aa))
print("")

print("n-uplet corespondant <-> [1, 2, 1, 5, 6, 9, 10] ")
tmp=decode_fraction_continu(lr_2a,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_2a,aa))
print("")

print("n-uplet corespondant <-> [1, 1, 2, 5, 6, 9, 10] ")
tmp=decode_fraction_continu(lr_3a,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_3a,aa))
print("")

print("n-uplet corespondant <-> [1, 1, 1, 4, 6, 9, 10] ")
tmp=decode_fraction_continu(lr_4a,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_4a,aa))
print("")

print("n-uplet corespondant <-> [1, 1, 1, 5, 2, 9, 10] ")
tmp=decode_fraction_continu(lr_7a,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_7a,aa))
print("")



print("test 61 2 erreur")
print("")

print("n-uplet corespondant <->"+str(lr_5a))
tmp=decode_fraction_continu(lr_5a,aa,2)
print(tmp)
print(recontitution_fraction(tmp,lr_5a,aa))
print("")

print("n-uplet corespondant <->"+str(lr_6a))
tmp=decode_fraction_continu(lr_6a,aa,2)
print(tmp)
print(recontitution_fraction(tmp,lr_6a,aa))

print("")

print("test sur 610")
print("")

print("n-uplet corespondant <->"+str(lr_1b))
tmp=decode_fraction_continu(lr_1b,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_1b,aa))
print("")

print("n-uplet corespondant <->"+str(lr_2b))
tmp=decode_fraction_continu(lr_2b,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_2b,aa))
print("")

print("n-uplet corespondant <->"+str(lr_3b))
tmp=decode_fraction_continu(lr_3b,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_3b,aa))
print("")

print("test sur 547")
print("")

print("n-uplet corespondant <->"+str(lr_1c))
tmp=decode_fraction_continu(lr_1c,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_1c,aa))
print("")

print("n-uplet corespondant <->"+str(lr_2c))
tmp=decode_fraction_continu(lr_2c,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_2c,aa))
print("")

print("n-uplet corespondant <->"+str(lr_3c))
tmp=decode_fraction_continu(lr_3c,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_3c,aa))
print("")

print("n-uplet corespondant <->"+str(lr_4c))
tmp=decode_fraction_continu(lr_4c,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_4c,aa))
print("")

print("n-uplet corespondant <->"+str(lr_5c))
tmp=decode_fraction_continu(lr_5c,aa,1)
print(tmp)
print(recontitution_fraction(tmp,lr_5c,aa))
print("")

print("essaie avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_1i))
tmp=decode_fraction_continu(lr_1i,bb,2)
print(tmp)


print("")
print("n-uplet corespondant <->"+str(lr_2i))
tmp=decode_fraction_continu(lr_2i,bb,2)
print(tmp)


print("")
print("n-uplet corespondant <->"+str(lr_3i))
tmp=decode_fraction_continu(lr_3i,bb,2)
print(tmp)


print("")
print("essaie 3 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_4i))
tmp=decode_fraction_continu(lr_4i,bb,5)
print(tmp)



print("")
print("essaie 4 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_5i))
tmp=decode_fraction_continu(lr_5i,bb,5)
print(tmp)


print("")

