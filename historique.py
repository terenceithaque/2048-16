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
        if len(self.contenu) == 0:
            n_coup = 0

        else:    
            n_coup = len(self.contenu) + 1 # Numéro du coup correspondant
        self.contenu[n_coup] = nouvel_etat # Enregistrer l'état dans l'historique
        return self.contenu

    def etat_grille(self, cle:int) -> list:
        """Retourne la valeur (état de la grille) correspondant à une clé (numéro d'un coup joué).
        - cle: numéro de coup pour lequel on souhaite retrouver l'état de la grille. Doit être strictement supérieur à zéro
        et ne doit pas non plus dépasser la longueur de l'historique.
        Si aucune corresponde n'est trouvée, renvoie le premier état de la grille enregistré."""

        # Assertions
        assert (type(cle).__name__ =="int"), "La clé doit être le numéro d'un coup joué."
        assert (cle >= 0 and cle <= len(self.contenu)), "La clé ne peut être comprise qu'entre 0 (inclus) et la longueur de l'historique (incluse)."


        dernier_etat = self.contenu[0] # Valeur à renvoyer par défaut -> le premier état enregistré

        # Parcourir l'historique pour retrouver l'état de la grille correspondant
        for c, etat in self.contenu.items():
            # Si la clé actuelle correspond à la clé spécifiée
            if c == cle:
                # Renvoyer l'état de la grille correspondant
                return etat

        # Si aucun résultat n'a été trouvé, renvoyer le dernier état enregistré
        return dernier_etat
    
    
    def dernieres_additions(self, n:int) -> int:
        "Renvoie la somme des additions réalisées au n-ième état de la grille."
        assert (type(n).__name__ == "int"), "n doit être un entier."
        assert n >= 1, "n doit être supérieur ou égal à 1."

        # Récupérer l'état de la grille pour le n-ième coup ainsi que le précédent.
        grille_etat_n = self.contenu(n)
        grille_etat_prec = self.contenu(n-1)
