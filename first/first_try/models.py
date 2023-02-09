from django.db import models

# Create your models here.

class Product(models.Model):
    weight = models.FloatField()
    name_tag = models.CharField(max_length=50)
    price = models.FloatField()
