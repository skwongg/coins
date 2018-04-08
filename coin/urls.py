from django.conf.urls import url
from django.contrib import admin


from coin.views import (
    CoinReadAPIView,
    CoinSearchAPIView,
)

urlpatterns = [
    url(r'^search', CoinSearchAPIView.as_view(), name='search'),
    url(r'^$', CoinReadAPIView.as_view(), name='retrieve'),
]
