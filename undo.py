"undo.py implémente des fonctionnalités pour défaire ou refaire le dernier coup joué"
import copy
import historique


def defaire(grille_jeu:list, historique_jeu:historique.Historique) -> list:
    "Défait la dernière action jouée en utilisant un historique du jeu, renvoie la grille actualisée."

    # Etat précédent de la grille de jeu, au départ l'actuel
    etat_precedent = copy.deepcopy(grille_jeu)
    if len(historique_jeu.contenu) > 0: # Si l'historique du jeu contient plus d'un coup jou
        # Récupérer l'état précédent et le renvoyer
        etat_precedent = historique_jeu.etat_grille(len(historique_jeu.contenu) -1)
        return etat_precedent
    
    # Si aucune action ne peut être annulée, renvoyer l'état actuel
    return grille_jeu


def refaire(grille_jeu:list, historique_jeu:historique.Historique) -> list:
    "Refait la dernière action annulée en utilisant un historique du jeu, renvoie la grille actualisée."
    
    # Etat annulé à rétablir, l'actuel pour l'instant
    etat_annule = copy.deepcopy(grille_jeu)
    # Récupérer le dernier état enregistré et le renvoyer
    etat_annule = historique_jeu.etat_grille(len(historique_jeu.contenu))
    return etat_annule

