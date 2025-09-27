Déploiement
===========

Le projet utilise **GitHub Actions** pour la CI/CD et **Render** pour l'hébergement.

Pipeline CI/CD
--------------

1. **Tests et linting** exécutés sur toutes les branches :
   - flake8
   - pytest avec coverage

2. **Build et déploiement** uniquement sur `main` :
   - Build Docker
   - Push vers Docker Hub
   - Notification à Render via un webhook

Render
------

- Service : Web Service
- Port exposé : **8000**
- Dockerfile utilisé pour construire l'image
- Variables d'environnement chargées automatiquement depuis `.env`

Une fois déployé, l'application est accessible sur :

.. code-block:: text

   https://oc-lettings-xxxx.onrender.com
