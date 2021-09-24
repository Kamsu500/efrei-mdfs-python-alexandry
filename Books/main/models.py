from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    date = models.DateField(max_length=max)
    language = models.CharField(max_length=100)
    pages = models.IntegerField(max_length=max)
