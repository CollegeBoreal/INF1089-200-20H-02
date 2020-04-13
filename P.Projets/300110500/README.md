
# 🎈 Mon premier script en python:

## Python3 code: Afficher le nom d'hote et l'addresse IP
```
En windows CMD, la commande ipconfig permet d'afficher les parametres du reseau tel que l'addresse ip de l'hote, 
le masque de sous reseau etc
En python nous pouvons avoir le meme resultat en utilisant un script
Pour mon cas j'ai realiser un script qui permet afficher le nom d'hote et l'addresse IP de son ordinateur.
Le processus de ce script doit suit les etapes suivante.
```
### :one: Importation du socket library 

import socket
What is socket?
Deriver du mot anglais, socket est un trou qui laisse passer des choses,comme une prise electrique ou une bouche.
Pour notre cas il designe une associationau niveau de l'IOS entre un programme qui tourne en boucheet et 
le port de la machine qui lui a ete dedie.
En un mot  importer le socket c'est faire communiquer deux noeuds a un reseau c'est a dire le port et l'ip

### :two: Definir la fonction et ses parametres tels que le nom d'hote et IP address 
 En programmation python les fonction sont utiles pour realiser plusieurs fois la meme operation.
 Elle rend le code plus lisible et clair en le fonctionnant en bloc logiques.
 D'ou la representation de la fonction de facon suivante:
 ```
 def nomDeLaFonction(liste de param�tres):
    ...
    bloc d'instructions
    ...
```
Voici le nom de la fonction et les parametres de ip address et hostname
 ```
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
```
### :three: Appel de la foction
L'appel d'une fonction qui renvoie une valeur est une expression, et on peut dès lors l'utiliser partout 
là où une expression est acceptée. 

```
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
     except: 
        print("Unable to get Hostname and IP") 
 get_Host_name_IP() #Function call 
 ````
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
