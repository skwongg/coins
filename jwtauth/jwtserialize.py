
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from django.contrib.auth.models import User

class CoinsJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'
