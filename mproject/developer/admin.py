from django.contrib import admin

from .models import Developer
from task.models import Task

# Permet d'importer les taches dans la page admin
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

# Page d'administration des developpeurs,
# On ajoute is_free qui est une méthode en tant que parametre
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_free')
    inlines = [TaskInline]

# Ajout du modèle developpeur a la page d'admin
admin.site.register(Developer, DeveloperAdmin)