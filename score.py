"score.py permet de gérer le score du joueur"
import pygame
import json
import os


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
        self.valeur += points
        # Mettre à jour le meilleur score si besoin
        if self.valeur > self.valeur_max:
            self.valeur_max = self.valeur
            
        return self.valeur
    
    def sauvegarder(self):
       "Sauvegarde le score actuel et le score maximal dans un fichier JSON"
       # Le dossier de sauvegarde est celui utilisé par le script (référence __file__)
       dossier_sauvegarde = os.path.dirname(os.path.abspath(__file__))
       print("Dossier de sauvegarde: ", dossier_sauvegarde)
       
       fichier_sauvegarde = os.path.join(dossier_sauvegarde, "score.json")

       dict_scores = {
           "score":self.valeur,
           "max_score":self.valeur_max
       }

       # Créer le fichier de sauvegarde et écrire les données dedans
       with open(fichier_sauvegarde, "w") as f:
           donnees = json.dump(dict_scores, f)
           f.close()


    def recuperer(self):
        "Récupère le score depuis un fichier JSON."
        pass       
        