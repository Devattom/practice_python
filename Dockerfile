FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements (si tu en as)
COPY requirements.txt* ./

# Installer les dépendances Python si le fichier existe
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Installer des packages utiles pour le développement
RUN pip install --no-cache-dir ipython jupyter matplotlib pandas numpy requests

# Copier le code source
COPY . .

# Exposer le port pour Jupyter (optionnel)
EXPOSE 8888

# Commande par défaut
CMD ["python"]