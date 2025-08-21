from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=30)
    f_name = models.CharField(max_length=30)
    email = models.EmailField()
    product = models.CharField(max_length=1) 
    date = models.DateField(auto_now=True)