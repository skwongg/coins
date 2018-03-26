# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from coin.models import Coin
from coin.serializers.create_coin import CoinCreateSerializer
from coin.serializers.update_coin import CoinUpdateSerializer
from coin.serializers.read_coins import CoinReadSerializer
from coin.serializers.search_coins import CoinSearchSerializer
from search.coinsearch import search
import json

class CoinCreateAPIView(CreateAPIView):
    serializer_class=CoinCreateSerializer
    queryset=Coin.objects.all()

class CoinUpdateAPIView(UpdateAPIView):
    serializer_class=CoinUpdateSerializer
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):
        if self.validate_req(request):
            #TODO:check if Coin.objects.filter(coinparams) exist, create if not
            return Response(json.dumps({'abc':'xyz'}), status=HTTP_200_OK)
        else:
            #case of missing attribute that can not be generated
            return json.dumps({'abc':'xyz'})

    def validate_req(self, request):
        if ('price' in request.POST) and ('name' in request.POST) and ('ticker' in request.POST) and ('btc_price' in request.POST):
            attrs = ['price','name','ticker','btc_price']
            for attr in attrs:
                if request.POST[attr]:
                    continue
                else:
                    return False
            return True

class CoinReadAPIView(RetrieveAPIView):
    serializer_class=CoinReadSerializer
    def get(self, request):
        coins = Coin.objects.all()
        serializer = CoinReadSerializer(coins, many=True)
        return Response({"coins":serializer.data}, status=HTTP_200_OK)

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
