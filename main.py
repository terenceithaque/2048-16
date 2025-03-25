"main.py contient la logique du jeu"
# Importer les modules nécessaires au jeu
import random
import pygame
pygame.init()
import nombre
import grille
import mouvement as mov
import historique
import undo
import score
from tkinter import messagebox



def demander_quitter(titre="Quitter ?", message="Voulez-vous quitter ?") -> bool:
    "Demande au joueur s'il souhaite quitter le jeu par une boîte de dialogue avec les propriétés titre et message, renvoie un booléen."
    # Demander au joueur s'il souhaite quitter
    quitter = messagebox.askyesno(titre, message)

    # Renvoyer la réponse du joueur
    return quitter



def jeu():
    "Boucle principale du jeu"
    # Préparation du jeu et initialisation de la variable d'exécution
    fenetre = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("2048-16")
    grille_jeu = grille.Grille()
    score_joueur = score.Score(fenetre=fenetre)

    # Liste des objectifs à atteindre
    objectifs = [64, 64*2, 64*4, 64*8, 64*16]
    # Commencer le jeu avec l'objectif 2048
    objectif_actuel = objectifs[0]

    # Dictionnaire des objectifs et messages de victoire associés
    objectifs_messages = {
        objectifs[0]: ["C'est OK !", f" Vous avez atteint {objectifs[0]}. Améliorez-vous en visant {objectifs[1]}."],
        objectifs[1]: ["C'est mieux !", f"Vous avez atteint {objectifs[1]}. Vous avez encore une marge de progression en essayant {objectifs[2]}."],
        objectifs[2]: ["Un champion !", f"Vous êtes dans le haut du panier. Atteignez {objectifs[3]} pour acquérir un statut d'élite !"],
        objectifs[3]: ["L'élite !", f"Vous vous êtes hissé(e) dans le haut du haut du panier. Mais ne vous reposez pas sur vos lauriers, car il reste un ultime, objectif, le Saint-Graal que les joueurs veulent attendre. \n Releverez-vous ce défi sans commune mesure ?"],
        objectifs[4]: ["Le dieu du 2048 !!!!", "Vous avez triomphé de milles et une épreuves, tel un véritable descendant d'Hercule. Bienvenue chez les dieux du 2048 !"]
    }
    
    deplacement_nombres = pygame.USEREVENT + 1 # Evénement pour le déplacement des nombres
    pygame.time.set_timer(deplacement_nombres, 100) # L'événement de déplacement des nombres a lieu toutes les 100 millisecondes
    
    historique_jeu = historique.Historique() # Créer un historique pour mémoriser les derniers coups joués.
    historique_jeu.ajouter(grille_jeu.contenu) # Commencer l'historique avec la nouvelle grille de jeu
    execution = True
    # Tant que le jeu est en cours d'exécution, que la grille n'est pas pleine ou que des fusions sont toujours possibles
    while execution or not grille_jeu.est_pleine() and not any([grille_jeu.fusion_haut(), grille_jeu.fusion_bas(), grille_jeu.fusion_gauche(), grille_jeu.fusion_droite()]):
        #print("Valeur du score :", score_joueur.valeur)
        #print("Coordonnées (x, y)  de (2, 2) :", grille_jeu.coordonnees(2, 2, 145, 195, 5))
        fenetre.fill((255, 255, 255))
        # Obtenir les touches pressées par l'utilisateur
        touches = pygame.key.get_pressed()
        # Gérer les événements du jeu
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT: # Si le joueur veut arrêter de jouer
                # Lui demander de confirmer
                if demander_quitter():
                    # Arrêter l'exécution, quitter pygame et arrêter complètement la fonction
                    execution = False
                    pygame.quit()
                    return

            """if evenement.type == pygame.MOUSEMOTION:
                print(pygame.mouse.get_pos())"""

            if evenement.type == deplacement_nombres:       

                if touches[pygame.K_UP]: # Si la touche "flèche vers le haut est pressée"
                    #print("Déplacement vers le haut.")
                    mov.deplacer_nombres("haut", grille_jeu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    # Choisir une case vide au hasard où générer un nouveau nombre
                    if len(grille_jeu.cases_vides()) > 0:
                        pos_nouveau_nombre = random.choice(grille_jeu.cases_vides())
                        ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                        col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                        # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                        grille_jeu.contenu[ligne][col] = nombre.generer()
                    
                    print("Fusions possibles vers le haut :", grille_jeu.fusion_haut())

                    historique_jeu.ajouter(grille_jeu.contenu) # Mettre à jour l'historique
                    #print("Dernier état de la grille :", historique_jeu.etat_grille(len(historique_jeu.contenu)))
                    
                    points = historique_jeu.dernieres_additions()
                    score_joueur.actualiser(points)
                    score_joueur.sauvegarder()
                    
                if touches[pygame.K_DOWN]: # Si la touche "flèche vers le bas est pressée"
                    #print("Déplacement vers le bas.")
                    mov.deplacer_nombres("bas", grille_jeu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    # Générer un nouveau nombre dans une case vide
                    if len(grille_jeu.cases_vides()) > 0:
                        pos_nouveau_nombre = random.choice(grille_jeu.cases_vides()) # Choisir une case vide au hasard
                        ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                        col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                        # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                        grille_jeu.contenu[ligne][col] = nombre.generer()
                    #print("Fusions possibles vers le bas:", grille_jeu.fusion_bas())

                    historique_jeu.ajouter(grille_jeu.contenu) # Mettre à jour l'historique
                    #print("Dernier état de la grille :", historique_jeu.etat_grille(len(historique_jeu.contenu)))
                    
                    points = historique_jeu.dernieres_additions()
                    score_joueur.actualiser(points)
                    score_joueur.sauvegarder()
                if touches[pygame.K_LEFT]: # Si la touche "flèche vers la gauche est pressée"
                    #print("Déplacement vers la gauche.")
                    mov.deplacer_nombres("gauche", grille_jeu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    if len(grille_jeu.cases_vides()) > 0:
                        pos_nouveau_nombre = random.choice(grille_jeu.cases_vides()) # Choisir une case vide au hasard
                        ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                        col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                        # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                        grille_jeu.contenu[ligne][col] = nombre.generer()
                    #print("Fusions possibles vers le bas:", grille_jeu.fusion_bas())

                    historique_jeu.ajouter(grille_jeu.contenu) # Mettre à jour l'historique
                    #print("Dernier état de la grille :", historique_jeu.etat_grille(len(historique_jeu.contenu)))
                    points = historique_jeu.dernieres_additions()
                    score_joueur.actualiser(points)
                    score_joueur.sauvegarder()
                    
                    
                if touches[pygame.K_RIGHT]: # Si la touche "flèche vers la droite est pressée"
                    #print("Déplacement vers la droite.")
                    mov.deplacer_nombres("droite", grille_jeu)
                    print("Positions des cases vides :", grille_jeu.cases_vides())
                    if len(grille_jeu.cases_vides()) > 0:
                        pos_nouveau_nombre = random.choice(grille_jeu.cases_vides()) # Choisir une case vide au hasard
                        ligne = pos_nouveau_nombre[0] # Ligne où se situe la case libre choisie
                        col = pos_nouveau_nombre[1] # Colonne où se situe la case choisie
                        # Générer le nouveau nombre et le placer à la case libre choisie dans la grille
                        grille_jeu.contenu[ligne][col] = nombre.generer()
                    #print("Fusions possibles vers le bas:", grille_jeu.fusion_bas())

                    historique_jeu.ajouter(grille_jeu.contenu) # Mettre à jour l'historique
                    #print("Dernier état de la grille :", historique_jeu.etat_grille(len(historique_jeu.contenu)))
                    points = historique_jeu.dernieres_additions()
                    score_joueur.actualiser(points)
                    score_joueur.sauvegarder()

        # Si le joueur appuie sur contrôle gauche + Z
        if touches[pygame.K_LCTRL] and touches[pygame.K_z]:
            # Annuler la dernière action de jeu
            print("Annulation de la dernière action de jeu...")
            grille_jeu.contenu = undo.defaire(grille_jeu.contenu, historique_jeu)

        # ou sur contrôle droite + Z
        elif touches[pygame.K_RCTRL] and touches[pygame.K_z]:
            # Annuler la dernière action de jeu
            print("Annulation de la dernière action de jeu...")
            grille_jeu.contenu = undo.defaire(grille_jeu.contenu, historique_jeu)


        # Si le joueur appuie sur contrôle gauche + Y
        if touches[pygame.K_LCTRL] and touches[pygame.K_y]:
            # Refaire la dernière action annulée
            print("Restauration de la dernière action...")
            grille_jeu.contenu = undo.refaire(grille_jeu.contenu, historique_jeu)

        # ou sur contrôle droite + Y
        elif touches[pygame.K_RCTRL] and touches[pygame.K_y]:
            # Refaire la dernière action annulée
            print("Restauration de la dernière action...")
            grille_jeu.contenu = undo.refaire(grille_jeu.contenu, historique_jeu)            


        # Vérifier si l'objectif est atteint$
        if any(objectif_actuel in ligne for ligne in grille_jeu.contenu):
            if objectif_actuel != objectifs[len(objectifs) -1]:
                continuer = messagebox.askyesno(objectifs_messages[objectif_actuel][0], objectifs_messages[objectif_actuel][1])
                if continuer:
                    grille_jeu.sauvegarder()
                    objectif_actuel *= 2
                    continue
                else:
                    execution = False
                    return

            else:
                messagebox.showinfo("Victoire !", "Vous avez atteint tous les objectifs et gagné le jeu. Félicitations !")
                execution = False
                return    

        # Afficher la grille et mettre à jour l'affichage
        grille_jeu.dessiner(fenetre)
        score_joueur.afficher(20, 20)
        pygame.display.flip()  


    messagebox.showinfo("Partie terminée !", "La partie est terminée.")                  
        
        
# Lancer le jeu
jeu()
        
        


