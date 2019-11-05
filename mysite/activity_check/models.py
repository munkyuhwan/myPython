from django.db import models
from member.models import Member


class ActivityCheck(models.Model):
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_complete_cnt = models.IntegerField()
    over_order_cnt = models.IntegerField()
    pickup_avg = models.IntegerField()
    pickup_complete_avg = models.IntegerField()
    order_avg_distance = models.IntegerField()
    order_acc_distance = models.IntegerField()
    pickup_request_complete = models.IntegerField()
    pickup_20min = models.IntegerField()
    pickup_40min = models.IntegerField()

