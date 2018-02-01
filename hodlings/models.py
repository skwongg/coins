# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from coin.models import Coin
from userprofile.models import UserProfile

class Hodling(models.Model):
    userprofile=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    coin=models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=40, decimal_places=8)

    def __unicode__(self):
        return "{0} {1}".format(self.quantity, self.coin.name)

    class Meta:
        db_table='hodlings'
