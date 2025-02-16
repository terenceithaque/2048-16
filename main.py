"main.py contient la logique du jeu"
# Importer les modules nécessaires au jeu
import pygame
pygame.init()
import nombre
import grille
import mouvement as mov





def jeu():
    "Boucle principale du jeu"
    # Préparation du jeu et initialisation de la variable d'exécution
    fenetre = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("2048-16")
    grille_jeu = grille.generer()
    grille_jeu[0][0] = nombre.generer()
    score_joueur = 0
    
    execution = True
    while execution:
        # Demander dans quelle direction déplacer les nombres
        entree = mov.entree("Entrer une direction (haut, bas, droite ou gauche) ou une commande:")
        
        
# Lancer le jeu
jeu()
        
        


