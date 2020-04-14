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

:three: Amélioration

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
