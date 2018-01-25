from django.contrib.contenttypes.models import ContentType
from coin.models import Coin
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
)
class CoinReadSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = [
            'name',
            'ticker',
            'pair',
            'price',
            'btc_price',
        ]
