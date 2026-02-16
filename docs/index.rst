Orange County Lettings - Documentation
======================================

Bienvenue dans la documentation du projet Orange County Lettings.

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

Description du projet
=====================

Orange County Lettings est une application web Django permettant de gérer des locations immobilières et des profils utilisateurs.

Fonctionnalités principales
----------------------------

* Gestion des locations (lettings)
* Gestion des profils utilisateurs
* Interface d'administration Django
* API REST pour les données
* Système de monitoring avec Sentry

Installation
============

Prérequis
---------

* Python 3.11+
* pip
* Git

Instructions d'installation
---------------------------

1. Cloner le repository::

    git clone https://github.com/Volt529/Orange.git
    cd Orange

2. Créer un environnement virtuel::

    python -m venv venv
    venv\Scripts\activate

3. Installer les dépendances::

    pip install -r requirements.txt

4. Configurer les variables d'environnement::

    Créer un fichier .env à la racine:
    
    SECRET_KEY=votre_secret_key
    DEBUG=True
    SENTRY_DSN=votre_dsn_sentry

5. Effectuer les migrations::

    python manage.py migrate

6. Créer un superutilisateur::

    python manage.py createsuperuser

7. Lancer le serveur::

    python manage.py runserver

Guide de démarrage rapide
==========================

Lancer le projet localement
----------------------------

Après l'installation::

    python manage.py runserver

Accédez à http://localhost:8000

Lancer les tests
----------------

::

    python manage.py test

Avec couverture::

    coverage run --source='.' manage.py test
    coverage report

Linter le code
--------------

::

    flake8

Technologies utilisées
======================

Backend
-------

* **Django 5.2.7** - Framework web Python
* **Python 3.11** - Langage de programmation
* **Gunicorn** - Serveur WSGI pour la production
* **WhiteNoise** - Gestion des fichiers statiques

Base de données
---------------

* **SQLite3** - Base de données (développement et production)

Tests et Qualité
----------------

* **pytest** - Framework de tests
* **pytest-django** - Plugin pytest pour Django
* **pytest-cov** - Couverture de code
* **flake8** - Linter Python
* **coverage** - Mesure de couverture de tests

Monitoring et Logging
---------------------

* **Sentry** - Surveillance des erreurs et monitoring

Déploiement et DevOps
---------------------

* **Docker** - Conteneurisation
* **GitHub Actions** - CI/CD
* **Render** - Hébergement cloud
* **Docker Hub** - Registry d'images Docker

Structure de la base de données
================================

Modèles principaux
------------------

Address
~~~~~~~

Représente une adresse géographique.

Champs:
    * number (PositiveIntegerField) - Numéro de rue
    * street (CharField) - Nom de la rue
    * city (CharField) - Ville
    * state (CharField) - État (2 caractères)
    * zip_code (PositiveIntegerField) - Code postal
    * country_iso_code (CharField) - Code pays ISO (3 caractères)

Letting
~~~~~~~

Représente une location.

Champs:
    * title (CharField) - Titre de la location
    * address (OneToOneField) - Relation avec Address

Profile
~~~~~~~

Représente le profil d'un utilisateur.

Champs:
    * user (OneToOneField) - Relation avec User Django
    * favorite_city (CharField) - Ville favorite

Guide d'utilisation
===================

Interface web
-------------

Page d'accueil
~~~~~~~~~~~~~~

Accessible à http://localhost:8000/

Affiche les liens vers les lettings et profiles.

Lettings
~~~~~~~~

* Liste: http://localhost:8000/lettings/
* Détail: http://localhost:8000/lettings/<id>/

Profiles
~~~~~~~~

* Liste: http://localhost:8000/profiles/
* Détail: http://localhost:8000/profiles/<username>/

Interface d'administration
--------------------------

Accès à http://localhost:8000/admin/

Permet de gérer:

* Les utilisateurs
* Les locations (Lettings)
* Les adresses (Addresses)
* Les profils (Profiles)

Procédures de déploiement
==========================

Pipeline CI/CD
--------------

Le projet utilise GitHub Actions pour l'intégration et le déploiement continus.

Workflow automatique
~~~~~~~~~~~~~~~~~~~~

À chaque push sur la branche ``main``:

1. **Tests et Linting**
   
   * Exécution des tests unitaires
   * Vérification de la couverture de code (> 80%)
   * Linting avec flake8

2. **Build Docker**
   
   * Construction de l'image Docker
   * Tag avec le hash du commit
   * Push vers Docker Hub

3. **Déploiement**
   
   * Déclenchement du webhook Render
   * Déploiement automatique en production

Configuration GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Secrets nécessaires dans GitHub:

* ``DOCKER_USERNAME`` - Nom d'utilisateur Docker Hub
* ``DOCKER_PASSWORD`` - Token d'accès Docker Hub
* ``RENDER_DEPLOY_HOOK`` - URL du webhook Render

Configuration Render
--------------------

Variables d'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur Render, configurer:

* ``SECRET_KEY`` - Clé secrète Django
* ``DEBUG`` - False en production
* ``ALLOWED_HOSTS`` - .onrender.com
* ``SENTRY_DSN`` - DSN pour Sentry
* ``ENVIRONMENT`` - production

Déploiement manuel
------------------

Pull de l'image Docker
~~~~~~~~~~~~~~~~~~~~~~

::

    docker pull sylvaindata/oc-lettings:latest

Lancer le container
~~~~~~~~~~~~~~~~~~~

::

    docker run -p 8000:8000 \
      -e SECRET_KEY=your_secret_key \
      -e DEBUG=False \
      -e ALLOWED_HOSTS=.onrender.com \
      sylvaindata/oc-lettings:latest

URL de production
-----------------

Le site est accessible sur:

https://orangev3-1.onrender.com

Gestion de l'application
=========================

Monitoring avec Sentry
-----------------------

Sentry est configuré pour capturer:

* Les erreurs 500
* Les exceptions non gérées
* Les logs d'erreur

Accès au dashboard Sentry pour voir les erreurs en temps réel.

Logs applicatifs
----------------

Les logs sont configurés dans ``settings.py`` avec:

* Logger console pour le développement
* Logger Sentry pour la production
* Niveau INFO pour les événements normaux
* Niveau ERROR pour les erreurs

Maintenance
-----------

Sauvegardes
~~~~~~~~~~~

La base de données SQLite est incluse dans l'image Docker.

Pour les sauvegardes régulières, exporter la base::

    python manage.py dumpdata > backup.json

Mise à jour des dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    pip list --outdated
    pip install --upgrade package_name
    pip freeze > requirements.txt
