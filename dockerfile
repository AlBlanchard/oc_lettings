FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    # timeout augmenté pour éviter les erreurs de connexion
    && pip install --default-timeout=100 -r requirements.txt

# Copie le reste du projet
COPY . .

# Copie du script entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Utilise l'entrypoint comme point de départ du container
ENTRYPOINT ["/entrypoint.sh"]

# Collecter les fichiers statiques pour Django
RUN python manage.py collectstatic --noinput

# Port utilisé par Django
EXPOSE 8000

# Commandes par défaut (gunicorn = prod)
# CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]

