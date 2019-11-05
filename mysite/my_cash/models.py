from django.db import models


# Create your models here.

class MyCash(models.Model):
    cashDate = models.CharField(max_length=200)
    cashShopName = models.CharField(max_length=200)
    cashNumber = models.CharField(max_length=200)
    cashType = models.CharField(max_length=200)
    cashAmt = models.CharField(max_length=200)
    cashTitle = models.CharField(max_length=200)




