🎡

# 👇 Mon projet 👇

## jeu: "pierre-feuille-ciseaux"

### 🎈Vue generale du jeu:
```
Le jeu de Pierre-Feuille-Ciseaux est jeu de mains où chaque joueur choisit simultanément un élément
parmis pierre, feuille et ciseaux. Le vainqueur est décidé selon les principes suivants : la pierre émousse les
ciseaux, les ciseaux coupent la feuille, la feuille enveloppe la pierre.
```

### 🔐L’objectif de ce code
```
Programmer un jeu de Pierre-Feuille-Ciseaux dont les deux joueurs sont l’ordinateur et l’utilisateur. Une partie se jouera en une succession de manches de "5" et le programme maintiendra une fiche de score afin de déterminer le vainqueur à la fin
```

### 🧨règles du jeu:

```
la feuille couvre la pierre
➡vous gagnez ✔
```
```
la pierre casse les ciseaux
➡vous gagnez ✔
```
```
les ciseaux coupe le papier
➡vous perdez ❌
```
```
pierre vs pierre ou ciseaux vs ciseaux ou papier vs papier
➡égalite
```
### ♻Comment se fonctione le code ⁉

#### Un appel de tirage retourne une chaîne de caractères contenant aléatoirement "Pierre","Feuille" ou "Ciseaux" avec l'enoncé du jeu! le choix –Aléatoire– de l’ordinateur

sous forme de:
```
Pierre-papier-ciseaux. Le premier Ã  5 a gagné !
```
#### Un appel de coupJoueur demande à l’utilisateur de choisir entre Pierre, Feuille et Ciseaux

```
1 : pierre, 2 : papier, 3 : ciseaux ? 

```
##### ⚠ Rappel : La fonction randrange(a, b) (du module random) retourne aléatoirement un entier n compris entre les paramètres a et b : a <= n < b

##### exemple:
```

1 : pierre, 2 : papier, 3 : ciseaux ? 
➡ 1
Vous montrez pierre - Je montre ciseaux 
vous 1    moi 0

1 : pierre, 2 : papier, 3 : ciseaux ? 
➡ 2
Vous montrez papier - Je montre pierre 
vous 2    moi 0


1 : pierre, 2 : papier, 3 : ciseaux ? 
➡ 1
Vous montrez pierre - Je montre papier 
vous 2    moi 1


1 : pierre, 2 : papier, 3 : ciseaux ? 
➡ 1
Vous montrez pierre - Je montre ciseaux 
vous 3    moi 1


1 : pierre, 2 : papier, 3 : ciseaux ? 
➡ 2
Vous montrez papier - Je montre ciseaux 
vous 3    moi 2


1 : pierre, 2 : papier, 3 : ciseaux ? 
➡ 3
Vous montrez ciseaux - Je montre papier 
vous 5    moi 2

```

#### finalement le premier Ã " 5 "a gagné 🎉🎊




