from django.db import models

# Create your models here.
class Product(models.Model):
    
    pname=models.charfield(max-length=50)
    pcartegory=models.charfield(max-length=50)
    pprice=models.int(max-length=100)

class cartd(models.Model):
     pname=models.charfield(max-length=50)
     pprice=models.charfield(max-length=50)


