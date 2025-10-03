Utilisation
===========

Accès local
-----------

Une fois le serveur lancé :

- Page d'accueil : http://127.0.0.1:8000
- Liste des lettings : http://127.0.0.1:8000/lettings/
- Liste des profils : http://127.0.0.1:8000/profiles/
- Ou utilisez le menu pour accéder aux sections Lettings et Profiles.

Cas d'utilisation
-----------------

1. **Consulter la liste des locations**
   - Rendez-vous sur « Lettings » pour voir toutes les annonces disponibles.
   - Cliquez sur une annonce pour afficher les détails (titre, adresse, etc.).

2. **Consulter un profil utilisateur**
   - Rendez-vous sur « Profiles ».
   - Sélectionnez un utilisateur pour afficher son profil et sa ville préférée.

3. **Gérer les erreurs**
   - Si vous accédez à une page inexistante, une page d'erreur 404 personnalisée s'affiche.
   - En cas d'erreur interne, une page 500 s'affiche et l'incident est remonté à Sentry.

Reporting Sentry
----------------

L'application utilise Sentry pour le suivi des erreurs et des performances.
N'oubliez pas de configurer la variable d'environnement `SENTRY_DSN` avec votre DSN Sentry.
Pour ceci, vous reportez à la section :ref:`configuration`. 

Pour consulter les rapports Sentry :

1. Accédez à votre tableau de bord Sentry.
2. Sélectionnez votre projet.
3. Consultez les erreurs et actions signalées.
