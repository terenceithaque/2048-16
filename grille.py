"grille.py permet de générer une grille de jeu."
import pygame
import nombre


class Grille:
    "Grille de jeu"
    def __init__(self, taille=4):
        "Constructeur de la grille"
        self.contenu = self.generer(0) # Générer le contenu de la grille avec uniquement des 0
        self.contenu[0][0] = nombre.generer()
        self.taille = 4 # Taille de la grille

    def generer(self, element=0) -> list:
        "Génère une grille de jeu de dimension 4*4, avec l'élément spécifié à chaque case."
        return [[element]*4]*4

    def est_pleine(self) -> bool:
        "Vérifie si la grille de jeu est pleine (aucun 0 présent) et renvoie un booléen"
        return all(0 not in ligne for ligne in self.contenu)
    
    def dessiner(self, ecran:pygame.Surface) -> None:
        "Dessine la grille à l'écran."
      

        # Hauteur et largeur d'une case
        hauteur_case = 145
        largeur_case = 195


        

        marge = 5 # Laisser une marge de 5 pixels entre les lignes

        for i in range(self.taille):
            # Dessiner les lignes horizontales
            for i in range(self.taille + 1):
                pygame.draw.line(ecran, (128, 128, 128), (0, i*(hauteur_case + marge)), (self.taille * (largeur_case + marge), i*(hauteur_case + marge)), 10)

            # Dessiner les lignes horizontales
            for j in range(self.taille + 1):
                pygame.draw.line(ecran, (128, 128, 128), (j * (largeur_case + marge), 0), 
                             (j * (largeur_case + marge), self.taille * (hauteur_case + marge)), 10)

    

