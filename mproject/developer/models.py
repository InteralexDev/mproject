# Imports relatifs au librairies
from django.db import models
from django.contrib.auth.models import AbstractUser

# Permet d'importer les modèles externes a ce fichier,
# notament l'application task.
from django.apps import apps

class Developer(AbstractUser):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    
    REQUIRED_FIELDS=['first_name', 'last_name']

    # Vérifie si un dev n'a aucune taches.
    def is_free(self):
        return self.tasks.count() == 0

    # Definir la valeur de retour dans le shell.
    # __str__ en python est l'équilalant de toString() en java.
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
    # Utile pour la page /admin via le fichier admin.py
    is_free.boolean = True 
    is_free.short_description = 'Is free'