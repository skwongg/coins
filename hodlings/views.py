from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from hodlings.models import Hodling
from hodlings.serializers.read import HodlingReadSerializer
import json


class HodlingReadAPIView(RetrieveAPIView):
    serializer_class=HodlingReadSerializer
    def get(self, request):
        print("*" * 100)
        print(request.GET)
        hodls = Hodling.objects.filter(userprofile=request.user.userprofile)
        serializer = HodlingReadSerializer(hodls, many=True)
        return Response({"hodls":serializer.data}, status=HTTP_200_OK)
