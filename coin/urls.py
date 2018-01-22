from django.conf.urls import url
from django.contrib import admin


from coin.views import (
    CoinCreateAPIView,
    CoinUpdateAPIView,
    CoinReadAPIView,
)

urlpatterns = [
    url(r'^create/$', CoinCreateAPIView.as_view(), name='create'),
    url(r'^edit/$', CoinUpdateAPIView.as_view(), name='update'),
    url(r'^all/$', CoinReadAPIView.as_view(), name='retrieve'),
]
