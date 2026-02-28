"""
Module opérateurs arithmétiques.
Ce module définit les fonctions arithmétiques de base utilisées par la calculatrice.
"""

def add(a,b):
    """
    Additionne deux nombres.
    
    Args:
        a (float/int): Premier opérande.
        b (float/int): Deuxième opérande.
        
    Returns:
        float/int: La somme de `a` et `b`.
    """
    return a + b

def subtract(a,b):
    """
    Soustrait le deuxième nombre du premier.
    
    Args:
        a (float/int): Nombre de base.
        b (float/int): Nombre à soustraire.
        
    Returns:
        float/int: La différence `a - b`.
    """
    return a - b

def multiply(a,b):
    """
    Élève le premier nombre à la puissance du deuxième.
    
    Args:
        a (float/int): Base.
        b (float/int): Exposant.
        
    Returns:
        float/int: Le résultat de `a ** b`.
    """
    return a ** b

def divide(a,b):
    """
    Effectue une division entière du premier nombre par le deuxième.
    
    Args:
        a (float/int): Numerateur.
        b (float/int): Dénominateur.
        
    Returns:
        float/int: Le quotient entier de `a // b`.
    """
    return a // b