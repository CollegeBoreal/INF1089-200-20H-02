
  # Sending and Receiving Python Objects with sockets with source code :star: :star: :star: :pray: :pray: :pray:
  
  
  
  
  
Nous allons apprendre  à envoyer et à recevoir des données de chaîne via des sockets, et maintenant je veux parler 
des cornichons. Pas la nourriture, mais la technique de sérialisation en Python.


En Python, tout est un objet, et tous vos objets peuvent être sérialisés avec Pickle. La sérialisation est la 
conversion de votre objet en octets et nous envoyons des octets avec des sockets.


Cela signifie que vous pouvez communiquer entre vos programmes python localement ou à distance, via des sockets, en utilisant pickle. Alors maintenant, littéralement n'importe quoi comme des fonctions, un dictionnaire géant, des tableaux, un modèle TensorFlow etc. Cela peuvent être envoyés dans les deux sens entre vos programmes!

:pushpin: Donc d'abord, rapidement, juste au cas où vous ne connaissez pas les cornichons, convertissons un cornichon(pickle) en 
une chaîne d'octets: 
``` 
(base) PS C:\Users\LENOVO\Developer\INF1089-200-20H-02\P.Projets\300111671> python
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pickle
>>> d = {1:"hi", 2: "there"}
>>> msg = pickle.dumps(d)
>>> msg
b'\x80\x03}q\x00(K\x01X\x02\x00\x00\x00hiq\x01K\x02X\x05\x00\x00\x00thereq\x02u.'

```
:pushpin: Maintenant, c'est notre msg, nous venons de l'envoyer. Lorsque nous l'obtenons, nous pouvons le lire avec des 
charges.
```
>>> recd = pickle.loads(msg)
>>> recd
{1: 'hi', 2: 'there'}
>>> 
                       
```




:pushpin: D'accord, mettons-le ensemble et envoyons cela. Notre server-chat.py aura le code suivant pour le message à envoyer:

```
d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)

```



:pushpin: Faire le script complet(nous essayons juste d'illustrer l'envoi d'objets):

```

import socket
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)

```

Dans le cas ci-dessus également, nous envoyons un en-tête qui compte en octets plutôt qu'en caractères, ce qui a 
plus de sens dans les deux cas, vraiment. Maintenant, notre client doit gérer cela. Conformément à ce 
changement, nous modifions notre message de départ en (à la fois initialement, puis une fois le message 
terminé):

```
full_msg = b''

```

:pushpin: Ensuite, nous pouvons supprimer les bits de décodage, nous construisons donc simplement notre message comme 
suit:

```

 full_msg += msg

```

:pushpin: Ensuite, nous attendons le message complet, puis convertissons d'octets en objet avec pickel.loads ():
```
if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))

            new_msg = True
            full_msg = b""
```


:pushpin: Full client.py

```
import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""

```
:pushpin: En les exécutant, j'obtiens:
```

(base) PS C:\Users\LENOVO\Developer\INF1089-200-20H-02\P.Projets\300111671>python server-chat.py
Connection from ('192.168.0.17', 50373) has been established.
b'33        \x80\x03}q\x00(K\x01X\x02\x00\x00\x00hiq\x01K\x02X\x05\x00\x00\x00thereq\x02u.'

```

:pushpin: Et sur le client:

```
(base) PS C:\Users\LENOVO\Developer\INF1089-200-20H-02\P.Projets\300111671>python b300111671.py
new msg len: b'33        '
full message length: 33
16
full message length: 33
32
full message length: 33
43
full msg recvd
b'\x80\x03}q\x00(K\x01X\x02\x00\x00\x00hiq\x01K\x02X\x05\x00\x00\x00thereq\x02u.'
{1: 'hi', 2: 'there'}

```
Merci d'avoir suivie mon tutorial :speech_balloon:  :speech_balloon: 💬 :speech_balloon: :smiley:
