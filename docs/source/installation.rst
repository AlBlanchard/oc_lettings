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

4. Collecter les statics en vue du déploiement :

   .. code-block:: bash

      python manage.py collectstatic

5. Tester le serveur en local :

   .. code-block:: bash

      python manage.py runserver

   Si toutes les étapes se sont bien déroulées, le site sera accessible à l'adresse : http://127.0.0.1:8000
   Pour un déploiement en production, passer à la section :ref:`configuration` puis :ref:`deploiement`.


