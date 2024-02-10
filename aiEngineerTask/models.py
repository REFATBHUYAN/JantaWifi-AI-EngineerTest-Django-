from django.db import models
from django.utils import timezone

class StockModel(models.Model):
    date = models.DateField(default=timezone.now)
    trade_code = models.CharField(max_length=100)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

