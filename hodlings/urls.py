from django.conf.urls import url
from django.contrib import admin


from hodlings.views import (
    HodlingReadAPIView,
)

urlpatterns = [
    url(r'^$', HodlingReadAPIView.as_view(), name='read'),
]
