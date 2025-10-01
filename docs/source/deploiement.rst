.. _deploiement:


Déploiement
===========

Le projet utilise **GitHub Actions** pour la CI/CD, **Docker** pour la conteneurisation et **Render** pour l'hébergement.

Pipeline CI/CD
--------------

1. **Tests et linting** exécutés sur toutes les branches :
   - flake8 (aucune erreur tolérée)
   - pytest (execution des tests)
   - coverage (minimum 80% requis)

   Important : les tests sont exécutés sur chaque push et pull request, peut importe la branche.

2. **Build et déploiement** uniquement sur `main` :
   - Build Docker automatique
   - Push vers Docker Hub
   - Notification à Render via un webhook
   - Déploiement automatique sur Render

   Important : Chaque push sur `master` déclenche un nouveau déploiement automatique.


Render
------

- Service : Web Service
- Port exposé : **8000**
- Dockerfile utilisé pour construire l'image
- Variables d'environnement chargées automatiquement depuis `.env`

Une fois déployé, l'application est accessible sur l'URL fournie par Render.


