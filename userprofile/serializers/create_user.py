from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    EmailField,
)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email_conf = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email_conf',
            'password',
        ]
        extra_kwargs = {"password": {"write_only":True}}

    def validate(self, data):
        email = data.get("email")
        email_conf = data.get("email_conf")
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This email has already been taken.")
        if email != email_conf:
            raise ValidationError("Emails must match")
        return data

    def create(self, validated_data):
        user_obj = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return validated_data
