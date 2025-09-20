#!/bin/sh


# Permet de gérer le démarrage de l'application Django avec Gunicorn
# et d'appliquer les migrations automatiquement.


echo "Démarrage de l'application Django..."

# Applique les migrations
echo "Migration de la base..."
python manage.py migrate --noinput

# Collecte les fichiers statiques
echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Charge les données si fixture.json existe
if [ -f "fixture.json" ]; then
  echo "Chargement des données depuis fixture.json..."
  python manage.py loaddata fixture.json || true
else
  echo "Aucun fixture.json trouvé, démarrage sans données."
fi

# Lance Gunicorn
echo "Lancement de Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
