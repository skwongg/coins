from django.conf.urls import url
from django.contrib import admin

from userprofile.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserTokenVerifyAPIView,
    UserResetPasswordAPIView,
)

urlpatterns = [
    url(r'^update/$', UserUpdateAPIView.as_view(), name='update'),
    url(r'^register$', UserCreateAPIView.as_view(), name='register'),
    url(r'^verify$', UserTokenVerifyAPIView.as_view(), name='verify'),
    url(r'^resetpw$', UserResetPasswordAPIView.as_view(), name='resetpw'),
]
