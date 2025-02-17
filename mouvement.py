"mouvement.py gère les déplacements de nombres dans la grille"


# Liste des directions autorisées
directions_autorisees = ["haut", "bas", "gauche", "droite"]





    
    
def deplacer_nombres(direction:str, grille:list) -> list:
    "Déplace les nombres d'une grille dans une direction donnée. Renvoie la grille actualisée."
    # Gérer la direction "haut"
    if direction == "haut":
        # Parcourir la grille depuis le bas vers le haut 
        for ligne in range(len(grille) -1, -1, -1):
            # Parcourir chaque colonne de la grille
            for colonne in range(len(grille[ligne])):
                if ligne < len(grille) -1:
                    # Si le nombre dans la case actuelle correspond à celui de la case supérieure
                    if grille[ligne][colonne] == grille[ligne+1][colonne]:
                        grille[ligne][colonne] = 0 # Vider la case actuelle
                        grille[ligne+1][colonne]*= 2 # Multiplier le nombre dans la case supérieure par deux

                    # ou que le nombre de la case supérieure vaut zéro
                    elif grille[ligne+1][colonne] == 0: 
                        # Déplacer le nombre de la case actuelle vers la case supérieure
                        grille[ligne+1][colonne] = grille[ligne][colonne]
                        grille[ligne][colonne] = 0    
            

    # Gérer la direction "bas"    
    elif direction == "bas":
        # Parcourir les lignes de la grille
        for ligne in range(len(grille) -1):
            for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne actuelle
                # Si le nombre dans la case actuelle correspond à celui de la case inférieure
                
                if grille[ligne][colonne] == grille[ligne+1][colonne]:
                    # Vider la case actuelle et multiplier le nombre de la case inférieure par 2
                    grille[ligne][colonne] = 0
                    grille[ligne+1][colonne]*=2

                # ou que la valeur de la case dans la ligne suivante est égale à 0

                elif grille[ligne+1][colonne] == 0:
                    # Déplacer le nombre de la case actuelle vers la case inférieure
                    grille[ligne+1][colonne] = grille[ligne][colonne]
                    grille[ligne][colonne] = 0   

    
    elif direction == "gauche":
        pass
    
    elif direction == "droite":
        pass
    