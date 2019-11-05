from django.db import models

# Create your models here.

class OrderList(models.Model):
    shop_name = models.CharField(max_length=200)
    address_from = models.CharField(max_length=200)
    address_new_from = models.CharField(max_length=200)
    address_to = models.CharField(max_length=200)
    serial_num = models.CharField(max_length=200)
    time_limit = models.CharField(max_length=200)
    payment_type = models.CharField(max_length=200)
    payment_amt = models.CharField(max_length=200)
    delivery_fee = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
    request = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    
 	