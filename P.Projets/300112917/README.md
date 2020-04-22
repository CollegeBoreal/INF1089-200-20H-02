
# Projet Python - le jeu: deviner le mot
:snake:

## Le But du JEU?

Dans ce jeu, il y a une liste de mots présents, parmi lesquels notre interprète choisira 1 mot au hasard. L'utilisateur doit d'abord saisir son nom, puis il lui sera demandé de deviner n'importe quel alphabet. Si le mot aléatoire contient cet alphabet, il sera affiché comme sortie (avec un placement correct) sinon le programme vous demandera de deviner un autre alphabet. L'utilisateur aura 12 tours (peut être modifié en conséquence) pour deviner le mot complet.

## Choisissons la Bibliotheque d'import

```
import random
```
Bibliothèque que nous utilisons pour choisir des mots aléatoires à partir d'une liste de mots. 

## Ajoutons

```
name = input("Quel est ton nom? ")
```
Ici, l'utilisateur est invité à saisir le nom en premier.

## Apres nous ajoutons la liste

```
print("Bonne Chance ! ", name) 

words = ['rainbow', 'ordinateur', 'science', 'programmation', 
		'python', 'mathematiques', 'joueur', 'condition', 
		'reverse', 'eau', 'planche', 'geeks']
```
La fonction choisira un mot au hasard dans cette liste de mots

## Ajoutons la fonction

```
word = random.choice(words) 
```
La fonction choisira un mot au hasard dans cette liste de mots

## Ajoutons le nombre des tours

```
print("Devinez les lettres") 

guesses = '' 

turns = 12
```
N'importe quel nombre de tours peut être utilisé ici, mais nous choisissons 12

## Le nombre d'echec

```
while turns > 0: 
       
    failed = 0
```
compte le nombre de fois où un utilisateur échoue

## Ajoutons

```
    for char in word:  
          
       if char in guesses:  
            print(char) 
```
Tous les caractères du mot d'entrée en prenant un à la fois.comparer ce personnage avec le personnage dans "in guesses"

## Ajoutons aussi

```
else:  
            print("_") 
              
            failed += 1
```
Pour chaque échec 1 sera incrémenté en échec

## Si le joueur echoue ou gagne

```
if failed == 0: 
		  print("Tu gagnes") 
		
		  print("Le mot est: ", word) 
		  break
```
l'utilisateur gagnera le jeu si l'échec est 0 et "You Win" sera donné en sortie

##  Final

```
	guess = input("Devinez un lettre:") 
	
	guesses += guess 
	
	if guess not in word: 
		
		   turns -= 1
		
		   print("Faux") 
		

		   print("Tu as", + turns, 'more guesses') 
		
		
		   if turns == 0: 
			      print("Perdant") 

```
si l'utilisateur a entré le mauvais alphabet, il lui demandera d'entrer un autre alphabet. Chaque caractère saisi sera stocké "in guesses". Vérifiez l'entrée avec le caractère dans le mot. Si le caractère ne correspond pas au mot, «Wrong» sera donné en sortie. Cela imprimera le nombre de tours restants pour l'utilisateur

##  Resultat Final

```
import random 

name = input("Quel est ton nom? ") 

print("Bonne Chance ! ", name) 

words = ['rainbow', 'ordinateur', 'science', 'programmation', 
		'python', 'mathematiques', 'joueur', 'condition', 
		'reverse', 'eau', 'planche', 'geeks'] 

word = random.choice(words) 


print("Devinez les lettres") 

guesses = '' 

turns = 12


while turns > 0: 
	
	failed = 0
	
	for char in word: 
		
		if char in guesses: 
			print(char) 
			
		else: 
			print("_") 
			
			failed += 1
			

	if failed == 0: 
		print("Tu gagnes") 
		
		print("Le mot est: ", word) 
		break
	
	guess = input("Devinez un lettre:") 
	
	guesses += guess 
	
	if guess not in word: 
		
		turns -= 1
		
		print("Faux") 
		

		print("Tu as", + turns, 'more guesses') 
		
		
		if turns == 0: 
			print("Perdant") 

```
