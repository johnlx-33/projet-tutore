
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
L_modulo_26=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]


k=1
for i in range(len(L_modulo_26)):
        k=k*L_modulo_26[i]
print(k)

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
p=72968059924902415062132347  ##[0, 2, 0, 5, 7, 1, 16, 2, 22, 25, 26, 34, 18, 19, 30, 24, 24, 22, 52, 56, 4, 78, 54, 68, 82, 58, 39, 88, 54,
                               ##11, 62, 73, 134, 126, 102, 142, 135, 92, 159, 48, 119, 33, 16, 77, 28, 29, 35, 89, 86, 163, 150]
k=1000000000000000 ##10^16  ##[0, 1, 0, 6, 10, 12, 12, 8, 5, 19, 1, 1, 1, 16, 40, 47, 52, 50, 24, 37, 22, 21, 28, 69, 45, 91
                    ##, 69, 39, 55, 101, 63, 71, 96, 76, 23, 59, 56, 61, 43, 170, 7, 160, 13, 137, 140, 210, 95, 76, 54, 54, 10]
## test avec N=510510
(aa,l_a)=generateur_de_cas(510510,a)
(aa,l_b)=generateur_de_cas(510510,b)
(aa,l_c)=generateur_de_cas(510510,c)
(aa,l_d)=generateur_de_cas(510510,d)
(aa,l_e)=generateur_de_cas(510510,e)
(aa,l_f)=generateur_de_cas(510510,f)
(aa,l_h)=generateur_de_cas(510510,h)


## test avec 52 nb premier
(bb,l_i)= generateur_de_cas_liste(L_modulo_25,i)
(bb,l_j)= generateur_de_cas_liste(L_modulo_25,j)
(bb,l_k)= generateur_de_cas_liste(L_modulo_25,k)
(bb,l_l)= generateur_de_cas_liste(L_modulo_25,l)
(bb,l_m)= generateur_de_cas_liste(L_modulo_25,m)
(bb,l_n)= generateur_de_cas_liste(L_modulo_25,n)
(bb,l_o)= generateur_de_cas_liste(L_modulo_25,o)


## test avec 100 nb premier

(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,l_k)= generateur_de_cas_liste(L_modulo_26,k)




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
print(l_p)
## test avec N=510
print("borne pour 1 erreur  "+ str(calcule_borne(bb,1)))
print("")
print("borne pour 2 erreur  "+ str(calcule_borne(bb,2)))
print("")
print("borne pour 3 erreur  "+ str(calcule_borne(bb,3)))
print("")
print("borne pour 4 erreur  "+ str(calcule_borne(bb,4)))
print("")
print("borne pour 5 erreur  "+ str(calcule_borne(bb,5)))
print("")
print("borne pour 6 erreur  "+ str(calcule_borne(bb,6)))
print("")
print("borne pour 7 erreur  "+ str(calcule_borne(bb,7)))
print("")
print("borne pour 8 erreur  "+ str(calcule_borne(bb,8)))
print("")
print("borne pour 9 erreur  "+ str(calcule_borne(bb,9)))
print("")
print("borne pour 10 erreur "+ str(calcule_borne(bb,10)))
print("")
print("borne pour 11 erreur "+ str(calcule_borne(bb,11)))
print("")
print("borne pour 12 erreur "+ str(calcule_borne(bb,12)))
print("")
print("borne pour 13 erreur "+ str(calcule_borne(bb,13)))
print("")
print("borne pour 14 erreur "+ str(calcule_borne(bb,14)))
print("")
print("borne pour 15 erreur "+ str(calcule_borne(bb,15)))
print("")



## lr_p1 15 erreur sur les 15 premiere pos
lr_p1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162, 24, 115, 77, 146, 226, 15]

## lr_p2 15 erreur sur le 15 derniere pos
lr_p2= [1, 2, 2, 4, 4, 4, 5, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0]

## lr_p3 5 erreur sur les premiere pos

lr_p3= [0, 0, 0, 0, 0, 4, 5, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162, 24, 115, 77, 146, 226, 15]

## lr_p4 5 erreur sur les derniere pos

lr_p4= [1, 2, 2, 4, 4, 4, 5, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162, 24,0,0,0,0,0]


## lr_p5 6 erreur sur les premiere pos
lr_p5= [0,0,0,0,0,0,5,4,16,17,15,33,10,32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162, 24, 115, 77, 146, 226, 15]

## lr_p6 6 erreur sur les derniere pos
lr_p6=[1, 2, 2, 4, 4, 4, 5, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162,0,0,0,0,0,0]

