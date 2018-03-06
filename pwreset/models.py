# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class PasswordReset(models.Model):
    token = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    consumed = models.BooleanField(default=False)
