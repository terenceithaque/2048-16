"nombre.py permet de générer des nombres aléatoires, de les convertir en base 16"
import random # Importer le module random

def generer() -> int:
    """Génère un nombre au hasard, 2 ou 4 selon des probabilités"""
    probabilite_4 = random.randint(0, 100) # Probabilité de générer un 4
    # Générer un 4 seulement si la probabilité d'en générer un est supérieure ou égale à 90 %
    if probabilite_4 >= 90:
        return 4
    
    return 2

def base16(nombre:int) -> str:
    """Renvoie un nombre converti en base 16 sans les caractères de début de la fonction traditionelle hex(), sous forme de
    chaîne de caractères.
    
    -nombre: le nombre (entier) à convertir en base 16"""

    n = "%x" % nombre # Nombre converti en base 16 et formaté pour enlever le "0x"
    return n



