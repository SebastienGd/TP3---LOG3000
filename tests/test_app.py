"""
Module de tests : test_app.py

Teste le backend de l'application Flask, l'évaluation de la logique d'analyse
dans `calculate()`, et la réponse des différents requêtes HTTP.
"""

import pytest
from app import app, calculate

@pytest.fixture
def client():
    """
    Fixture Pytest qui initialise un client web de test pour Flask.
    """
    with app.test_client() as client:
        yield client

def test_calculate_valid_expressions():
    """
    Teste la fonction d'analyse de la calculatrice avec des expressions de base valides.
    """
    assert calculate("2+2") == 4
    assert calculate("  5 - 3  ") == 2
    assert calculate("4 * 3") == 12
    assert calculate("10 / 2") == 5

def test_calculate_invalid_expressions():
    """
    Teste les rejets de la calculatrice en présence d'expressions corrompues ou invalides.
    """
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")
        
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("2 + 3 + 4")
        
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+5")

    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a + b")

def test_flask_index_get(client):
    """
    Teste l'accessibilité de la page web principale avec la méthode GET.
    Vérifie que le client HTTP reçoit le code statut 200 (OK).
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data

def test_flask_index_post_valid(client):
    """
    Teste le calcul à travers la requête de formulaire (POST) simulée.
    """
    response = client.post('/', data={'display': '5+5'})
    assert response.status_code == 200
    # Vérifie si le résultat '10' est correctement inséré dans le template.
    assert b'value="10"' in response.data or b'value="10.0"' in response.data

def test_flask_index_post_error(client):
    """
    Teste le comportement de renvoi d'erreur du POST web lors d'une mauvaise entrée.
    """
    response = client.post('/', data={'display': 'x/y'})
    assert response.status_code == 200
    assert b'Error:' in response.data

def test_flask_index_ui_button_2(client):
    """Vérifie que le bouton 2 est correctement libellé sur l'interface."""
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert ">2<" in html, "Erreur UI: Le bouton 2 est manquant ou affiche un libellé erroné."

def test_flask_index_ui_button_8(client):
    """Vérifie que le bouton 8 est correctement libellé sur l'interface."""
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert ">8<" in html, "Erreur UI: Le bouton 8 est manquant ou affiche un libellé erroné. "

def test_flask_index_ui_operator_multiply(client):
    """Vérifie que le bouton de multiplication a le bon symbole visuel."""
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert ">*<" in html, "Erreur UI: Le bouton de multiplication est manquant ou affiche un libellé erroné. "

def test_flask_index_ui_operator_divide(client):
    """Vérifie que le bouton de division a le bon symbole visuel."""
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert ">/<" in html, "Erreur UI: Le bouton de division est manquant ou affiche un libellé erroné. "