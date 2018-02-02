from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from hodlings.models import Hodling
from coin.models import Coin
from hodlings.serializers.read import HodlingReadSerializer
from hodlings.serializers.create import HodlingCreateSerializer
import json


class HodlingReadAPIView(RetrieveAPIView):
    serializer_class=HodlingReadSerializer
    def get(self, request):
        hodls = Hodling.objects.filter(userprofile=request.user.userprofile)
        serializer = HodlingReadSerializer(hodls, many=True)
        return Response({"hodls":serializer.data}, status=HTTP_200_OK)


class HodlingCreateAPIView(CreateAPIView):
    serializer_class=HodlingCreateSerializer
    def create(self, request):
        hodler=request.user.userprofile
        coin=Coin.objects.get(id=request.POST['coin'])
        quantity=request.POST['quantity']
        hodln=Hodling.objects.filter(userprofile=hodler, coin=coin)
        if hodln:
            hodln=hodln[0]
            hodln.quantity=float(hodln.quantity) + float(quantity)
            hodln.save()
        else:
            hodln = Hodling.objects.create(userprofile=hodler, coin=coin, quantity=quantity)

        serializer=HodlingCreateSerializer(hodln)
        return Response({"hodls":serializer.data}, status=HTTP_200_OK)
