from django.db import models

# Create your models here.
class Product(models.Model):
    
    pname=models.CharField(max_length=50)
    pcartegory=models.CharField(max_length=50)
    pprice=models.IntegerField(max_length=100)
    pid=models.UUIDField(max_length=50)
class cartd(models.Model):
     pname=models.CharField(max_length=50)
     pprice=models.CharField(max_length=50)
     cid=models.UUIDField(max_length=50)


