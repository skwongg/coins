from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from coin import views
from jwtauth.auth import CoinsJWTAPIView



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/v1/users/', include('userprofile.urls')),
    url(r'^api/v1/coins/', include('coin.urls')),
    url(r'^api/v1/hodls/', include('hodlings.urls')),
    url(r'^api/v1/auth/', CoinsJWTAPIView.as_view()),
]
