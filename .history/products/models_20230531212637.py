from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=999_000_000_000, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
    
    def __str__(self) -> str:
        return self.name