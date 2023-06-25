from django.db import models

# Create your models here.
class MyModel(models.Model):
    plain = models.CharField(max_length=200)
    compressed = models.CharField(max_length=200)
    status = models.IntegerField()