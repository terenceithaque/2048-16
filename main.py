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
    grille_jeu = grille.Grille()
    grille_jeu.contenu[0][0] = nombre.generer()
    score_joueur = 0
    
    execution = True
    while execution:
        # Obtenir les touches pressées par l'utilisateur
        touches = pygame.key.get_pressed()
        # Gérer les événements du jeu
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT: # Si le joueur veut arrêter de jouer
                execution = False # Arrêter l'exécution

        
        if touches[pygame.K_UP]: # Si la touche "flèche vers le haut est pressée"
            print("Déplacement vers le haut.")

        if touches[pygame.K_DOWN]: # Si la touche "flèche vers le bas est pressée"
            print("Déplacement vers le bas.")

        if touches[pygame.K_LEFT]: # Si la touche "flèche vers la gauche est pressée"
            print("Déplacement vers la gauche.")

        if touches[pygame.K_RIGHT]: # Si la touche "flèche vers la droite est pressée"
            print("Déplacement vers la droite.")              
        
        
# Lancer le jeu
jeu()
        
        


