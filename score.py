"score.py permet de gérer le score du joueur"
import pygame

class Score:
    "Score du joueur"
    def __init__(self, valeur:int, valeur_max:int, fenetre:pygame.Surface) -> None:
        """Initialise la classe Score.
           Les propriétés suivantes permettent de régler les attributs de la classe:
               - valeur: nombre entier représentant la valeur de départ (0 généralement).
               - valeur_max: Meilleur score réalisé.
               - fenetre: fenêtre pygame sur laquelle afficher le score."""
        
        # Initialisation des valeurs
        self.valeur = valeur
        self.valeur_max = valeur_max
        
        # Récupérer la fenêtre de jeu
        self.fenetre = fenetre
        
   def actualiser(self, points=4) -> int:
        """Actualise le score avec une addition (score + points). Met à jour le meilleur score si besoin.
           Renvoie le score actualisé."""
        self.valeur += valeur
        # Mettre à jour le meilleur score si besoin
        if self.valeur > self.valeur_max:
            self.valeur_max = self.valeur
            
        return self.valeur    
        