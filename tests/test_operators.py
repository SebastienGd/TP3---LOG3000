"""
Module de tests : test_operators.py

Définit les tests unitaires pour le module `operators.py`.
Vérifie que les fonctions mathématiques retournent le résultat arithmétique attendu.
"""

import pytest
from operators import add, subtract, multiply, divide

def test_add():
    """
    Teste la fonction d'addition.
    Vérifie l'addition de base entre des nombres entiers et flottants.
    """
    assert add(2, 3) == 5
    assert add(10.5, 2.5) == 13.0
    assert add(-5, 5) == 0

def test_subtract():
    """
    Teste la fonction de soustraction.
    Vérifie la soustraction normale (a - b).
    NOTE: La soustraction est censée renvoyer `a - b`.
    """
    assert subtract(5, 3) == 2
    assert subtract(10.5, 2.5) == 8.0
    assert subtract(0, 5) == -5

def test_multiply():
    """
    Teste la fonction de multiplication.
    Vérifie la multiplication de base entre des nombres.
    NOTE: La multiplication doit renvoyer le produit `a * b`.
    """
    assert multiply(3, 4) == 12
    assert multiply(5.0, 2) == 10.0
    assert multiply(-2, 3) == -6

def test_divide():
    """
    Teste la fonction de division.
    Vérifie la division décimale classique (a / b).
    NOTE: La division classique suppose une précision décimale, pas uniquement une division entière.
    """
    assert divide(10, 2) == 5
    assert divide(9, 2) == 4.5
    assert divide(5.0, 2.0) == 2.5