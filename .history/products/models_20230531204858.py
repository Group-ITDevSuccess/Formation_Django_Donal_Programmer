from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    description = models.TextField()