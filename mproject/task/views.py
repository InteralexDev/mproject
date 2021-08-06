# Oblige l'utilisateur a etre connecté pour avoir acces a cette application ainsi 
# qu'avoir la permission pour acceder a quelque chose
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.urls import reverse

from .models import Task
from .forms import TaskForm


class IndexView(LoginRequiredMixin,PermissionRequiredMixin, ListView): 
    model = Task
    template_name = "task/index.html" 
    context_object_name = 'tasks'
    # Demande la permission task_management pour acceder a la page
    permission_required = 'task.task_management' 
    # Permet de faire fonctionner les formulaires par la suite (transforme les données)
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs) 
        context['form'] = TaskForm 
        return context

# Details concernant un e tache
class TaskDetailVue(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/detail.html'

def create(request): 
    form = TaskForm(request.POST) 
    if form.is_valid(): 
        Task.objects.create( 
            title=form.cleaned_data['title'], 
            description=form.cleaned_data['description'],
            assignee=form.cleaned_data['assignee'],
        ) 
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('task:index')) 

def delete(request, id): 
    # On recois l'id par le lien défini dans urls (/delete/<id>)
    # Puis on le supprime du modèle via filter.delete()
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('task:index'))