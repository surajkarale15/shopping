from django.db import models

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=100)
    active = models.CharField(default='Y', max_length=50)

    class Meta:
        db_table ='Category_Model'