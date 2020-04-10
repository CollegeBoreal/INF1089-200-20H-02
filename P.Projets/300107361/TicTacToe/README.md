
# Projet Python - Étapes pour construire un jeu Python

Il ne fait aucun doute que vous devez avoir joué au Tic Tac Toe a l'ecole et chacun de nous aime jouer au jeu. 
Vous serez surpris de savoir que le jeu de Tic Tac Toe existe depuis les temps de l'Égypte antique.

Avec ce projet Python de [Toch90](https://github.com/toch90), nous allons construire un jeu interactif de Tic Tac Toe où nous apprendrons de nouvelles choses en cours de route.

## Qu'est-ce que Tic Tac Toe?

Tic Tac Toe est l'un des jeux les plus joués et est le meilleur jeu tueur de temps auquel vous pouvez jouer n'importe où avec juste un stylo et du papier. 
Si vous ne savez pas comment jouer à ce jeu, ne vous inquiétez pas, laissez-nous d'abord comprendre cela.


Le jeu est joué par deux personnes. Tout d'abord, nous dessinons un tableau avec une grille carrée 3 × 3. 
Le premier joueur choisit «X» et le dessine sur l’une des grilles carrées, puis c’est la chance du deuxième joueur de dessiner «O» sur les cases disponibles. 

Comme cela, les joueurs dessinent alternativement «X» et «O» sur les espaces vides jusqu'à ce qu'un joueur réussisse à dessiner 3 marques consécutives soit horizontalement, verticalement ou diagonalement.

Ensuite, le joueur gagne la partie, sinon la partie est nulle lorsque toutes les places sont remplies.

![image](https://dkb46014en6d6.cloudfront.net/tutorials/wp-content/uploads/sites/2/2019/12/tic-tac-toe-project-in-python.gif)

## Tic Tac Toe - À propos du projet Python

L'intéressant projet Python sera construit en utilisant la bibliothèque pygame. 
Nous expliquerons toutes les méthodes d'objet pygame utilisées dans ce projet.

Pygame est une excellente bibliothèque qui nous permettra de créer la fenêtre et de dessiner des images et des formes sur la fenêtre. 
De cette façon, nous capturerons les coordonnées de la souris et identifierons le bloc où nous devons marquer «X» ou «O». 

Ensuite, nous vérifierons si l'utilisateur gagne le jeu ou non.

## Prerequis
Pour implémenter ce jeu, nous utiliserons les concepts de base de Python et Pygame qui est une bibliothèque Python pour construire des jeux multi-plateformes. 

Il contient les modules nécessaires aux graphiques informatiques et aux bibliothèques de sons. Pour installer la bibliothèque, vous pouvez utiliser le programme d'installation pip à partir de la ligne de commande:
```
pip install pygame
```

## Tout d'abord, vérifions les étapes pour construire le programme Tic Tac Toe en Python:

* Créez la fenêtre d'affichage de notre jeu.
* Dessinez la grille sur la toile où nous jouerons Tic Tac Toe.
* Tracez la barre d’état sous le canevas pour montrer quel est le tour du joueur et qui remporte la partie.
* Lorsque quelqu'un gagne la partie ou que la partie est nulle, nous réinitialisons la partie.

Nous devons exécuter notre jeu dans une boucle infinie. 
Il recherchera continuellement des événements et lorsqu'un utilisateur appuiera sur le bouton de la souris sur la grille, nous obtiendrons d'abord les coordonnées X et Y de la souris. 

Ensuite, nous vérifierons sur quel carré l'utilisateur a cliqué. 
Ensuite, nous dessinerons l'image appropriée «X» ou «O» sur la toile. C'est donc essentiellement ce que nous ferons dans cette idée de projet Python.

## 1. Initialisation des composants du jeu
Commençons donc par importer la bibliothèque pygame et la bibliothèque de temps car nous allons utiliser la méthode `time.sleep()` pour mettre le jeu en pause à certaines positions. 

Ensuite, nous initialisons toutes les variables globales que nous utiliserons dans notre jeu Tic Tac Toe.
```
import pygame as pg,sys
from pygame.locals import *
import time
#initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)
#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]
```
Ici, le TTT est la principale planche Tic Tac Toe 3 × 3 et, dans un premier temps, il aura 9 valeurs None. 
La hauteur et la largeur de la toile sur laquelle nous allons jouer est de 400 × 400.

## 3. Initialisation de la fenêtre Pygame

Nous utilisons le pygame pour créer une nouvelle fenêtre où nous jouerons à notre jeu Tic Tac Toe. 
Nous initialisons donc le pygame avec la méthode `pg.init()` et l'affichage de la fenêtre est défini avec une largeur de 400 et une hauteur de 500. 

Nous avons réservé un espace de 100 pixels pour afficher l'état du jeu.

Le `pg.display.set_mode()` initialise l'affichage et nous le référençons avec la variable screen. 
Cette variable d'écran sera utilisée chaque fois que nous voulons dessiner quelque chose sur l'écran.

La méthode `pg.display.set_caption` est utilisée pour définir un nom qui apparaîtra en haut de la fenêtre d'affichage.
```
#initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe")
```

## 3.Charger et transformer des images

Le projet d'apprentissage automatique Python utilise de nombreuses images comme l'image d'ouverture qui s'affichera au démarrage ou à la réinitialisation du jeu. 

Les images X et O que nous allons dessiner lorsque l'utilisateur clique sur la grille. 
Nous chargeons toutes les images et les redimensionnons afin qu'elles s'intègrent facilement dans notre fenêtre.
```
#loading the images
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')
#resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))
```

## 4.Définir les fonctions

Nous créons maintenant une fonction qui lancera le jeu. Nous utiliserons également cette fonction lorsque nous voulons redémarrer le jeu. 
Dans pygame, la fonction `blit()` est utilisée sur la surface pour dessiner une image au-dessus d'une autre image.

Nous dessinons donc l'image d'ouverture et après le dessin, nous devons toujours mettre à jour l'affichage avec `pg.display.update()`. 
Lorsque l'image d'ouverture est dessinée, nous attendons 1 seconde en utilisant `time.sleep(1)` et remplissons l'écran de couleur blanche.

Ensuite, nous dessinons 2 lignes verticales et horizontales sur le fond blanc pour faire la grille 3 × 3. 
Au final, on appelle la fonction `draw_status()`
```
def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()
```

La fonction `draw_status()` dessine un rectangle noir où nous mettons à jour le statut du jeu en indiquant le tour du joueur et si le jeu se termine ou se dessine.
```
def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
```

La fonction `check_win()` vérifie la carte Tic Tac Toe pour voir toutes les marques de «X» et «O». 
Il calcule si un joueur a gagné le jeu ou non. 

Ils peuvent soit gagner lorsque le joueur a marqué 3 marques consécutives dans une rangée, une colonne ou en diagonale. 
Cette fonction est appelée à chaque fois que nous dessinons une marque «X» ou «O» sur la carte.
```
def check_win():
    global TTT, winner,draw
    # check for winning rows
    for row in range (0,3):
        if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and(TTT [row][0] is not None)):
            # this row won
            winner = TTT[row][0]
            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                              (width, (row + 1)*height/3 - height/6 ), 4)
            break
    # check for winning columns
    for col in range (0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
            # this column won
            winner = TTT[0][col]
            #draw winning line
            pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\
                          ((col + 1)* width/3 - width/6, height), 4)
            break
    # check for diagonal winners
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        # game won diagonally left to right
        winner = TTT[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        # game won diagonally right to left
        winner = TTT[0][2]
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)
    if(all([all(row) for row in TTT]) and winner is None ):
        draw = True
    draw_status()
```

La fonction `drawXO(ligne, col)` prend la ligne et la colonne où la souris est cliquée, puis elle trace la marque «X» ou «O». 

Nous calculons les coordonnées x et y du point de départ à partir desquelles nous allons dessiner l'image png de la marque.
```
def drawXO(row,col):
    global TTT,XO
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30
    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
TTT[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img,(posy,posx))
XO= 'o'
else:
        screen.blit(o_img,(posy,posx))
        XO= 'x'
    pg.display.update()
    #print(posx,posy)
    #print(TTT)
```

La fonction `userClick()` est déclenchée chaque fois que l'utilisateur appuie sur le bouton de la souris.

Lorsque l’utilisateur clique sur la souris, nous prenons d’abord les coordonnées x et y de l’endroit où la souris est cliquée dans la fenêtre d’affichage, puis si cet endroit n’est pas occupé, nous dessinons le ‘XO’ sur la toile.

Nous vérifions également si le joueur gagne ou non après avoir tiré "XO" sur le plateau.
```
def userClick():
    #get coordinates of mouse click
    x,y = pg.mouse.get_pos()
    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)
    if(row and col and TTT[row-1][col-1] is None):
        global XO
        #draw the x or o on screen
        drawXO(row,col)
        check_win()
```


La dernière fonction est le `reset_game()`. 
Cela redémarrera le jeu et nous réinitialiserons également toutes les variables au début du jeu.
```
def reset_game():
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner=None
    TTT = [[None]*3,[None]*3,[None]*3]
```

## 5.Exécutez le jeu pour toujours

Pour démarrer le jeu, nous appellerons la fonction `game_opening()`. 

Ensuite, nous exécutons une boucle infinie et vérifions en permanence tout événement créé par l'utilisateur. 
Si l'utilisateur appuie sur le bouton de la souris, l'événement MOUSEBUTTONDOWN sera capturé, puis nous déclencherons la fonction `userClick()`. 

Ensuite, si l'utilisateur gagne ou que le jeu tire, nous réinitialisons le jeu en appelant la fonction `reset_game()`. 
Nous mettons à jour l'affichage à chaque itération et nous avons défini les images par seconde à 30.
```
game_opening()
# run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
```
Le jeu est terminé et prêt à jouer. Enregistrez le fichier du code source avec le nom de fichier [b300107361.py](https://github.com/CollegeBoreal/INF1089-200-20H-02/blob/master/P.Projets/300107361/TicTacToe/b300107361.py) et exécutez le fichier.

## LE `DEMO:`

![image](https://dkb46014en6d6.cloudfront.net/tutorials/wp-content/uploads/sites/2/2019/12/tic-tac-toe-project-in-python.gif)

![image](https://dkb46014en6d6.cloudfront.net/tutorials/wp-content/uploads/sites/2/2019/12/tic-tac-toe-starting-in-python-project-with-source-code.png)

![image](https://dkb46014en6d6.cloudfront.net/tutorials/wp-content/uploads/sites/2/2019/12/tic-tac-toe-game-in-python-project-idea.png)



## Résumé

Avec ce projet en Python, nous avons réussi à créer le jeu Tic Tac Toe. Nous avons utilisé la bibliothèque pygame populaire pour le rendu des graphiques sur une fenêtre d'affichage. 

Nous avons appris à capturer des événements à partir du clavier ou de la souris et à déclencher une fonction lorsque le bouton de la souris est enfoncé. 

De cette façon, nous pouvons calculer la position de la souris, dessiner X ou O sur l'écran et vérifier si le joueur gagne la partie ou non. J'espère que vous avez apprécié la construction du jeu.


Author: @[Toch90](https://github.com/toch90)
