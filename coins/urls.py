from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from coin import views
from rest_framework_jwt.views import obtain_jwt_token
from jwtauth.auth import CoinsJWTAPIView



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/v1/users/', include('userprofile.urls')),
    url(r'^api/v1/coins/', include('coin.urls')),
    url(r'^api/v1/hodls/', include('hodlings.urls')),
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^api/auth/', obtain_jwt_token)
    # url(r'^api/auth/', ObtainJSONWebToken.as_view(serializer_class=CoinsJWTSerializer)),
    url(r'^api/auth/', CoinsJWTAPIView.as_view()),
]
