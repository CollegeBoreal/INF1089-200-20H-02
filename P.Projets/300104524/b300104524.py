# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:08:56 2020

@author: 300104524
"""

# Devine mon nombre

from random import randint

nbr_essais_max = 5
nbr_essais = 1
borne_sup = 30
mon_nombre = randint(1,borne_sup)   # nombre choisi par l'ordinateur
ton_nombre = 0                      # nombre proposé par le joueur

print("J'ai choisi un nombre entre 1 et",borne_sup)
print("A vous de le deviner en",nbr_essais_max,"tentatives au maximum !")

while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:
    print("Essai no ",nbr_essais)
    while True:
        try:
            ton_nombre = int(input("Votre proposition : "))
            break
        except ValueError:
            print("Réponse non valide. Réessayez !")  
    if ton_nombre < mon_nombre:
        print("Trop petit")
    elif ton_nombre > mon_nombre:
        print("Trop grand")
    else:
        print("Bravo ! Vous avez trouvé",mon_nombre,"en",nbr_essais,"essai(s)")
    nbr_essais += 1
        
if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
    print("Désolé, vous avez utilisé vos",nbr_essais_max,"essais en vain.")
    print("J'avais choisi le nombre",mon_nombre,".")
    
      
                
