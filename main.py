"main.py contient la logique du jeu"
# Importer les modules nécessaires au jeu
import nombre
import grille
import mouvement as mov





def jeu():
    "Boucle principale du jeu"
    # Préparation du jeu et initialisation de la variable d'exécution
    grille_jeu = grille.generer()
    grille_jeu[0][0] = nombre.generer()
    score_joueur = 0
    
    execution = True
    while execution:
        # Demander dans quelle direction déplacer les nombres
        entree = mov.entree("Entrer une direction (haut, bas, droite ou gauche) ou une commande:")
        
        
# Lancer le jeu
jeu()
        
        


