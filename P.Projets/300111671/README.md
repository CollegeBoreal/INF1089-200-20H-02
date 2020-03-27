SERVER SCRIPT
Le programme serveur a toute la logique pour contrôler et réguler le chat,
donc la plupart de la logique de chat est implémentée avec un programme serveur.
La première étape de la communication consiste donc à identifier les utilisateurs,
comment le serveur fait-il cela?
Dans la communication réseau,les utilisateurs sont identifiés par un socket qui n'est rien d'autre qu'une combinaison d'adresse IP
et  de port.
Donc, pour la compréhension humaine, Abbas et Djuma discuteront mais parun réseau,
c'est un processus à deux sockets qui envoie et reçoit des octets.
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
