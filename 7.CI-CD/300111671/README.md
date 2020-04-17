## Bienvenue dans "Bonjour Monde" avec GitHub Actions

# :seven: CI/CD Batch

Ce laboratoire t'apprendra à utiliser les commandes `shell` sous Unix en créant un fichier `entrypoint.sh`, à créer ton propre conteneur `Docker` en créant un fichier `Dockerfile` et t'apprendra les bases du [`CI/CD`](https://en.wikipedia.org/wiki/CI/CD) `Continuous Integration` et `Continuous Delivery` avec le service `github actions` de `github.com`.

Une section [Indices](#fire-indices) est fournie ci-dessous comme documentation d'aide à terminer ce laboratoire.

Tu pourras t'appuyer d'une documentation en ligne pour continuer ce labobratoire en améliorant le fichier `Dockerfile` avec le [cours en ligne suivant](https://www.linkedin.com/learning/docker-essential-training-3-image-creation-management-and-registry/analyzing-a-dockerfile)

## :a: :id:

* Créer un répertoire avec votre :id:

* Créer votre fichier `README.md`

```
$ touch README.md
```

[Participation](Participation.md)

## :b: Laboratoire

:one: Écrire les scripts en suivant le laboratoire ci-dessous dans [Github Leaning Lab](https://lab.github.com/CollegeBoreal):

https://lab.github.com/CollegeBoreal/lab-github-actions:-bonjour-monde


:two: Copier votre scripts dans le cours en remplaçant :id: par votre :id: github :octocat: :

https://github.com/:id:/lab-bonjour-github-actions

- [x] Copier les scripts:

Par example:

  - [x] Copier le fichier `Dockerfile` dans votre :id: `Boréal` 

  - [x] Copier le fichier `entrypoint.sh` dans votre :id: `Boréal` 


- [x] Modifie ton fichier README.md pour plus de documentation


En un mot, récupérer le travail que vous avez fait à travers [Github Leaning Lab](https://lab.github.com/CollegeBoreal) et le mettre dans celui du cours [7.CI-CD](../7.CI-CD)


Le laboratoire vous garantit une note de :five::zero:`%`, ajouter du code en améliorant les scripts embellira la note.

En rappel, pour éxécuter localement son fichier `Dockerfile`, on execute la commande :


* $ `docker build --tag b300111671:1.0 .`
```
Sending build context to Docker daemon  14.85kB
Step 1/4 : FROM python:3
3: Pulling from library/python
7e2b2a5af8f6: Pull complete                                                           09b6f03ffac4: Pull complete                                                           dc3f0c679f0f: Pull complete                                                           fd4b47407fc3: Pull complete                                                           b32f6bf7d96d: Pull complete                                                           3940e1b57073: Pull complete                                                           ce1fce2a6cf9: Pull complete                                                           1f593157bb4c: Pull complete                                                           bde1ccd8f1b8: Pull complete                                                           Digest: sha256:3df040cc8e804b731a9e98c82e2bc5cf3c979d78288c28df4f54bbdc18dbb521
Status: Downloaded newer image for python:3
 ---> b55669b4130e
Step 2/4 : ADD script.py /
 ---> a35eb36603f7
Step 3/4 : RUN pip install pystrich
 ---> Running in e7e741855a50
Collecting pystrich
  Downloading pyStrich-0.8.tar.gz (981 kB)
Collecting Pillow
  Downloading Pillow-7.1.1-cp38-cp38-manylinux1_x86_64.whl (2.1 MB)
Building wheels for collected packages: pystrich
  Building wheel for pystrich (setup.py): started
  Building wheel for pystrich (setup.py): finished with status 'done'
  Created wheel for pystrich: filename=pyStrich-0.8-py3-none-any.whl size=1107396 sha256=a4e5bbdba69554060bdece0e747ee9100049c6ca5a91fa451d864c61cfccd088
  Stored in directory: /root/.cache/pip/wheels/7b/19/71/add9414f3633ad86fd47e0de58c0c577bf9c33ab5da5e20dd9
Successfully built pystrich
Installing collected packages: Pillow, pystrich
Successfully installed Pillow-7.1.1 pystrich-0.8
Removing intermediate container e7e741855a50
 ---> 3f7188621dde
Step 4/4 : CMD [ "python", "./script.py" ]
 ---> Running in e5ac40f67651
Removing intermediate container e5ac40f67651
 ---> 500137778fbe
Successfully built 500137778fbe
Successfully tagged b300111671:1.0
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.

```

* $ docker run --tty --env INPUT_MON_NOM="abbas" b300111671:1.0

```

    XX  XX  XX  XX  XX  XX  XX  XX  XX  XX
    XX  XX  XX  XXXX    XX  XX      XX  XXXX
    XXXX  XX    XX    XXXX    XXXXXX    XX
    XX    XXXX      XXXX  XXXX        XX  XX
    XX    XX    XXXX      XX  XX
    XXXXXX  XX  XX  XX  XXXX  XXXXXX    XXXX
    XXXX  XX          XXXX  XXXX    XX  XX
    XXXX      XX  XXXXXX  XXXX        XXXXXX
    XX    XX      XX  XXXXXX    XX  XX  XX
    XX  XX    XXXX  XX  XXXX    XXXXXX    XX
    XXXX      XX  XX    XXXX  XXXXXX  XX
    XX  XX  XXXXXX  XX    XX  XXXX  XX    XX
    XX          XX      XXXX  XX  XXXXXXXX
    XXXXXX  XXXXXX  XXXX  XXXXXXXXXXXX    XX
    XX  XXXXXX  XX    XX      XXXXXXXX
    XX    XX    XX  XX  XX    XXXXXXXXXX  XX
    XX  XXXXXXXX  XX    XXXXXX  XX  XX  XX
    XX  XX        XXXX  XX  XXXX  XX      XX
    XXXX  XX  XXXX    XX      XX  XXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    
    ```


Pour visualiser les couches images de l'image créée

* $ 
```
$ docker image history b300111671:1.0
```
 docker image history b300111671:1.0                                                 IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
500137778fbe        18 minutes ago      /bin/sh -c #(nop)  CMD ["python" "./script.p…   0B
3f7188621dde        18 minutes ago      /bin/sh -c pip install pystrich                 23.8MB
a35eb36603f7        19 minutes ago      /bin/sh -c #(nop) ADD file:b94ab6a4d436803f6…   174B
b55669b4130e        7 hours ago         /bin/sh -c #(nop)  CMD ["python3"]              0B
<missing>           7 hours ago         /bin/sh -c set -ex;   wget -O get-pip.py "$P…   6.34MB
<missing>           7 hours ago         /bin/sh -c #(nop)  ENV PYTHON_GET_PIP_SHA256…   0B
<missing>           7 hours ago         /bin/sh -c #(nop)  ENV PYTHON_GET_PIP_URL=ht…   0B
<missing>           7 hours ago         /bin/sh -c #(nop)  ENV PYTHON_PIP_VERSION=20…   0B
<missing>           7 hours ago         /bin/sh -c cd /usr/local/bin  && ln -s idle3…   32B
<missing>           7 hours ago         /bin/sh -c set -ex   && wget -O python.tar.x…   106MB
<missing>           7 hours ago         /bin/sh -c #(nop)  ENV PYTHON_VERSION=3.8.2     0B

```
# :three: Amélioration

## ASCII QR code

* Créer un nouveau fichier appelé `Dockerfile`

`> nano .\Dockerfile`

`> cat .\Dockerfile`
```
FROM python:3

ADD script.py /

RUN pip install pystrich

CMD [ "python", "./script.py" ]
```

* Créer un fichier de script Python appelé script.py et ajouter ce script dedans:

```
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())

```

* Maintenant, je suis prêt à créer une image à partir de ce Dockerfile en lancant cette comande:

```
> docker build -t python-300111671 .
```
```
Sending build context to Docker daemon  14.85kB
Step 1/4 : FROM python:3
 ---> b55669b4130e
Step 2/4 : ADD script.py /
 ---> Using cache
 ---> a35eb36603f7
Step 3/4 : RUN pip install pystrich
 ---> Using cache
 ---> 3f7188621dde
Step 4/4 : CMD [ "python", "./script.py" ]
 ---> Using cache
 ---> 500137778fbe
Successfully built 500137778fbe
Successfully tagged python-300111671:latest
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.

```
* Pour verifier que l'image est creer lancez cette commande:

```
> docker images
```
* Lancez la nouvelle image en entrant :

```
> docker run python-300111671
```


    XX  XX  XX  XX  XX  XX  XX  XX  XX  XX
    XX  XX  XX  XXXX    XX  XX      XX  XXXX
    XXXX  XX    XX    XXXX    XXXXXX    XX
    XX    XXXX      XXXX  XXXX        XX  XX
    XX    XX    XXXX      XX  XX
    XXXXXX  XX  XX  XX  XXXX  XXXXXX    XXXX
    XXXX  XX          XXXX  XXXX    XX  XX
    XXXX      XX  XXXXXX  XXXX        XXXXXX
    XX    XX      XX  XXXXXX    XX  XX  XX
    XX  XX    XXXX  XX  XXXX    XXXXXX    XX
    XXXX      XX  XX    XXXX  XXXXXX  XX
    XX  XX  XXXXXX  XX    XX  XXXX  XX    XX
    XX          XX      XXXX  XX  XXXXXXXX
    XXXXXX  XXXXXX  XXXX  XXXXXXXXXXXX    XX
    XX  XXXXXX  XX    XX      XXXXXXXX
    XX    XX    XX  XX  XX    XXXXXXXXXX  XX
    XX  XXXXXXXX  XX    XXXXXX  XX  XX  XX
    XX  XX        XXXX  XX  XXXX  XX      XX
    XXXX  XX  XXXX    XX      XX  XXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



✔

# :fire: Indices 

Tu auras besoin de:

:round_pushpin: créer et manipuler une branche avec `git`:

https://github.com/CollegeBoreal/Tutoriels/tree/master/0.GIT/.branch

:round_pushpin: Créer une demande d'extraction `pull request` par le biais de l'interface web de github: 

https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request#creating-the-pull-request

:round_pushpin: Creér Répertoire Imbriqué

par exemple pour créer `.github/workflows` utilise la commande suivante avec le parametre `-p`:

```
$ mkdir -p .github/workflows
```
