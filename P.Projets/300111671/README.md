
  # DEVELOPING CHAT APPLICATION IN PYTHON WITH SOURCE CODE


Le programme serveur a toute la logique pour contrôler et réguler le chat,
donc la plupart de la logique de chat est implémentée avec un programme serveur.
La première étape de la communication consiste donc à identifier les utilisateurs,
comment le serveur fait-il cela?
Dans la communication réseau,les utilisateurs sont identifiés par un socket qui n'est rien d'autre qu'une combinaison d'adresse IP
et  de port.
Donc, pour la compréhension humaine, Abbas et Djuma discuteront mais parun réseau,
c'est un processus à deux sockets qui envoie et reçoit des octets.

##SERVER SCRIPT

Les étapes impliquées dans ce processus sont les suivantes:

Create socket

Communicate the socket address

Keep waiting for an incoming connection request/s

Connect to client

Receive the message

Decode the destination user and select the socket

Send a message to the intended client

Keep repeating step 5 & 6 as per users wish

Exit i.e. end the communication by terminating the connection


###Script client

Le script client est exécuté par l'utilisateur, donc le même code client sera exécuté par un utilisateur différent mais chacun aura un socket séparé afin d'avoir son canal de communication unique. 
Le script client est généralement léger car il a très peu de travail, c'est-à-dire qu'il ne se connecte qu'au serveur et envoie et reçoit des messages. Les étapes impliquées dans le script client sont les suivantes:


Create a unique client socket per instance/user

Connect to the server with given socket address (IP and port)

Send and receive messages

Repeat step 3 as per configuration

Close the connection


Dans le programme ci-dessus, chaque utilisateur doit exécuter le script client séparément après l'exécution du script serveur. 
Une fois que le programme client se connecte au serveur, le client doit s'enregistrer en tant qu'utilisateur en donnant un nom d'utilisateur, donc le reste de la communication se fera en utilisant le nom d'utilisateur.
