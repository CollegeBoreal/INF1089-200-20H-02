
# 🎈 Mes premiers scripts en python:

## Python3 code: Afficher le nom d'hote and l'addresse IP 
 Pour afficher le nom d'hote et l'addresse IP de son ordinateur le script doit comporter les etapes suivantes
  
### :a: Importer le  socket library 
```
import socket
What is socket?
```
Deriver du mot anglais, socket est un trou qui laisse passer des choses,comme une prise electrique ou une bouche.
Pour notre cas il designe une associationau niveau de l'IOS entre un programme qui tourne en boucheet et le port de la machinequi lui a ete dedie
En un mot il ecoute le port et repond aux demandes faites par ce port`
``

 ### :b:Definir la fonction qui affichera lee nom d'hote et IP address 
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
### :c:. Inserrer une fonction qui affichera le resultat final puis executer le code 
get_Host_name_IP() #Function call 
  
## Script final 

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

## Output
```
Hostname :   LAPTOP-9J91CJSR
IP :  169.254.162.12
```
