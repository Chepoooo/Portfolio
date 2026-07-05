from django.shortcuts import render, HttpResponse
from django import urls
from .models import Project, Social
import os
from django.http import FileResponse
from django.conf import settings

def main(request):
    project = Project.objects.all()
    socials = Social.objects.all()
    
    context = {
        'project':project,
        'socials': socials
    }
    return render(request, 'home.html', context)
    
    

def download_cv(request):
    file_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'portmedia', 'cvluis.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True)





