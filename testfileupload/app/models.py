from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


