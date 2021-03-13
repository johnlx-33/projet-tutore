##Projet Tutoré


#!/usr/bin/env python
# -*- coding: cp1252 -*-
from fractions import gcd

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
if i :
    print()
    print ()
    print ("********************************************************************************")
    print ("*        Résolution d'équations par le théorème des restes chinois             *")
    print ("*                                  Voir :                                      *")
    print ("* [url]http://www.bibmath.net/dico/index.php3?action=affiche&quoi=./c/chinois.html[/url]  *")
    print ("********************************************************************************")
    print ()
    print ()
    Modulos, Restes, Produits_partiels, Inverses, nb_equa, Mods_prod, Som_prod,a,vrai =[],[],[],[],0,1,0,"",0
    while vrai != 1:
        a=input("De combien d'équations disposez-vous ? ")
        nb_equa,vrai=entree_entiers(a,0)
        if not vrai or nb_equa <2:
            print ("Entrée incorrecte, veillez recommencer")
    print
    for i in range(nb_equa):
        vrai,vrai2=0,0
        while vrai2 != 1:
            while vrai != 1:
                a=input("Entrer le reste  no "+str(i+1)+" : ")
                r,vrai=entree_entiers(a,0)
                if not vrai:
                    print ("Entrée incorrecte, veillez recommencer")
            vrai=0
            while vrai != 1:
                a=input("Entrer le modulo no "+str(i+1)+" : ")
                m,vrai=entree_entiers(a,0)
                if not vrai or r >= m:
                    print ("Entrée incorrecte, veillez recommencer")
            p=gcd(r,m)
            if p == 1:
                vrai2=1
            else:
                print ("Ces 2 nombres ne sont pas premiers entre eux, veillez recommencer")
        Restes.append(r)
        Modulos.append(m)
        print ("----------------------")
        Mods_prod*=m

    print()
    print ("                           Votre problème :")
    print ("          Trouver le plus petit nombre entier naturel x tel que ")
    for i in range(nb_equa):
        print ('            x = '+str(Restes[i])+'   (modulo '+str(Modulos[i])+")")
    print()
    print()
    print ("                           **************")
    print ("                           * Résolution *")
    print ("                           **************")
    print ()
    print ("Le produit des modulos est :",Mods_prod)

    for i in range(nb_equa):
        pp_i=Mods_prod//Modulos[i]
        print ("Produit_partiel n° "+str(i+1)+" : "+str(Mods_prod)+"/"+str(Modulos[i])+" = ",pp_i, end="")
        Produits_partiels.append(pp_i)
        inv_i= int(xeuklid(pp_i,Modulos[i]))
        print ("     L'inverse, modulo "+str(Modulos[i])+", de "+str(pp_i)+" est : ",inv_i)
        Som_prod+=Restes[i]*pp_i*inv_i
        Inverses.append(inv_i)


                                                   
    print ( )                                            
    print ('                         On a alors  :')
    for i in range(nb_equa):
        if i>0:
            print ("+",end="")
        print (str(Restes[i])+"*"+str(Produits_partiels[i])+"*"+str(Inverses[i]),end="")
    print ("= "+str(Som_prod))
    print ()
    print ("                         Et enfin : ")
    print ("              ",Som_prod,"modulo "+str(Mods_prod)+" =",Som_prod%Mods_prod)
     
