from django import forms
from .models import Task, Developer

# Classe formulaire permet de gerer les formulaires directement via les modèles

class TaskForm(forms.ModelForm):
    assignee = forms.ModelChoiceField(queryset=Developer.objects.all(),required=False)
    class Meta: 
        model = Task
        fields = ['title', 'description', 'assignee']