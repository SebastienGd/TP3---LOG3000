# Module Templates

## Raison d'être du module

Ce répertoire contient les modèles (templates) de pages web utilisés pour générer l'interface utilisateur (UI). Flask s'appuie sur le moteur de rendu Jinja2 pour analyser ces fichiers, y injecter des données dynamiques envoyées depuis le serveur (comme les retours de requêtes ou les résultats de calculs) puis générer une vue HTML pure qui est renvoyée au client.

## Principaux fichiers et responsabilités

- `index.html` : Le point d'entrée visuel de l'application.
  - **Responsabilité 1 :** Déclarer la structure HTML du formulaire de la calculatrice (l'écran d'affichage et la grille des boutons).
  - **Responsabilité 2 :** Intégrer de petits scripts JavaScript en ligne pour gérer l'interaction des clics simulés avant soumission (`appendToDisplay` et `clearDisplay`).
  - **Responsabilité 3 :** Afficher la variable `{{ result }}` obtenue à l'issue de l'opération POST via le serveur Flask.

## Dépendances ou hypothèses

- Ces fichiers dépendent du système de langage de gabarit **Jinja2** (fourni d'office par Flask).
- L'intégration aux fichiers statiques (comme le CSS) s'effectue via la méthode Flask `url_for('static', filename='...')`.
- Hypothèse que tout nouveau fichier HTML devra être placé ici pour que la méthode `render_template` de Flask puisse l'identifier.
