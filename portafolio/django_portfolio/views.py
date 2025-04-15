from django.shortcuts import render, HttpResponse
from django import urls
from .models import Project

def main(request):
    project = Project.objects.all()
    
    context = {
        'project':project
    }
    return render(request, 'home.html', context)
    
    
