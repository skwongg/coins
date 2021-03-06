from django.contrib.contenttypes.models import ContentType
from coin.models import Coin
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
)
class CoinUpdateSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = [
            'name',
            'ticker',
            'price',
            'btc_price',
        ]
