
# 🎈 Mes premiers scripts en python:

## Python3 code: Afficher le nom d'hote et l'addresse IP 
 Pour afficher le nom d'hote et l'addresse IP de son ordinateur le script doit comporter les etapes suivantes
  
### :one: Importer le  socket library 
```
import socket
What is socket?
```
Deriver du mot anglais, socket est un trou qui laisse passer des choses,comme une prise electrique ou une bouche.
Pour notre cas il designe une associationau niveau de l'IOS entre un programme qui tourne en boucheet et le port de la machinequi lui a ete dedie.
En un mot  importer le socket c'est faire communiquer deux noeuds a un reseau c'est a dire le port et l'ip

 ### :two: Definir la fonction qui affichera le nom d'hote et IP address 
 ```
 
En programmation, les fonctions sont très utiles pour réaliser plusieurs fois la même opération au sein d'un programme. Elles rendent également le code plus lisible et plus clair en le fractionnant en blocs logiques.

Vous connaissez déjà certaines fonctions Python. Par exemple math.cos(angle) du module math renvoie le cosinus de la variable angle exprimé en radian. Vous connaissez aussi des fonctions internes à Python comme range() ou len(). Pour l'instant, une fonction est à vos yeux une sorte de « boîte noire » (voir figure 1) :

À laquelle vous passez aucune, une ou plusieurs variable(s) entre parenthèses. Ces variables sont appelées arguments. Il peut s'agir de n'importe quel type d'objet Python.
Qui effectue une action.
Et qui renvoie un objet Python ou rien du tout.
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
  ```
  
### :three:Inserrer une fonction qui affichera le resultat final puis executer le code 
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


### :ofive: Output
```
Hostname :   LAPTOP-9J91CJSR
IP :  169.254.162.12
```
