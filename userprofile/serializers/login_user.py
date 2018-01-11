from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ValidationError,
)

User = get_user_model()

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username=CharField(allow_blank=True, required=False)
    email= EmailField(label='Email Address', allow_blank=True, required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password": {"write_only":True}}

    def validate(self, data):
        ###refactor
        user_obj = None
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        if not email or not username:
            raise ValidationError("Username or email required.")
        else:
            user = User.objects.filter(email=email) | User.objects.filter(username=username, email__isnull=False)
            if user.exists() and user.count() == 1:
                user_obj = user[0]
                if not user_obj.check_password(password):
                    raise ValidationError("Incorrect credentials, please try again.")

            else:
                raise ValidationError("Username/email not valid.")

        data["token"] = "SOME RANDOM TOKEN"
        return data
