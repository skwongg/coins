from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_encode_handler
from jwtauth.custom_jwt import jwt_payload_handler
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    token = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'token',
            'password',
        ]
        extra_kwargs = {"password": {"write_only":True}}

    def get_token(self, obj):
        return jwt_encode_handler(jwt_payload_handler(User.objects.get(id=obj.id)))

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        user.token = jwt_encode_handler(jwt_payload_handler(user))
        return user

    def validate(self, data):
        email = data.get("email")
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This email has already been taken.")
        return data
