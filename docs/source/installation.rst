Installation
============

Prérequis
---------

- Python 3.10
- pip
- Docker et Docker Compose (pour la version containerisée)
- Compte GitHub (pour le déploiement sur Render et ReadTheDocs)

Installation locale
-------------------

1. Cloner le dépôt :

   .. code-block:: bash

      git clone https://github.com/AlBlanchard/oc_lettings.git
      cd oc_lettings

2. Créer un environnement virtuel et installer les dépendances :

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # sous Linux/Mac
      venv\Scripts\activate     # sous Windows

      pip install -r requirements.txt

3. Appliquer les migrations et charger les données de test :

   .. code-block:: bash

      python manage.py migrate
      python manage.py loaddata fixture.json

4. Lancer le serveur en local :

   .. code-block:: bash

      python manage.py runserver

   Le site sera accessible à l'adresse : http://127.0.0.1:8000
