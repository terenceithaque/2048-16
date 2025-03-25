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
            n_coup = 1

        else:    
            n_coup = len(self.contenu) + 1 # Numéro du coup correspondant
        self.contenu[n_coup] = nouvel_etat # Enregistrer l'état dans l'historique

        if len(self.contenu) > 2:
            if self.contenu[len(self.contenu) -1] == self.contenu[len(self.contenu) -2]:
                del self.contenu[len(self.contenu) -1]

        return self.contenu
    

        

    def etat_grille(self, cle:int) -> list:
        """Retourne la valeur (état de la grille) correspondant à une clé (numéro d'un coup joué).
        - cle: numéro de coup pour lequel on souhaite retrouver l'état de la grille. Doit être strictement supérieur à zéro
        et ne doit pas non plus dépasser la longueur de l'historique.
        Si aucune corresponde n'est trouvée, renvoie le premier état de la grille enregistré."""

        # Assertions
        assert (type(cle).__name__ =="int"), "La clé doit être le numéro d'un coup joué."
        assert (cle >= 0 and cle <= len(self.contenu)), "La clé ne peut être comprise qu'entre 0 (inclus) et la longueur de l'historique (incluse)."


        dernier_etat = self.contenu[1] # Valeur à renvoyer par défaut -> le premier état enregistré

        # Parcourir l'historique pour retrouver l'état de la grille correspondant
        for c, etat in self.contenu.items():
            # Si la clé actuelle correspond à la clé spécifiée
            if c == cle:
                # Renvoyer l'état de la grille correspondant
                return etat

        # Si aucun résultat n'a été trouvé, renvoyer le dernier état enregistré
        return dernier_etat
    
    
    def dernieres_additions(self) -> int:
        "Renvoie la somme des additions réalisées au dernier état de la grille."
        
        
        somme = 0

        # Récupérer l'état de la grille pour le n-ième coup ainsi que le précédent.
        if len(self.contenu) >= 3:
            grille_etat_n = self.contenu[len(self.contenu) -1]
            grille_etat_prec = self.contenu[len(self.contenu) -2]
        
            # Calculer la somme actuelle des cases et la somme précédente, puis renvoyer la différence
            somme_actuelle = sum(sum(ligne) for ligne in grille_etat_n)
            somme_prec = sum(sum(ligne) for ligne in grille_etat_prec)
            somme = somme_actuelle - somme_prec
            
        return max(0, somme)
        
        
        