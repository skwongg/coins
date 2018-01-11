from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    EmailField,
)

from coin.models import Coin


class CoinCreateSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = [
            'name',
            'ticker',
            'price',
            'btc_price',
        ]

    def validate(self, data):
        return data #TODO: build validation logic here

    def create(self, validated_data):
        return validated_data #TODO: build this validation
