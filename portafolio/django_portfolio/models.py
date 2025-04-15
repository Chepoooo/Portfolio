from django.db import models
from django.db.models.fields import URLField

class Project(models.Model):
    title = models.CharField(max_length=30, blank=False, null=True)
    description = models.TextField(max_length=500, blank = False, null = False)
    image = models.ImageField(upload_to="django_portfolio/images/")
    url = URLField(blank=True)
    
    
    def __str__(self):
        return self.title
    
    
