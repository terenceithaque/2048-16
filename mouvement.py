"mouvement.py gère les déplacements de nombres dans la grille"


# Liste des directions autorisées
directions_autorisees = ["haut", "bas", "gauche", "droite"]
# Entrées spéciales qui ne sont pas des directions mais agissent sur le jeu.
# Par exemple "q" pour quitter
entrees_speciales = ["q"]



def entree(message="Choisir une direction") -> str:
    "Demande une direction ou une entrée à l'utilisateur, et recommence tant qu'elle est invalide."
    # Demander la direction de déplacement des nombres ou l'entrée au joueur
    entree = input(message)
    
    # Redemander tant que la direction fournie est invalide ou que l'entrée fournie est invalide.
    while entree.lower() not in directions_autorisees and not entree in entrees_speciales:
        print("Direction ou entrée invalide.")
        entree = input(message)
    
    return entree
    
    
def deplacer_nombres(direction:str, grille:list) -> list:
    "Déplace les nombres d'une grille dans une direction donnée. Renvoie la grille actualisée."
    # Gérer la direction "haut"
    if direction == "haut":
        # Parcourir la grille 
        for ligne in grille:
            pass
        
    elif direction == "bas":
        pass
    
    elif direction == "gauche":
        pass
    
    elif direction == "droite":
        pass
    