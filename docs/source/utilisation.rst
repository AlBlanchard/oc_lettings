Utilisation
===========

Accès local
-----------

Une fois le serveur lancé :

- Page d'accueil : http://127.0.0.1:8000
- Liste des lettings : http://127.0.0.1:8000/lettings/
- Liste des profils : http://127.0.0.1:8000/profiles/

Déploiement avec Docker
-----------------------

1. Construire l'image Docker :

   .. code-block:: bash

      docker build -t oc-lettings .

2. Lancer le container :

   .. code-block:: bash

      docker run -it -p 8000:8000 --env-file .env oc-lettings

3. Accéder à l'application sur : http://127.0.0.1:8000

Déploiement sur Render
----------------------

- L'application est déployée automatiquement via GitHub Actions.
- À chaque push sur la branche ``main``, une nouvelle image Docker est construite et envoyée.
- Render récupère automatiquement cette image et redémarre le service.
