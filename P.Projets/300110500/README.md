
# 🎈 Mon premier script en python:

## Python3 code: Afficher le nom d'hote et l'addresse IP 
 Pour afficher le nom d'hote et l'addresse IP de son ordinateur le script doit comporter les etapes suivantes
  
### :one: Importer le  socket library 

```
import socket
```
What is socket?

```
Deriver du mot anglais, socket est un trou qui laisse passer des choses,comme une prise electrique ou une bouche.
Pour notre cas il designe une associationau niveau de l'IOS entre un programme qui tourne en boucheet et 
le port de la machine qui lui a ete dedie.
En un mot  importer le socket c'est faire communiquer deux noeuds a un reseau c'est a dire le port et l'ip
```
### :two: Definir la fonction qui affichera le nom d'hote et IP address 

 ```
 En programmation python les fonction sont utiles pour realiser plusieurs fois la meme operation.
 Elle rend le code plus lisible et clair en le fonctionnant en bloc logiques.
 D'ou la representation de la fonction de facon suivante:
 def nomDeLaFonction(liste de param�tres):
    ...
    bloc d'instructions
    ...
    
 ```

 
 ```
 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
  ```
L'appel d'une fonction qui renvoie une valeur est une expression, et on peut dès lors l'utiliser partout là où une expression est         acceptée. 
        
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
  ```
  
### :three: Inserrer une fonction qui affichera le resultat final puis executer le code 
 get_Host_name_IP() #Function call 
  
### :four: Script final 

```
get_Host_name_IP() ]
  
import socket 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
  
get_Host_name_IP()
```


### :five: Output
```
Hostname :   LAPTOP-9J91CJSR
IP :  169.254.162.12
```
