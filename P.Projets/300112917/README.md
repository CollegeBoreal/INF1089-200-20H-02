
# Projet Python - Simple fonction
:snake:

## Qu'est-ce que PYTHON MAIN FUNCTION?

Comme Python est un langage interprété, il suit une approche descendante. 
Juste parce que python est interprété, il n'y a pas de point d'entrée statique vers le programme et le code source est exécuté séquentiellement et il n'appelle aucune méthode à moins que vous ne l'appeliez manuellement.

## Tic Tac Toe - À propos du projet Python

```
print(“Good Morning”)
 
def main():
          print(“Hello Python”)
 
print(“Good Evening”)
Output:

Good Morning
Good Evening
```
Si nous observons le programme ci-dessus, il n'a imprimé que 'Good Morning' et 'Good Evening' et il n'a pas imprimé le terme 'Hello Python' parce que nous ne l'avons pas appelé manuellement ou nous n'avons pas utilisé le principal de python fonctionner ici.
Pygame est une excellente bibliothèque qui nous permettra de créer la fenêtre et de dessiner des images et des formes sur la fenêtre. 

## Ajoutons la fonction MAIN
Voyons maintenant le programme avec l'appel de fonction si __name__ == "__main__".

```
print(“Good Morning”)
 
def main():
          print(“Hello Python”)
 
print(“Good Evening”)
 
if __name__ == “__main__”:
         main()
```

## Resultat

```
print(“Good Morning”)
 
def main():
          print(“Hello Python”)
 
print(“Good Evening”)
 
if __name__ == “__main__”:
         main()
Output:

Good Morning
Good Evening
Hello Python

```
Si vous observez le programme ci-dessus, vous pouvez avoir une question - pourquoi Bonjour Python est imprimé? 
C'est parce que nous appelons la fonction principale à la fin du code, donc elle affiche «Good Morning» en premier, «Good Evening» ensuite et «Hello Python» à la fin.
