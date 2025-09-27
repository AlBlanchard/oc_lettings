Architecture
============

Aperçu
------

Le projet est une application Django découpée en trois modules :

- **oc_lettings_site** : configuration globale, vues principales, gestion des erreurs 404/500.
- **lettings** : gestion des annonces immobilières.
- **profiles** : gestion des profils utilisateurs.

Fonctionnalités techniques
--------------------------

- **Sentry** : utilisé pour la collecte des erreurs et la traçabilité des événements.
- **Audit Decorator** : décorateur personnalisé pour tracer automatiquement les appels aux vues et commandes.
- **Whitenoise** : gère les fichiers statiques (CSS, JS, images) directement dans le container.
- **Fixtures JSON** : préchargent les données de test (lettings et profils).

Pipeline CI/CD
--------------

- **GitHub Actions** :  
  - Vérifie le linting et les tests sur toutes les branches.
  - Construit et déploie l'image Docker uniquement sur la branche ``main``.

- **Docker** :  
  - Image basée sur ``python:3.10-slim``.  
  - Contient toutes les dépendances, les migrations automatiques et le chargement des fixtures.

- **Render** :  
  - Héberge l'application web.
  - Gère automatiquement la reconstruction du service à chaque nouvelle image Docker.

