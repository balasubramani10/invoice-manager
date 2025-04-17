from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

    



