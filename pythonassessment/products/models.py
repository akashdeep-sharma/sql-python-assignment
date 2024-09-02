from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_sold = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_count = models.IntegerField()

    def __str__(self):
        return self.product_name
