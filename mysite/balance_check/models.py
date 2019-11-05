from django.db import models

class BalanceCheck(models.Model):
    complete_cnt = models.IntegerField()
    commision_amt = models.IntegerField()
    after_commission = models.IntegerField()
    jingsu = models.IntegerField()
