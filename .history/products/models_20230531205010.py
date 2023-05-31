from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=999_000_000_000, decimal_places=2)
    description = models.TextField()