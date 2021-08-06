from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin

from .forms import DeveloperForm, DeveloperChangeForm
from .models import Developer
from task.models import Task

# Permet d'importer les taches dans la page admin
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

# Page d'administration des developpeurs,
# On ajoute is_free qui est une méthode en tant que parametre
class DeveloperAdmin(UserAdmin): 
    add_form = DeveloperForm
    form = DeveloperChangeForm
    model = get_user_model()
    list_display = ('first_name', 'last_name', 'username', 'is_free', 'username')
    inlines = [TaskInline]

# Ajout du modèle developpeur a la page d'admin
admin.site.register(Developer, DeveloperAdmin)