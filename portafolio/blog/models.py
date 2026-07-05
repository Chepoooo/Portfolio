from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=30, blank=False, null=True)
    description = models.TextField(max_length=500, blank = False, null = False)
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today)
