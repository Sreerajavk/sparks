from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserDetails(models.Model):

    user = models.ForeignKey(to=User , on_delete=models.CASCADE)
    consumer_no  = models.CharField(max_length=20)
    voltage = models.FloatField()
    current = models.FloatField()
    power_factor = models.FloatField()
    power = models.FloatField()
    status = models.BooleanField(default=False)

