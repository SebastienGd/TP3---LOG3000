"""
Configuration globale pour Pytest.

Ce fichier est automatiquement évalué par Pytest avant le lancement de la suite de tests.
Il assure que le répertoire racine du projet (le dossier parent de 'tests')
soit inclus dans les variables de chemin Python (`sys.path`). 

Cela corrige les erreurs locales `ModuleNotFoundError`, permettant aux 
fichiers de test d'importer directement `app` et `operators` même s'ils
sont lancés directement depuis le terminal depuis n'importe quel niveau de répertoire.
"""

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)