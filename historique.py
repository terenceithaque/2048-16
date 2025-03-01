"historique.py permet de gérer l'historique des coups joués"
import copy

class Historique:
    "Objet représentant un historique des coups joués par le joueur."
    def __init__(self) -> None:
        "Initialise l'historique"
        # Dictionnaire représentant le contenu de l'historique.
        # associe un nombre (n° du coup joué) à l'état de jeu correspondant.
        self.contenu = {}


    def ajouter(self, etat_grille:list) -> dict:
        "Ajoute un état de jeu à l'historique, renvoie le contenu mis à jour de ce dernier."
        nouvel_etat = copy.deepcopy(etat_grille) # Copier l'état de la grille spécifié
        n_coup = len(self.contenu) + 1 # Numéro du coup correspondant
        self.contenu[n_coup] = nouvel_etat # Enregistrer l'état dans l'historique    