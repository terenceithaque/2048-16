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
        self.police_nombres = pygame.font.Font(None, 20) # Police de caractères pour afficher les nombres

    def generer(self, element=0) -> list:
        "Génère une grille de jeu de dimension 4*4, avec l'élément spécifié à chaque case."
        return [[element]*4]*4

    def est_pleine(self) -> bool:
        "Vérifie si la grille de jeu est pleine (aucun 0 présent) et renvoie un booléen"
        return all(0 not in ligne for ligne in self.contenu)
    

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
            nombre.base16(2): (255, 255, 255),
            nombre.base16(4): (245, 245, 245),
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
            for i in range(self.taille + 1):
                pygame.draw.line(ecran, (128, 128, 128), (0, i*(hauteur_case + marge)), (self.taille * (largeur_case + marge), i*(hauteur_case + marge)), 10)
                #n = self.police_nombres.render()


            # Dessiner les lignes horizontales
            for j in range(self.taille + 1):
                pygame.draw.line(ecran, (128, 128, 128), (j * (largeur_case + marge), 0), 
                             (j * (largeur_case + marge), self.taille * (hauteur_case + marge)), 10)

    

