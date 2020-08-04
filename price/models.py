from django.db import models

# Create your models here.
from pip._vendor.pyparsing import PrecededBy

from product.models import *
class Price(models.Model):
    prod_qty = models.IntegerField()
    prod_price=models.FloatField()
    prod_price_qty=models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    active = models.CharField(default='Y', max_length=50)

    class Meta:
        db_table = 'Price_info'