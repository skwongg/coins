# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from userprofile.mailtrap import send_mail

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=48, blank=True)
    is_authenticated = models.BooleanField(default=False)

    def send_auth_email(self, token):
        if self.is_authenticated:
            return
        else:
            send_mail

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
        token = Token.objects.create(user=instance)
        userprofile.send_auth_email()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
