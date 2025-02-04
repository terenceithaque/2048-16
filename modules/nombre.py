"nombres.py permet de générer des nombres aléatoires, de les convertir en base 16"
import random # Importer le module random

def generer() -> int:
    """Génère un nombre au hasard, 2 ou 4 selon des probabilités"""
    # Logique à implémenter ici
    pass

def base16(nombre:int) -> str:
    """Renvoie un nombre converti en base 16 sans les caractères de début de la fonction traditionelle hex(), sous forme de
    chaîne de caractères.
    
    -nombre: le nombre (entier) à convertir en base 16"""

    n = "%x" % nombre # Nombre converti en base 16 et formaté pour enlever le "0x"
    return n


# Tests
for n in range(8193):
    if n % 2048 == 0:
        print(n, ":", base16(n))
