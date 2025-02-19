"mouvement.py gère les déplacements de nombres dans la grille"
import grille

# Liste des directions autorisées
directions_autorisees = ["haut", "bas", "gauche", "droite"]





    
    
def deplacer_nombres(direction:str, grille:grille.Grille) -> list:
    "Déplace les nombres d'une grille dans une direction donnée. Renvoie la grille actualisée."
    # Gérer la direction "haut"
    
    if direction == "haut":
        # Parcourir la grille depuis le bas vers le haut 
        for ligne in range(len(grille.contenu) -1, -1, -1):
            # Parcourir chaque colonne de la grille
            print("Ligne :", grille.contenu[ligne])
            for colonne in range(len(grille.contenu[ligne])):
                if ligne < len(grille.contenu) -1:
                    print("Ligne :", ligne)
                    # Si le nombre dans la case actuelle correspond à celui de la case supérieure
                    if grille.contenu[ligne-1][colonne] == grille.contenu[ligne][colonne]:
                        grille.contenu[ligne][colonne]*=2 # Multiplier le nombre dans la case supérieure par deux
                        grille.contenu[ligne-1][colonne] = 0 # Vider la case actuelle
                        #break

                    # ou que le nombre de la case supérieure vaut zéro
                    elif grille.contenu[ligne-1][colonne] == 0: 
                        # Déplacer le nombre de la case actuelle vers la case supérieure
                        grille.contenu[ligne-1][colonne] = grille.contenu[ligne][colonne]
                        grille.contenu[ligne][colonne] = 0
                        #break    
            

    # Gérer la direction "bas"    
    elif direction == "bas":
        # Parcourir les lignes de la grille
        for ligne in range(len(grille.contenu) -1):
            for colonne in range(len(grille.contenu[ligne])): # Pour chaque colonne de la ligne actuelle
                # Si le nombre dans la case actuelle correspond à celui de la case inférieure
                
                if grille.contenu[ligne][colonne] == grille.contenu[ligne+1][colonne]:
                    # Vider la case actuelle et multiplier le nombre de la case inférieure par 2
                    grille.contenu[ligne][colonne] = 0
                    grille.contenu[ligne+1][colonne]*=2
                    #break

                # ou que la valeur de la case dans la ligne suivante est égale à 0

                elif grille.contenu[ligne+1][colonne] == 0:
                    # Déplacer le nombre de la case actuelle vers la case inférieure
                    grille.contenu[ligne+1][colonne] = grille.contenu[ligne][colonne]
                    grille.contenu[ligne][colonne] = 0
                    #break   

    # Gérer la direction "gauche"
    elif direction == "gauche":
        # Parcourir chaque ligne de la grille
        for ligne in range(len(grille.contenu)):
            # Parcourir toutes les colonnes à partir de la 2ème position
            for colonne in range(1, len(grille.contenu)):
                # Si le nombre de la case actuelle correpond à celui de la case à gauche
                if grille.contenu[ligne][colonne] == grille.contenu[ligne][colonne-1]:
                    # Fusionner les deux cases et vider l'actuelle
                    grille.contenu[ligne][colonne-1]*=2
                    grille.contenu[ligne][colonne] = 0

                # Si la case à gauche est vide
                elif grille.contenu[ligne][colonne-1] == 0:
                    # Déplacer le nombre de la case actuelle vers la gauche
                    grille.contenu[ligne][colonne-1] = grille.contenu[ligne][colonne]
                    grille.contenu[ligne][colonne] = 0    
    
    # Gérer la direction "droite"
    elif direction == "droite":
        # Parcourir toutes les lignes
        for ligne in range(len(grille.contenu)):
            for colonne in range(len(grille.contenu[ligne]) -1):
                # Si le nombre de la case actuelle correpond à celui de la case juste à droite
                if grille.contenu[ligne][colonne] == grille.contenu[ligne][colonne+1]:
                    # Fusionner les deux cases et vider l'actuelle
                    grille.contenu[ligne][colonne+1]*=2
                    grille.contenu[ligne][colonne] = 0

                # Si la case à droite est vide
                elif grille.contenu[ligne][colonne+1] == 0:
                    # Déplacer le nombre de la case actuelle vers la suivante
                    grille.contenu[ligne][colonne+1] = grille.contenu[ligne][colonne]
                    grille.contenu[ligne][colonne] = 0    
        
    