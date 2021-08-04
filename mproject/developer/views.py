#imports django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#imports locaux
from .models import Developer
from .forms import DeveloperForm

# Liste des developpeurs
def index(request):
    context = {
        'developers': Developer.objects.all(),
        'form': DeveloperForm,
    }
    return render(request, 'developer/index.html', context)

# Details d'un developpeur
def detail(request, developer_id): 
    #developer = Developer.objects.get(pk=developer_id) 
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer/detail.html', {'developer': developer})

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