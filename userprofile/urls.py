from django.conf.urls import url
from django.contrib import admin

from userprofile.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserLoginAPIView,
)

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^update/$', UserUpdateAPIView.as_view(), name='update'),
]
