# Module Tests

## Raison d'être du module

Ce répertoire contient l'ensemble de la suite de tests automatisés du projet Flask Calculator. Ces tests permettent de s'assurer que les opérations mathématiques et le traitement des requêtes HTTP fonctionnent correctement.

## Fichiers de test

- `test_operators.py` : Teste les opérations arithmétiques pures (`add`, `subtract`, `multiply`, `divide`).
- `test_app.py` : Teste la logique d'analyse de la calculatrice (`calculate`) ainsi que les réponses HTTP du serveur Flask.

## Couverture des tests

Les tests couvrent :

- L'addition, la soustraction, la multiplication et la division avec des nombres entiers et flottants.
- Les cas d'erreurs mathématiques asymétriques potentielles de la calculatrice.
- Le rejet d'expressions mathématiques invalides (vides, mauvaises lettres, sans opérateurs, doubles opérateurs).
- Le bon fonctionnement du point de terminaison de la page principale (`/`) en méthode `GET` et `POST`.

## Exécution des tests

Assurez-vous d'avoir activé votre environnement virtuel au préalable et d'être à la racine de `TP3---LOG3000`.

Exécuter la suite complète (tous les fichiers) :

```bash
pytest -v
```

Exécuter un fichier de test spécifique :

```bash
pytest tests/test_operators.py -v
```
