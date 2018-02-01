from django.contrib.contenttypes.models import ContentType
from hodlings.models import Hodling
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)
class HodlingReadSerializer(ModelSerializer):
    class Meta:
        model = Hodling
        fields = [
            'userprofile',
            'coin',
            'quantity',
        ]
