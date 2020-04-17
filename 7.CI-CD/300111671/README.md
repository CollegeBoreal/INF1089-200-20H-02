## 🎡Bienvenue dans "Bonjour Monde" avec GitHub Actions🎡

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

Pour ceci il faut rentrer d'abord dans le repertoire `action-a`

* $ cd action-a

* $ docker build --tag b300108234:1.0 .

```
PS C:\Users\User\Developer\INF1089-200-20H-02\7.CI-CD\300108234\action-a> docker build --tag b300108234:1.0 .                                                                             Sending build context to Docker daemon  4.096kB
Step 1/4 : FROM debian:9.5-slim
9.5-slim: Pulling from library/debian
f17d81b4b692: Pull complete                                                                  Digest: sha256:ef6be890318a105f7401d0504c01c2888daa5d9e45b308cf0e45c7cb8e44634f
Status: Downloaded newer image for debian:9.5-slim
 ---> 4b4471f624dc
Step 2/4 : ADD entrypoint.sh /entrypoint.sh
 ---> bc1047a8c62e
Step 3/4 : RUN chmod +x /entrypoint.sh
 ---> Running in 86df95e96f6d
Removing intermediate container 86df95e96f6d
 ---> 2e6da2d3a0e9
Step 4/4 : ENTRYPOINT ["/entrypoint.sh"]
 ---> Running in aec02719c1c3
Removing intermediate container aec02719c1c3
 ---> cd36b92a8005
Successfully built cd36b92a8005
Successfully tagged b300108234:1.0
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.
```

* $ docker run --tty --env INPUT_MON_NOM="halima" b300108234:1.0

`Bonjour tout le monde mon nom est halima`

Pour visualiser les couches images de l'image créée

* $ docker image history b300108234:1.0
```
$ docker image history b300108234:1.0                                                                             IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
cd36b92a8005        11 minutes ago      /bin/sh -c #(nop)  ENTRYPOINT ["/entrypoint.…   0B   
2e6da2d3a0e9        11 minutes ago      /bin/sh -c chmod +x /entrypoint.sh              79B  
bc1047a8c62e        11 minutes ago      /bin/sh -c #(nop) ADD file:c63a97c860b6e940d…   79B  
4b4471f624dc        18 months ago       /bin/sh -c #(nop)  CMD ["bash"]                 0B   
<missing>           18 months ago       /bin/sh -c #(nop) ADD file:f8f26d117bc4a9289…   55.3M
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
> docker build -t python-300108234 .
```
```
Sending build context to Docker daemon  16.38kB
Step 1/4 : FROM python:3
3: Pulling from library/python
f15005b0235f: Pull complete                                                         41ebfd3d2fd0: Pull complete                                                         b998346ba308: Pull complete                                                         f01ec562c947: Pull complete                                                         fdd2d569da3e: Pull complete                                                         ac3886b74a9f: Pull complete                                                         3c783a9b35dd: Pull complete                                                         ce16dda809f6: Pull complete                                                         Digest: sha256:76947ddb1731d5e347edb349c9315e473bccceefd919df0301c834176d53d1f9
Status: Downloaded newer image for python:3
 ---> d47898c6f4b0
Step 2/4 : ADD script.py /
 ---> 0553be1301cc
Step 3/4 : RUN pip install pystrich
 ---> Running in f3a628535321
Collecting pystrich
  Downloading pyStrich-0.8.tar.gz (981 kB)
Collecting Pillow
  Downloading Pillow-7.1.1-cp38-cp38-manylinux1_x86_64.whl (2.1 MB)
Building wheels for collected packages: pystrich
  Building wheel for pystrich (setup.py): started
  Building wheel for pystrich (setup.py): finished with status 'done'
  Created wheel for pystrich: filename=pyStrich-0.8-py3-none-any.whl size=1107396 sha256=b89839a6406b24a670d0229ba169a3fb32e1caa60ac652d5e7af90c2c72527ca
  Stored in directory: /root/.cache/pip/wheels/7b/19/71/add9414f3633ad86fd47e0de58c0c577bf9c33ab5da5e20dd9
Successfully built pystrich
Installing collected packages: Pillow, pystrich
Successfully installed Pillow-7.1.1 pystrich-0.8
Removing intermediate container f3a628535321
Step 4/4 : CMD [ "python", "./script.py" ]
 ---> Running in c94340b1c42b
Removing intermediate container c94340b1c42b
 ---> e0fd6b916c73
Successfully built e0fd6b916c73
Successfully tagged python-300108234:latest
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.
```
* Pour verifier que l'image est creer lancez cette commande:

```
> docker images
```
* Lancez la nouvelle image en entrant :

```
> docker run python-300108234
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
