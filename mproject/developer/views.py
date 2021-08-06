#Oblige l'utilisateur a etre connecté pour avoir acces a cette application
from django.contrib.auth.mixins import LoginRequiredMixin

# Imports relatifs au librairies
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

# Imports locaux
from .models import Developer
from .forms import ShortDeveloperForm
from task.forms import TaskForm

# Liste des developpeurs
# LoginRequiredMixin force les utilisateur a se log pour acceder a la page
class IndexView(LoginRequiredMixin, ListView): 
    model = Developer 
    template_name = "developer/index.html" 
    context_object_name = 'developers'
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs) 
        context['form'] = ShortDeveloperForm
        return context

# Details concernant un developpeur
# LoginRequiredMixin force les utilisateur a se log pour acceder a la page
class DevDetailVue(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = 'developer/detail.html'
    def get_context_data(self, **kwargs): 
        context = super(DevDetailVue, self).get_context_data(**kwargs) 
        form = TaskForm(initial={'assignee': get_object_or_404(Developer, pk=self.kwargs['pk'])})
        form.fields['assignee'].disabled = True
        context['form'] = form
        return context

# Interractions avec le modèle #

def create(request): 
    form = ShortDeveloperForm(request.POST) 
    if form.is_valid(): 
        Developer.objects.create( 
            first_name=form.cleaned_data['first_name'], 
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'], 
        ) 
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index')) 

def delete(request, id): 
    # On recois l'id par le lien défini dans urls (/delete/<id>)
    # Puis on le supprime du modèle via filter.delete()
    Developer.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('developer:index'))