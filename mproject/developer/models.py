from django.db import models
from django.apps import apps

class Developer(models.Model):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    
    # Vérifie si un dev n'a aucune taches.
    def is_free(self):
        return self.tasks.count() == 0

    # Definir la valeur de retour dans le shell.
    # __str__ en python est l'équilalant de toString() en java.
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 