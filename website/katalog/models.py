from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    Description = models.CharField(max_length=2083)
    image = models.ImageField(upload_to='image/')