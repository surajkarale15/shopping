from django.db import models

# Create your models here.
from category.models import *

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    active = models.CharField(default='Y', max_length=50)
    
    class Meta:
        db_table ='Product_Info'