## lr_p7 7 erreur sur les premiere pos
lr_p7=[0,0,0,0,0,0,0, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162, 24, 115, 77, 146, 226, 15]

## lr_p8 7 erreur sur les derniere pos
lr_p8=[1, 2, 2, 4, 4, 4, 5, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185,0,0,0,0,0,0, 0]

## lr_p9 8 erreur sur les premiere pos
lr_p9=[0, 0, 0, 0, 0, 0, 0, 0, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 185, 162, 24, 115, 77, 146, 226, 15]

## lr_p10 8 erreur sur les derniere pos
lr_p10= [1, 2, 2, 4, 4, 4, 5, 4, 16, 17, 15, 33, 10, 32, 3, 13, 26, 51, 32, 34, 15, 71, 22, 78, 47, 26, 76, 73, 49, 35, 57, 99, 123, 96, 40, 135, 92, 107, 137, 148, 30, 137, 156, 0, 0, 0, 0, 0, 0, 0, 0]

## lr_p11 7 erreur sur pos alterné à la fin

lr_p11=[0, 2, 0, 5, 7, 1, 16, 2, 22, 25, 26, 34, 18, 19, 30, 24, 24, 22, 52, 56, 4, 78, 54, 68, 82, 58, 39, 88, 54, 11, 62, 73, 134, 126, 102, 142, 135, 92, 0, 48, 0, 33, 0, 77, 0, 29, 0, 89, 0, 163,0]

## lr_p12 7 erreur sur pos alterné à partir 4eme pos

lr_p12=[0, 2, 0, 5, 0, 1, 0, 2, 0, 25, 0, 34, 0, 19, 0, 24,0, 22, 52, 56, 4, 78, 54, 68, 82, 58, 39, 88, 54,11, 62, 73, 134, 126, 102, 142, 135, 92, 159, 48, 119, 33, 16, 77, 28, 29, 35, 89, 86, 163, 150]

print("")
print("essaie 5 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p3))
tmp=decode_fraction_continu(lr_p3,bb,15)
print(tmp)

print("")
print("essaie 5 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p4))
tmp=decode_fraction_continu(lr_p4,bb,15)
print(tmp)

print("")
print("essaie 6 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p5))
tmp=decode_fraction_continu(lr_p5,bb,15)
print(tmp)

print("")
print("essaie 6 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p6))
tmp=decode_fraction_continu(lr_p6,bb,15)
print(tmp)


print("")
print("essaie 7 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p7))
tmp=decode_fraction_continu(lr_p7,bb,15)
print(tmp)

print("")
print("essaie 7 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p8))
tmp=decode_fraction_continu(lr_p8,bb,15)
print(tmp)

print("")
print("essaie 8 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p9))
tmp=decode_fraction_continu(lr_p9,bb,8)
print(tmp)

print("")
print("essaie 8 erreur avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p10))
tmp=decode_fraction_continu(lr_p10,bb,8)
print(tmp)

print("")
print("essaie 7 erreur avec 51 nb premier alterné fin ")
print("")
print("n-uplet corespondant <->"+str(lr_p11))
tmp=decode_fraction_continu(lr_p11,bb,8)
print(tmp)

print("")
print("essaie 7 erreur avec 51 nb premier alteren 4eme pos")
print("")
print("n-uplet corespondant <->"+str(lr_p12))
tmp=decode_fraction_continu(lr_p12,bb,8)
print(tmp)


print("")
print("essaie 15 erreur premiere pos avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p1))
tmp=decode_fraction_continu(lr_p1,bb,15)
print(tmp)

print("")
print("essaie 15 erreur derniere pos avec 51 nb premier")
print("")
print("n-uplet corespondant <->"+str(lr_p2))
tmp=decode_fraction_continu(lr_p2,bb,15)
print(tmp)

print("")
print("essaie 7 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(7,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))

print("")
print("essaie 7 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(7,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))

print("")
print("essaie 7 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(7,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))

print("")
print("essaie 8 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(8,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))

print("")
print("essaie 9 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(9,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))

print("")
print("essaie 10 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(10,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))


print("")
print("essaie 12 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(12,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))

print("")
print("essaie 15 erreurs avec 100 nb premier")
print("")
(cc,l_p)= generateur_de_cas_liste(L_modulo_26,p)
(cc,lr_p15)=create_error(15,cc,l_p)
print("n-uplet corespondant <->"+str(lr_p15))
tmp=decode_fraction_continu(lr_p15,cc,15)
print("modulo supposé erroné"+str(tmp))


