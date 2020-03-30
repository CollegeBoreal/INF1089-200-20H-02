# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:36:16 2020

@author: acer
"""
     
    ## programme de gestion de l'ATM,

    #tout l'utilisateur a besoin d'un mot de passe pour entrer dans le programme,
    #puis une liste apparaît:

 # 1. retirer de l'argent.
 # 2. appuyez sur 2 pour transférer de l'argent.
 # 3.pour déposer de l'argent.
 # 4. pour afficher le solde actuel.


numéros_de_comptes=[23410324,132432,9865665,596900,4654680,76432,86785342,5678888,734533,456045456]
clé_de_comptes=[2344,5433,7523,9806,4560,6454,5343,6565,3455,5677]
solde_de_comptes=[20000,10000,0,0,0,0,0,0,0,0]

num_compte=int(input('Bienvenue à ATM, entrez votre numéro de compte:'))
compte_trouvé=False
counter=-1
for a in numéros_de_comptes:
    counter=counter+1
    if a==num_compte:
        compte_trouvé=True
        break

if compte_trouvé == False:
    print("Le numéro de compte n'existe pas")
else:
    clé_de_compte=int(input('Entrez votre mot de passe'))
    if clé_de_compte==clé_de_comptes[counter]:
        option=int(input("1.Retirer de l'argent.\n2.Transférer de l'argent sur un autre compte.\n3.Dépôt de l'argent.\n4.Afficher le solde.\n"))
        if option==1:
            argent=int(input("Entrez le montant d'argent:"))
            if argent>solde_de_comptes[counter]:
                print("Pas assez d'argent dans votre solde")
