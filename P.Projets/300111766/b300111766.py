                                             STRUCTURES DE DONNEES PYTON
                                             
                                            
 déﬁnir la liste: liste =[17, 38, 10, 25, 72],puis effectuez les actions suivantes: 
 
 – triez etafﬁchez la liste;
 
 – ajoutez l’élément 12 à la liste et afﬁchez laliste; 
 
 – renversez et afﬁchez la liste; 
 
 – afﬁchez l’indice de l’élément 17; 
 
 – enlevez l’élément 38 et afﬁchez la liste;
 
 – afﬁchez la sous-liste du 2e au 3e élément; 
 
 – afﬁchez la sous-liste du début au 2e élément; 
 
 – afﬁchez lasous-liste du 3e élément à laﬁndelaliste; 
 
 – afﬁchez la sous-liste complète de la liste;
  
  – afﬁchez le dernier élément en utilisant unindiçage négatif
  
  
  ## Liste initiale
  
  nombres = [17, 38, 10, 25, 72] 
  
print(" Liste initiale ".center(50, '-'))

print(nombres, '\n')
  
   ##  triez et afﬁchez la liste;
  
 nombres = [17, 38, 10, 25, 72]
  
print(" Liste initiale ".center(50, '-'))

print(nombres, '\n')

  ##  ajoutez l’élément 12 à la liste et afﬁchez laliste;
  
  print(" Ajout d'un element ".center(50, '-')) 
  
nombres.append(12) 

print(nombres, '\n')

 ## renversez et afﬁchez la liste; 
  
 print(" Retournement ".center(50, '-')) 
  
nombres.reverse() 

print(nombres, '\n')

 ## afﬁchez l’indice de l’élément 17;
  
print(" Indice d'un element ".center(50, '-'))

print(nombres.index(17), '\n')

## enlevez l’élément 38 et afﬁchez la liste;

print(" Retrait d'un element ".center(50, '-')) 

nombres.remove(38) 

print(nombres, '\n')

## afﬁchez la sous-liste du 2e au 3e élément; 

print(" Indicage ".center(50, '-'))


## afﬁchezlasous-listedu2eau3eélément; 

print("nombres[1:3] =", nombres[1:3]) 

 ## afﬁchez la sous-liste du début au 2e élément; 

print("nombres[:2] =", nombres[:2]) 



print("nombres[2:] =", nombres[2:]) 

 ##  afﬁchez la sous-liste du3eélément à laﬁn de laliste;


print("nombres[:] =", nombres[:]) 

 ## extraire de derniers elements de la liste 

print("nombres[-1] =", nombres[-1])


## _LA FONCTION mean()_




 







