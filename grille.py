"grille.py permet de générer une grille de jeu."
import pygame


class Grille:
    "Grille de jeu"
    def __init__(self):
        "Constructeur de la grille"
        self.contenu = self.generer(0) # Générer le contenu de la grille avec uniquement des 0

    def generer(self, element=0) -> list:
        "Génère une grille de jeu de dimension 4*4, avec l'élément spécifié à chaque case."
        return [[element]*4]*4

    def est_pleine(self) -> bool:
        "Vérifie si la grille de jeu est pleine (aucun 0 présent) et renvoie un booléen"
        return all(0 not in ligne for ligne in self.contenu)
    
    def dessiner(self, ecran:pygame.Surface) -> None:
        "Dessine la grille à l'écran."
        pass
    

