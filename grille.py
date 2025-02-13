"grille.py permet de générer une grille de jeu."


def generer(element=0) -> list:
    "Génère une grille de jeu de dimension 4*4, avec l'élément spécifié à chaque case."
    return [[element]*4]*4

def est_pleine(grille:list) -> bool:
    "Vérifie si la grille de jeu est pleine (aucun 0 présent) et renvoie un booléen"
    return all(0 not in ligne for ligne in grille)
    

