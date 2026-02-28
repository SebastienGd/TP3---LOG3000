# Module Static

## Raison d'être du module

Ce répertoire contient les fichiers d'assets statiques de l'application web. Ces fichiers sont servis directement au navigateur client par Flask sans aucun traitement préalable. Ils sont responsables de la présentation visuelle (styles), du comportement côté client additionnel (scripts) ou des médias de l'application.

## Principaux fichiers et responsabilités

- `style.css` : La feuille de style en cascade unique et principale. Elle contient toutes les règles CSS pour formater la calculatrice (mise en page Flexbox/Grid, gestion du mode sombre, effet d'animations au survol et au clic des touches).

## Dépendances ou hypothèses

- Hypothèse que le dossier s'appelle explicitement `static`, ce qui permet à Flask de le router automatiquement sans configuration supplémentaire.
- Les fichiers de ce répertoire ne dépendent pas du backend et sont uniquement exécutés par le navigateur de l'utilisateur.
