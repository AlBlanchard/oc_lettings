Déploiement
===========

Pipeline CI/CD
--------------

1. **Lint et tests** exécutés sur toutes les branches :
   - Flake8
   - Pytest + Coverage (seuil 80%)

2. **Build Docker + Push sur Docker Hub** uniquement sur la branche ``main``.

3. **Déploiement Render** déclenché via webhook après push de l'image.

Docker
------

Construire et lancer l'application :

.. code-block:: bash

   docker build -t oc-lettings:dev .
   docker run -it -p 8000:8000 --env-file .env oc-lettings:dev

Docker Compose (optionnel)
--------------------------

Un fichier ``docker-compose.yml`` permet de lancer l'app plus facilement :

.. code-block:: yaml

   version: "3"
   services:
     web:
       build: .
       ports:
         - "8000:8000"
       env_file:
         - .env
