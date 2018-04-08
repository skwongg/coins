# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from coin.models import Coin
from coin.serializers.read_coins import CoinReadSerializer
from coin.serializers.search_coins import CoinSearchSerializer
from search.coinsearch import search
import json

class CoinReadAPIView(ListAPIView):
    queryset = Coin.objects.all()
    serializer_class=CoinReadSerializer


class CoinSearchAPIView(RetrieveAPIView):
    serializer_class=CoinSearchSerializer
    def get(self, request):
        ticker = request.query_params['q']
        return Response(search(ticker))
        if ticker:
            coin = Coin.objects.filter(ticker=ticker)
            if coin:
                coin = coin.first()
                serializer = CoinSearchSerializer(coin)
                return Response({"coin": serializer.data},status=HTTP_200_OK)

        return Response(json.dumps({'status': 404, 'message': 'Coin not found'}), status=HTTP_400_BAD_REQUEST)
