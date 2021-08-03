from django.shortcuts import render
# from django.http import HttpResponse

from .models import Developer

def index(request):
    context = {
        'developers': Developer.objects.all()
    }
    return render(request, 'developer/index.html', context)