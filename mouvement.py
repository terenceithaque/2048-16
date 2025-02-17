"mouvement.py gère les déplacements de nombres dans la grille"


# Liste des directions autorisées
directions_autorisees = ["haut", "bas", "gauche", "droite"]





    
    
def deplacer_nombres(direction:str, grille:list) -> list:
    "Déplace les nombres d'une grille dans une direction donnée. Renvoie la grille actualisée."
    # Gérer la direction "haut"
    if direction == "haut":
        # Parcourir la grille 
        for ligne in grille:
            pass

    # Gérer la direction "bas"    
    elif direction == "bas":
        # Parcourir les lignes de la grille
        for ligne in range(len(grille) -1):
            for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne actuelle
                # Si le nombre dans la case actuelle correspond à celui de la case dans la ligne suivante
                
                if grille[ligne][colonne] == grille[ligne+1][colonne]:
                    # Vider la case actuelle et multiplier le nombre de la ligne suivante par 2
                    grille[ligne][colonne] = 0
                    grille[ligne+1][colonne]*=2

                # ou que la valeur de la case dans la ligne suivante est égale à 0
                
                elif grille[ligne+1][colonne] == 0:
                    grille[ligne+1][colonne] = grille[ligne][colonne]
                    grille[ligne][colonne] = 0   

    
    elif direction == "gauche":
        pass
    
    elif direction == "droite":
        pass
    