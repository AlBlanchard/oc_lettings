Utilisation
===========

Accès local
-----------

Une fois le serveur lancé :

- Page d'accueil : http://127.0.0.1:8000
- Liste des lettings : http://127.0.0.1:8000/lettings/
- Liste des profils : http://127.0.0.1:8000/profiles/

Reporting Sentry
----------------

L'application utilise Sentry pour le suivi des erreurs et des performances.
N'oubliez pas de configurer la variable d'environnement `SENTRY_DSN` avec votre DSN Sentry.
Pour ceci, vous reportez à la section :ref:`Configuration`. 

Pour consulter les rapports Sentry :

1. Accédez à votre tableau de bord Sentry.
2. Sélectionnez votre projet.
3. Consultez les erreurs et actions signalées.
