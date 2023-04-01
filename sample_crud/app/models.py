from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    
