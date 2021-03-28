
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


## test 1
"""
(ln,lr) = generateur_de_cas_liste(L_modulo_1,61)
print("test 1 N=30030 ; k=61")
print("sans erreur :" ,ln,lr)
lr_error=lr
lr_error[0]=0
print("test",reste_chinois1(ln,lr))
print(détection_1_erreur(ln,lr))
##print("brute force 0 erreur",brute_force_hamming(ln,lr,1))
##print("brute force 1 erreur",brute_force_hamming(ln,lr_error,1))

"""
