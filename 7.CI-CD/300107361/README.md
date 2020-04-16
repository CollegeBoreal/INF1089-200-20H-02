## Bienvenue dans "Bonjour Monde" avec GitHub Actions

Ce cours te guidera à écrire ta première action et à l'utiler avec un fichier de flux de tâches `workflow`. 

**Prêt à démarrer? Dirige toi vers le premier problème.**

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

`$ docker build --tag b`:id:`:1.0 .`
```
$ docker build --tag b300107361:1.0 .
Sending build context to Docker daemon  7.168kB
Step 1/4 : FROM debian:9.5-slim
9.5-slim: Pulling from library/debian
f17d81b4b692: Already exists
Digest: sha256:ef6be890318a105f7401d0504c01c2888daa5d9e45b308cf0e45c7cb8e44634f
Status: Downloaded newer image for debian:9.5-slim
 ---> 4b4471f624dc
Step 2/4 : ADD entrypoint.sh /entrypoint.sh
 ---> 664d8eaf46e7
Step 3/4 : RUN chmod +x /entrypoint.sh
 ---> Running in bad911873d74
Removing intermediate container bad911873d74
 ---> 12b635826ce1
Step 4/4 : ENTRYPOINT ["/entrypoint.sh"]
 ---> Running in bb5aa6ea5c30
Removing intermediate container bb5aa6ea5c30
 ---> 73da3c454a8a
Successfully built 73da3c454a8a
Successfully tagged b300107361:1.0
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.
```

Pour visualiser les couches images de l'image créée

```
$ docker image history b300107361
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
1c2df9f0e1cd        41 hours ago        /bin/sh -c #(nop)  ENTRYPOINT ["/entrypoint.…   0B
eee9174f3eaf        41 hours ago        /bin/sh -c chmod +x /entrypoint.sh              79B
ee5155eaf6da        41 hours ago        /bin/sh -c #(nop) ADD file:c63a97c860b6e940d…   79B
4b4471f624dc        18 months ago       /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>           18 months ago       /bin/sh -c #(nop) ADD file:f8f26d117bc4a9289…   55.3MB

```

