
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
En programmation, les fonctions sont tres utiles pour realiser plusieurs fois la même operation au sein d'un programme. Elles rendent egalement le code plus lisible et plus clair en le fractionnant en blocs logiques.
La syntaxe pour d´efinir une fonction :
def nomdefonction(liste_de_parametres) :
bloc_instructions
Le bloc instructions effectue les calculs pour rrealiser les taaches confiees a la fonction
definie. Les calculs peuvent produire de nouvelles valeurs que l’on peut renvoyer dans
une expression (affecter a  variable, utiliser comme arguments d’une autre fonction).
Pour cela, on utilise l’instruction return valeur (ou return tuple de valeurs). Lors qu’une
instruction return valeur est executee dans le bloc, la valeur est renvoy´ee et l’ex´ecution
de la fonction s’arrete ; toutes autres instructions apres cette instruction return valeur
sont abandonn´ees. Dans le bloc instructions on peut avoir plusieurs instructions return,
```
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
