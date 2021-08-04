from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from .models import Developer

# Liste des developpeurs
def index(request):
    context = {
        'developers': Developer.objects.all()
    }
    return render(request, 'developer/index.html', context)

# Details d'un developpeur
def detail(request, developer_id): 
    #developer = Developer.objects.get(pk=developer_id) 
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer/detail.html', {'developer': developer})