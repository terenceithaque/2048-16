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
    score_joueur = 0
    deplacement_nombres = pygame.USEREVENT + 1 # Evénement pour le déplacement des nombres
    pygame.time.set_timer(deplacement_nombres, 100) # L'événement de déplacement des nombres a lieu toutes les 100 millisecondes
    
    execution = True
    while execution:

        #print("Coordonnées (x, y)  de (2, 2) :", grille_jeu.coordonnees(2, 2, 145, 195, 5))
        fenetre.fill((255, 255, 255))
        # Obtenir les touches pressées par l'utilisateur
        touches = pygame.key.get_pressed()
        # Gérer les événements du jeu
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT: # Si le joueur veut arrêter de jouer
                execution = False # Arrêter l'exécution

            """if evenement.type == pygame.MOUSEMOTION:
                print(pygame.mouse.get_pos())"""

            if evenement.type == deplacement_nombres:       

                if touches[pygame.K_UP]: # Si la touche "flèche vers le haut est pressée"
                    print("Déplacement vers le haut.")
                    mov.deplacer_nombres("haut", grille_jeu.contenu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())

                if touches[pygame.K_DOWN]: # Si la touche "flèche vers le bas est pressée"
                    print("Déplacement vers le bas.")
                    mov.deplacer_nombres("bas", grille_jeu.contenu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())

                if touches[pygame.K_LEFT]: # Si la touche "flèche vers la gauche est pressée"
                    print("Déplacement vers la gauche.")
                    mov.deplacer_nombres("gauche", grille_jeu.contenu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())

                if touches[pygame.K_RIGHT]: # Si la touche "flèche vers la droite est pressée"
                    print("Déplacement vers la droite.")
                    mov.deplacer_nombres("droite", grille_jeu.contenu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())


           



        # Afficher la grille et mettre à jour l'affichage
        grille_jeu.dessiner(fenetre)
        pygame.display.flip()                 
        
        
# Lancer le jeu
jeu()
        
        


