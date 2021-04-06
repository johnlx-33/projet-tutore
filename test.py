
from fractions import gcd
import random
from Encode_fonc import *
from Usual_fonc import *
from Decode_fonc import *

### Definition des N
L_modulo_1=[2,3,5,7,11,13]                      ##30030         #borne  = 858
L_modulo_2=[2,3,5,7,11,13,17]                   ##510510        #       = 10010
L_modulo_3=[2,3,5,7,11,13,17,19]                ##9699690       #       = 140575
L_modulo_4=[2,3,5,7,11,13,17,19,23]             ##223092870     #       = 2451570
L_modulo_5=[2,3,5,7,11,13,17,19,23,29]          ##6469693230    #       = 54367170
L_modulo_6=[2,3,5,7,11,13,17,19,23,29,31]       ##20056049010   #       = 1346043557
L_modulo_7=[2,3,5,7,11,13,17,19,23,29,31,37]    ##742073813500  #       = 40112098026

a=61   ##[1, 1, 1, 5, 6, 9, 10]
b=610  ##[0, 1, 0, 1, 5, 12, 15]
c=547  ##[1, 1, 2, 1, 8, 1, 3]
d=858  ##[0, 0, 3, 4, 0, 0, 8]
e=1453 ##[1, 1, 3, 4, 1, 10, 8]
f=1958 ##[0, 2, 3, 5, 0, 8, 3]
g=2300 ##[0, 1, 0, 1, 3, 4, 1]
h=2500 ##
## test avec N=510510
(aa,l_a)=generateur_de_cas(510510,a)
(aa,l_b)=generateur_de_cas(510510,b)
(aa,l_c)=generateur_de_cas(510510,c)
(aa,l_d)=generateur_de_cas(510510,d)
(aa,l_e)=generateur_de_cas(510510,e)
(aa,l_f)=generateur_de_cas(510510,f)
(aa,l_h)=generateur_de_cas(510510,h)
## test 1
print(l_a)
print(l_b)
print(l_c)
print(l_d)
print(l_e)
print(l_f)
print(l_h)      
## liste erroné

##1 erreur

lr_1a=[1, 2, 1, 5, 6, 9, 10] ## pos 1
lr_2a=[4, 1, 1, 5, 6, 9, 10] ## pos 0
lr_3a=[1, 1, 2, 5, 6, 9, 10] ## pos 2
lr_4a=[1, 1, 1, 5, 6, 9, 16]

## 2 erreur
lr_5a=[1, 1, 1, 5, 1, 9, 16]


lr_1b=[0, 1, 0, 1, 5, 12, 15]
lr_1c=[1, 1, 2, 1, 8, 1, 3]
lr_1d=[0, 0, 3, 4, 0, 0, 8]
lr_1e=[0, 1, 0, 1, 3, 4, 1]
lr_1f=[0, 1, 0, 1, 3, 4, 1]
lr_1h=[0, 1, 0, 1, 3, 4, 2]
lr_2h=[0, 1, 1, 1, 3, 4, 1]



## test avec N=510510

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

print(decode_fraction_continu(lr_1a,aa))
print(decode_fraction_continu(lr_2a,aa))
print(decode_fraction_continu(lr_3a,aa))

print(reste_chinois1 ([0, 0, 3, 4, 0, 0, 8], aa))

