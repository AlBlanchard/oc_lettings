.. _configuration:

Configuration
=============

Variables d'environnement (.env)
--------------------------------

Créer un fichier ``.env`` à la racine du projet :

.. code-block:: ini

   DJANGO_SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,.onrender.com
   SENTRY_DSN=https://xxxxxxx.ingest.sentry.io/yyyyyy

Secrets GitHub (CI/CD)
----------------------

Dans **Settings > Secrets and variables > Actions**, ajouter :

- ``DOCKERHUB_USERNAME`` : identifiant Docker Hub
- ``DOCKERHUB_PASSWORD`` : mot de passe/token Docker Hub
- ``RENDER_URL`` : webhook Render pour déploiement automatique
