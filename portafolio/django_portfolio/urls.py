from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name ='main'),
    path('download-cv/', views.download_cv, name='download_cv'),
    
]