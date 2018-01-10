# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Coin(models.Model):
    name=models.CharField(max_length=255)
    ticker=models.CharField(max_length=10)
    price=models.DecimalField()
    btc_price=models.DecimalField()
