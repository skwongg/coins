# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Coin(models.Model):
    name=models.CharField(max_length=255)
    ticker=models.CharField(max_length=10)
    pair=models.CharField(max_length=10)
    price=models.DecimalField(max_digits=15, decimal_places=8)
    btc_price=models.DecimalField(max_digits=15, decimal_places=8)
    icon_url=models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table="coins"
