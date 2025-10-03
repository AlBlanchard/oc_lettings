Guide de démarrage rapide
=========================

Ce guide fournit les étapes essentielles pour lancer l'application en quelques commandes.

.. note::
   Pour plus de détails, consultez la section :ref:`installation`.

Exécution locale
----------------

.. code-block:: bash

   git clone https://github.com/AlBlanchard/oc_lettings.git
   cd oc_lettings
   python -m venv venv
   source venv/bin/activate   # ou venv\Scripts\activate sous Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

L'application est accessible sur : http://127.0.0.1:8000/

Exécution via Docker
--------------------

.. code-block:: bash

   docker build -t oc-lettings .
   docker run -it -p 8000:8000 --env-file .env oc-lettings

L'application est accessible sur : http://127.0.0.1:8000/
