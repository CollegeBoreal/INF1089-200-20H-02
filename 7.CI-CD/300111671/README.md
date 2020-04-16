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


- [ ] Modifie ton fichier README.md pour plus de documentation


En un mot, récupérer le travail que vous avez fait à travers [Github Leaning Lab](https://lab.github.com/CollegeBoreal) et le mettre dans celui du cours [7.CI-CD](../7.CI-CD)

:three: Amélioration

Le laboratoire vous garantit une note de :five::zero:`%`, ajouter du code en améliorant les scripts embellira la note.

En rappel, pour éxécuter localement son fichier `Dockerfile`, on execute la commande :

```
$ docker build --tag b300111671:1.0 .
Sending build context to Docker daemon   7.68kB
Step 1/12 : FROM debian:9.5-slim
9.5-slim: Pulling from library/debian
f17d81b4b692: Pull complete                                                                                             Digest: sha256:ef6be890318a105f7401d0504c01c2888daa5d9e45b308cf0e45c7cb8e44634f
Status: Downloaded newer image for debian:9.5-slim
 ---> 4b4471f624dc
Step 2/12 : COPY . /app
 ---> 17736b121a88
Step 3/12 : RUN apt-get update
 ---> Running in 7e9a7c8601de
Get:1 http://security.debian.org/debian-security stretch/updates InRelease [94.3 kB]
Ign:2 http://deb.debian.org/debian stretch InRelease
Get:3 http://deb.debian.org/debian stretch-updates InRelease [91.0 kB]
Get:4 http://deb.debian.org/debian stretch Release [118 kB]
Get:5 http://deb.debian.org/debian stretch Release.gpg [2410 B]
Get:6 http://security.debian.org/debian-security stretch/updates/main amd64 Packages [521 kB]
Get:7 http://deb.debian.org/debian stretch-updates/main amd64 Packages [27.9 kB]
Get:8 http://deb.debian.org/debian stretch/main amd64 Packages [7083 kB]
# trop long voila pourquoi j'ai couper
 ---> fc2fff8e7ba0
Step 9/12 : WORKDIR /app
 ---> Running in 2c81dead56c3
Removing intermediate container 2c81dead56c3
 ---> 283e43b26fc4
Step 10/12 : ADD entrypoint.sh /entrypoint.sh
 ---> 011a2f0846b1
Step 11/12 : RUN chmod +x /entrypoint.sh
 ---> Running in 0802bd09fea1
Removing intermediate container 0802bd09fea1
 ---> 80c6d94020d8
Step 12/12 : ENTRYPOINT ["/entrypoint.sh"]
 ---> Running in f916b32a2add
Removing intermediate container f916b32a2add
 ---> 35be52eb8f5c
Successfully built 35be52eb8f5c
Successfully tagged b300111671:1.0
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.

```
`$ docker run --tty --env INPUT_MON_NOM="Draman" b`:id:`:1.0`

`Bonjour tout le monde mon nom est Draman`

Pour visualiser les couches images de l'image créée


```
  docker image history b300111671:1.0
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
35be52eb8f5c        11 minutes ago      /bin/sh -c #(nop)  ENTRYPOINT ["/entrypoint.…   0B
80c6d94020d8        11 minutes ago      /bin/sh -c chmod +x /entrypoint.sh              79B
011a2f0846b1        11 minutes ago      /bin/sh -c #(nop) ADD file:c63a97c860b6e940d…   79B
283e43b26fc4        11 minutes ago      /bin/sh -c #(nop) WORKDIR /app                  0B
fc2fff8e7ba0        11 minutes ago      /bin/sh -c #(nop)  EXPOSE 5000                  0B
6683a810102a        11 minutes ago      /bin/sh -c #(nop)  CMD ["entry.py"]             0B
aad510f03cf9        11 minutes ago      /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "pyth…   0B
7d8330faa516        11 minutes ago      /bin/sh -c apt-get install -y python python-…   327MB
42736a536423        15 minutes ago      /bin/sh -c apt-get upgrade -y                   28.4MB
f168a04a46a0        16 minutes ago      /bin/sh -c apt-get update                       16.4MB
17736b121a88        17 minutes ago      /bin/sh -c #(nop) COPY dir:2163cf50b8f146005…   4.24kB
4b4471f624dc        18 months ago       /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>           18 months ago       /bin/sh -c #(nop) ADD file:f8f26d117bc4a9289…   55.3MB

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
