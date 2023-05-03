from django.db import models

# Create your models here.
class Cases(models.Model):
    casetype = models.CharField(max_length=10)
    crimename = models.CharField(max_length=50)

class Files(models.Model):
    file = models.FileField(upload_to='files/')
    date = models.DateField(auto_now_add=True)
    cases = models.ForeignKey(Cases, on_delete=models.CASCADE)

class ZipFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.BinaryField()