from django.conf.urls import url
from django.contrib import admin

from userprofile.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserLoginAPIView,
    UserTokenVerifyAPIView,
)

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^update/$', UserUpdateAPIView.as_view(), name='update'),
    url(r'^register$', UserCreateAPIView.as_view(), name='register'),
    url(r'^verify/(?P<token_key>[\w.-]+)/', UserTokenVerifyAPIView.as_view(), name='verify'),
]
