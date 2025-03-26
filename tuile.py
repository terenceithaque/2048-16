"tuile.py permet de gérer les tuiles du jeu"
import pygame

class Tuile:
    "Représente une tuile du jeu"
    def __init__(self, valeur:int, x:int, y:int, ecran:pygame.Surface) -> None:
        """Initalise la tuile.
            valeur: valeur de la tuile, un entier.
            x: position x de la tuile.
            y: position y de la tuile."""
        

        # Initialiser la valeur de la tuile
        self.valeur = valeur

        # Positions x et y de la tuile
        self.x = x
        self.y = y

        # Ecran sur lequel afficher la tuile
        self.ecran = ecran


    def deplacer(self, direction:str) -> None:
        "Déplace la tuile dans une direction donnée."
        if direction == "haut":
            self.y += 5

        if direction == "bas":
            self.y -= 5


        if direction == "gauche":
            self.x += 5

        if direction == "droite":
            self.x -= 5                 

    