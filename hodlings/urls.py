from django.conf.urls import url
from django.contrib import admin


from hodlings.views import (
    HodlingReadAPIView,
    HodlingCreateAPIView
)

urlpatterns = [
    url(r'^create/$', HodlingCreateAPIView.as_view(), name='create'),
    url(r'^$', HodlingReadAPIView.as_view(), name='read'),
]
