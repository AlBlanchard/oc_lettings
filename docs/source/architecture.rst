Architecture
============

Organisation du projet Django
-----------------------------

- **oc_lettings_site** : application principale
- **profiles** : gestion des profils utilisateurs
- **lettings** : gestion des adresses et logements

Fichiers importants
-------------------

- `Dockerfile` : construction de l'image
- `docker-compose.yml` : exécution locale simplifiée
- `entrypoint.sh` : initialise la base, collecte les statiques et lance Gunicorn
- `requirements.txt` : dépendances
- `.readthedocs.yaml` : configuration Read the Docs

Gestion des fichiers statiques
------------------------------

- **WhiteNoise** est utilisé pour servir les fichiers statiques en production.
- `collectstatic` est exécuté lors de la construction de l'image Docker.
- Les fichiers sont regroupés dans `/app/staticfiles`.

Monitoring et audit
-------------------

- **Sentry** intégré pour la remontée des erreurs.
- Un système d'**audit avec breadcrumbs et événements** enregistre les actions importantes.
