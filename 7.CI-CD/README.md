# :seven: CI/CD Batch


https://www.linkedin.com/learning/docker-essential-training-3-image-creation-management-and-registry/analyzing-a-dockerfile

## :a: :id:

* Créer un répertoire avec votre :id:

* Créer votre script PowerShell en donnant le nom b:id:.ps1

Example b300098957.ps1

[Participation](Participation.md)

## :b: Laboratoire

:one: Écrire les scripts en suivant le laboratoire ci-dessous dans [Github Leaning Lab](https://lab.github.com/CollegeBoreal):

https://lab.github.com/CollegeBoreal/lab-github-actions:-bonjour-monde


:two: Copier votre scripts dans le cours en remplaçant :id: par votre :id: github :octocat: :

https://github.com/:id:/lab-github-actions:-bonjour-monde

- [ ] Copier les scripts:

Par example:

  - [ ] Copier le fichier `Dockerfile` dans votre :id: `Boréal` 

  - [ ] Copier le fichier `entrypoint.sh` dans votre :id: `Boréal` 


- [ ] Créer votre fichier README.md


En un mot, récupérer le travail que vous avez fait à travers [Github Leaning Lab](https://lab.github.com/CollegeBoreal) et le mettre dans celui du cours [7.CI-CD](../7.CI-CD)

:three: Amélioration

Le laboratoire vous garantit une note de passage, ajouter du code en améliorant le script embellira la note.

et les autres fichier utiles quand on execute la commande :

`$ docker build --tag b`:id:`:1.0 .`

`$ docker run --tty --env INPUT_MY_NAME="Draman" b`:id:`:1.0`

`Hello world my name is Draman`

`% docker image history b`:id:`:1.0`
```
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
a555cf89a1b7        40 seconds ago      /bin/sh -c #(nop)  ENTRYPOINT ["/entrypoint.…   0B                  
4bb76bfb1e74        40 seconds ago      /bin/sh -c chmod +x /entrypoint.sh              65B                 
c010b45de5b3        40 seconds ago      /bin/sh -c #(nop) ADD file:44be7c7e599db7b1d…   65B                 
4e5021d210f6        2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           2 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           2 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   745B                
<missing>           2 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     987kB               
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:594fa35cf803361e6…   63.2MB   
```

# :fire: Indices 

:round_pushpin: Tu auras besoin de créer une branche avec `git`

https://github.com/CollegeBoreal/Tutoriels/tree/master/0.GIT/.branch

:round_pushpin: Tu auras également besoin de créer une demande d'extraction `pull request`

https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request

:round_pushpin: Répertoire Imbriqué

pour créer un répertoire imbriqué par exemple `.github/workflows` utilise la commande suivante avec le parametre `-p`:

```
$ mkdir -p .github/workflows
```
