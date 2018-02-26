# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, UpdateAPIView)
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from userprofile.serializers.create_user import UserCreateSerializer
from userprofile.serializers.login_user import UserLoginSerializer
from userprofile.serializers.update_user import UserUpdateSerializer

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    # queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserCreateSerializer(data)
        print("* " * 100)
        print(serializer.data)
        return Response(serializer.data, status=HTTP_200_OK)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request
        queryset=User.objects.get()
