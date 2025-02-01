
Noms : Terence le Thierry
Titre du projet : 2048-16
Présentation de l'objectif minimal : Un jeu de 2048 en solo, ligne de commande et avec des nombres en base 16.
Présentation des améliorations envisageables :  Une interface graphique avec tkinter ou pygame, des couleurs pour représenter les nombres.
Règles du jeu:
        Il faut déplacer des nombres définis dans une grille de manière à obtenir le nombre 2048 (en base 16)  ou un multiple de 2048 (4096, 8192, etc) dans une case.  Pour déplacer les nombres de la grille, il faut qu'il soit égal au nombre d'une case adjacente ou que la case adjacente soit VIDE. Si la grille est pleine avant d'avoir atteint l'objectif, alors LA PARTIE EST PERDUE.

Les fichiers utilisés par le jeu:

    main.py : contient la logique du jeu (boucle, variables, etc).

    Dans un dossier séparé:

    nombre.py : contient deux fonctions -> generer() et base16(). generer() renvoie un nombre au hasard (généralement 2 ou 4) et bas16() le convertit en hexadécimal SANS les caractères de début de la fonction hex().

    grille.py : ne contient, qu'une fonction -> generer(). generer() renvoie une liste de listes représentant la grille de jeu.

    mouvements:.py définit une liste des directions possibles, puis une fonction deplacer_nombres(). Cette fonction prend en paramètre une direction,  une grille sur laquelle opérer le déplacement. GENERE UNE ERREUR SI LA DIRECTION EST INVALIDE.