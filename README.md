# TP3 LOG3000 - Calculatrice Flask

## Nom du projet

TP3 LOG3000 - Flask Calculator

## Numéro d'équipe

Numéro d'équipe : 17

## Objectif

Ce projet fournit une calculatrice web simple construite avec Flask. L'objectif est d'appliquer les pratiques d'ingénierie logicielle collaborative : documentation, tests, suivi des problèmes (issues), corrections de bogues basées sur des branches, requêtes d'intégration (pull requests) et validation finale.

## Portée du projet

- Logique arithmétique et analyse d'expressions côté serveur (Backend).
- Interface de la calculatrice côté client (Frontend - HTML/CSS/JS).
- Tests automatisés pour détecter et prévenir les régressions.
- Flux de travail d'équipe traçable utilisant les problèmes GitHub et les requêtes d'intégration.

## Structure du dépôt

- `TP3---LOG3000/` : code source de l'application.
- `app.py` : point d'entrée Flask et gestion des routes.
- `operators.py` : opérations arithmétiques.
- `templates/` : modèles HTML.
- `static/` : ressources CSS.
- `tests/` : suite de tests.

## Prérequis

- Git
- Python 3.11+ et pip

## Guide d'installation

Cloner le dépôt :

```bash
git clone git@github.com:SebastienGd/TP3---LOG3000.git
```

Créer un environnement virtuel :

- Windows PowerShell : `python -m venv .venv`

Activer l'environnement :

- Windows PowerShell : `.\.venv\Scripts\Activate.ps1`

Installer les dépendances :

```powershell
python -m pip install --upgrade pip
python -m pip install flask pytest
```

## Guide d'utilisation

Lancer l'application Flask depuis `TP3---LOG3000` :

```bash
python app.py
```

Utiliser les boutons de la calculatrice pour composer une expression.
Appuyer sur `=` pour soumettre et afficher le résultat.

## Guide de test

Depuis `TP3---LOG3000` avec l'environnement virtuel activé :

Exécuter tous les tests :

```bash
pytest -q
```

Exécuter un fichier spécifique :

```bash
pytest -q tests/test_operators.py
```

Voir `TP3---LOG3000/tests/README.md` pour les détails de couverture de test.

## Flux de contribution

- Créer ou confirmer un problème (issue) GitHub décrivant le bogue/la fonctionnalité.
- Créer une branche dédiée à partir de `main` : `<type>-<id>/-short-description`
- Implémenter les modifications et ajouter/mettre à jour les tests.
- Exécuter les tests localement avant de commiter.
- Commiter avec un message clair expliquant pourquoi le changement est nécessaire.
- Ouvrir une requête d'intégration (Pull Request) liée au problème.
- Réviser et fusionner après approbation et passage des tests.

## Notes pour la remise

Assurez-vous que toutes les sections du devoir sont représentées dans l'historique du dépôt (problèmes, branches, PRs, tests, documentation).
Gardez le dépôt public à l'heure limite et évitez les commits après cette heure limite.
