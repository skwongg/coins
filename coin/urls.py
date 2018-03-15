from django.conf.urls import url
from django.contrib import admin


from coin.views import (
    CoinCreateAPIView,
    CoinUpdateAPIView,
    CoinReadAPIView,
    CoinSearchAPIView,
)

urlpatterns = [
    url(r'^create/$', CoinCreateAPIView.as_view(), name='create'),
    url(r'^edit/$', CoinUpdateAPIView.as_view(), name='update'),
    url(r'^search', CoinSearchAPIView.as_view(), name='search'),
    url(r'^$', CoinReadAPIView.as_view(), name='retrieve'),
]
