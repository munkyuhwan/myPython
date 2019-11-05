from django.db import models

# Create your models here.

class AutoPolicy(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
