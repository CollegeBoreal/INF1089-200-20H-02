   def manip(nombres,rem_value,val_ajout,val_ind):
    
    print(" Liste initiale ".center(50, '-'))
    print(nombres, '\n')
    print(" Liste trier: {} ".format(sorted(nombres)))

#print(nombres, '\n')

  ##  ajoutez l’élément 12 à la liste et afﬁchez laliste;
    print(" Ajout d'un element ".center(50, '-')) 
    nombres.append(val_ajout) 
    print(nombres, '\n')

 ## renversez et afﬁchez la liste; 
  
    print(" list inverser ".center(50, '-')) 
  
    nombres.reverse() 

    print(nombres, '\n')

 ## afﬁchez l’indice de l’élément 17;
    if val_ind not in nombres:
        print("La valeur que vous voulez son index nest pas la list")
    else:
        print(" Indice d'un element ".center(50, '-'))
        print(nombres.index(val_ind), '\n')

## enlevez l’élément 38 et afﬁchez la liste;

    print(" Retrait d'un element ".center(50, '-')) 

    if rem_value not in nombres:
        print("La valeur nest pas la liste")
    else:
        nombres.remove(rem_value) 
        print(nombres, '\n')

## afﬁchez la sous-liste du 2e au 3e élément; 

    print(" Indicage ".center(50, '-'))


## afﬁchez la sous-liste du 2e au3e élément; 

    print("nombres[1:3] =", nombres[1:3]) 

 ## afﬁchez la sous-liste du début au 2e élément; 

    print("nombres[:2] =", nombres[:2]) 



    print("nombres[2:] =", nombres[2:]) 

 ##  afﬁchez la sous-liste du3e élément à laﬁn de la liste;


    print("nombres[:] =", nombres[:]) 

 ## extraire de derniers elements de la liste 

    print("nombres[-1] =", nombres[-1])
    

def main():
    print("Pour tester mon program")
    #manip([236,179,3,10,9,13],1,1000,17)
    manip([17, 38, 10, 25, 72],38,12,17)
    
if __name__=="__main__":
    main()
    
