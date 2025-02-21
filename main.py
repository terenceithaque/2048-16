"main.py contient la logique du jeu"
# Importer les modules nécessaires au jeu
import random
import pygame
pygame.init()
import nombre
import grille
import mouvement as mov
from tkinter import messagebox





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
    # Tant que le jeu est en cours d'exécution, que la grille n'est pas pleine ou que des fusions sont toujours possibles
    while execution and not grille_jeu.est_pleine() or any([grille_jeu.fusion_haut(), grille_jeu.fusion_bas(), grille_jeu.fusion_gauche(), grille_jeu.fusion_droite()]):

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
                    mov.deplacer_nombres("haut", grille_jeu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    # Choisir une case vide au hasard où générer un nouveau nombre
                    pos_nouveau_nombre = random.choice(grille_jeu.cases_vides())
                    ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                    col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                    # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                    grille_jeu.contenu[ligne][col] = nombre.generer()
                    print("Fusions possibles vers le haut :", grille_jeu.fusion_haut())


                if touches[pygame.K_DOWN]: # Si la touche "flèche vers le bas est pressée"
                    print("Déplacement vers le bas.")
                    mov.deplacer_nombres("bas", grille_jeu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    pos_nouveau_nombre = random.choice(grille_jeu.cases_vides())
                    ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                    col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                    # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                    grille_jeu.contenu[ligne][col] = nombre.generer()
                    print("Fusions possibles vers le bas:", grille_jeu.fusion_bas())

                if touches[pygame.K_LEFT]: # Si la touche "flèche vers la gauche est pressée"
                    print("Déplacement vers la gauche.")
                    mov.deplacer_nombres("gauche", grille_jeu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    pos_nouveau_nombre = random.choice(grille_jeu.cases_vides())
                    ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                    col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                    # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                    grille_jeu.contenu[ligne][col] = nombre.generer()
                    print("Fusions possibles vers la gauche:", grille_jeu.fusion_gauche())

                if touches[pygame.K_RIGHT]: # Si la touche "flèche vers la droite est pressée"
                    print("Déplacement vers la droite.")
                    mov.deplacer_nombres("droite", grille_jeu)
                    print("Grille de jeu:", grille_jeu.contenu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    pos_nouveau_nombre = random.choice(grille_jeu.cases_vides())
                    ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                    col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                    # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                    grille_jeu.contenu[ligne][col] = nombre.generer()
                    print("Fusions possibles vers la droite :", grille_jeu.fusion_droite())


           



        # Afficher la grille et mettre à jour l'affichage
        grille_jeu.dessiner(fenetre)
        pygame.display.flip()  


    messagebox.showinfo("Partie terminée !", "La partie est terminée.")                  
        
        
# Lancer le jeu
jeu()
        
        


