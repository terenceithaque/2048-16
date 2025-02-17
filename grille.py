"grille.py permet de générer une grille de jeu."
from turtle import color
import pygame
import nombre
import random


class Grille:
    "Grille de jeu"
    def __init__(self, taille=4):
        "Constructeur de la grille"
        self.contenu = self.generer(0) # Générer le contenu de la grille avec uniquement des 0
        self.contenu[0][0] = nombre.generer()
        print("Contenu de la grille :", self.contenu)
        self.taille = len(self.contenu) # Taille de la grille
        self.police_nombres = pygame.font.Font(None, 100) # Police de caractères pour afficher les nombres

    def generer(self, element=0) -> list:
        "Génère une grille de jeu de dimension 4*4, avec l'élément spécifié à chaque case."
        return [[element for _ in range(4)] for _ in range(4)]

    def est_pleine(self) -> bool:
        "Vérifie si la grille de jeu est pleine (aucun 0 présent) et renvoie un booléen"
        return all(0 not in ligne for ligne in self.contenu)


    def cases_vides(self) -> list:
        "Calcule la position de chaque case vide dans la grille et renvoie une liste de tuples, un pour chaque position."

        pos_cases_vides = [] # Liste contenant la position de chaque case vide

        # Parcourir chaque ligne de la grille
        for ligne in range(self.taille):
            # Parcourir chaque colonne de la ligne
            for colonne in range(len(self.contenu[ligne])):
                if self.contenu[ligne][colonne] == 0: # Si le contenu de la case aux coordonnées (ligne, colonne) vaut zéro, alors elle est vide
                    # Ajouter le tuple de coordonnées (ligne, colonne) à la liste
                    pos_cases_vides.append((ligne, colonne))


        # Quand toutes les positions sont trouvées, renvoyer la liste de tuples
        return pos_cases_vides            



    

    def coordonnees(self, ligne=0, col=0, hauteur_case=145, largeur_case=195, marge=5) -> tuple:
        """Convertit les coordonnées (ligne, col) en coordonnées cartésiennes (x, y). Renvoie un tuple.
        - ligne: numéro de la ligne.
        - col: numéro de la colonne.
        - hauteur_case : entier représentant la hauteur d'une case.
        - largeur_case : entier représentant la largeur d'une case.
        - marge : entier représentant la marge entre les cases."""

        # Calcul des coordonées x et y
        x = col * largeur_case + marge
        y = ligne * hauteur_case + marge

        return (x, y)
    
    def dessiner(self, ecran:pygame.Surface) -> None:
        "Dessine la grille à l'écran."



        # Couleurs des nombres à afficher dans les cases

        couleurs = {
            nombre.base16(0): (0, 0, 0),
            nombre.base16(2): (22, 22, 22),
            nombre.base16(4): (128, 114, 19),
            nombre.base16(8) : (255, 165, 0),
            nombre.base16(16): (255, 69, 0),
            nombre.base16(32): (238, 130, 238),
            nombre.base16(64): (128, 128, 128),
            nombre.base16(128): (64, 64, 64),
            nombre.base16(256): (32, 32, 32),
            nombre.base16(512): (16, 16, 16),
            nombre.base16(1024): (8, 8, 8),
            nombre.base16(2048): (4, 4, 4)

        }

        # Hauteur et largeur d'une case
        hauteur_case = 145
        largeur_case = 195


        

        marge = 5 # Laisser une marge de 5 pixels entre les lignes

        for i in range(self.taille):
            # Dessiner les lignes horizontales
            for y in range(self.taille + 1):
                pygame.draw.line(ecran, (128, 128, 128), (0, y*(hauteur_case + marge)), (self.taille * (largeur_case + marge), y*(hauteur_case + marge)), 10)
            
            


            # Dessiner les lignes horizontales
            for j in range(self.taille + 1):
                pygame.draw.line(ecran, (128, 128, 128), (j * (largeur_case + marge), 0), 
                             (j * (largeur_case + marge), self.taille * (hauteur_case + marge)), 10)

    
        # Afficher les nombres dans chaque case
        #ecran.fill((0, 0, 0))
        for ligne in range(self.taille):
            for col in range(self.taille):
                valeur = self.contenu[ligne][col] # Récupérer le contenu de chaque case de la grille
                #print(valeur)
                if valeur != 0: # Si la valeur est différente de 0 (case non vide)
                    # L'afficher en base 16 dans la grille graphique
                    #valeur = nombre.base16(valeur)
                    affichage = self.police_nombres.render(str(valeur), True, couleurs[nombre.base16(valeur)])
                    # Récupérer les coordonnées cartésiennes de la ligne et de la colonne actuelle pour l'affichage.
                    pos_x, pos_y = self.coordonnees(ligne, col, hauteur_case, largeur_case, marge)

                    # Centrer le texte
                    rect_texte = affichage.get_rect()
                    pos_x += (largeur_case - rect_texte.width) // 2
                    pos_y += (hauteur_case - rect_texte.height) // 2

                    # Afficher le texte
                    ecran.blit(affichage, (pos_x, pos_y))

