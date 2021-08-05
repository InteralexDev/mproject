#imports django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
#imports locaux
from .models import Developer
from .forms import DeveloperForm

# Liste des developpeurs
class IndexView(ListView): 
    model = Developer 
    template_name = "developer/index.html" 
    context_object_name = 'developers'
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs) 
        context['form'] = DeveloperForm 
        return context

# Details concernant un developpeur
class DevDetailVue(DetailView):
    model = Developer
    template_name = 'developer/detail.html'

# Interractions avec le modèle #

def create(request): 
    form = DeveloperForm(request.POST) 
    if form.is_valid(): 
        Developer.objects.create( 
            first_name=form.cleaned_data['first_name'], 
            last_name=form.cleaned_data['last_name'] 
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