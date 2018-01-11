from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
)
User = get_user_model()

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
        ]
        extra_kwargs = {"password": {"write_only":True}}
