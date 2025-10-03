Structure de la base de données
===============================

La base de données est composée des modèles principaux suivants :

- **Address**
  - Champs : number, street, city, state, zip_code, country_iso_code

- **Letting**
  - Champs : title
  - Relation : ForeignKey vers **Address**

- **Profile**
  - Champs : favorite_city
  - Relation : OneToOne avec l'utilisateur **User** de Django

- **User**
  - Modèle standard de Django (nom, email, mot de passe, etc.)
  - Étendu via le modèle **Profile**

Schéma simplifié
----------------

.. code-block::

    User 1---1 Profile
           |
           |
    Letting *---1 Address
