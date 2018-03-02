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
from rest_framework.authtoken.models import Token
from userprofile.serializers.create_user import UserCreateSerializer
from userprofile.serializers.login_user import UserLoginSerializer
from userprofile.serializers.update_user import UserUpdateSerializer
from rest_framework_jwt.utils import jwt_encode_handler
from jwtauth.custom_jwt import jwt_payload_handler

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        validated_data = request.data.get('user')
        serializer = UserCreateSerializer(data=validated_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response({'data':new_data}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request
        queryset = User.objects.get()


class UserTokenVerifyAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        if 'token_key' in self.kwargs:
            token_key = self.kwargs['token_key']
            conf_token = Token.objects.filter(key=token_key)
            if conf_token:
                confirmed_user = conf_token.first().user.userprofile
                if not confirmed_user.is_authenticated:
                    confirmed_user.is_authenticated = True
                    confirmed_user.save()
                return Response({'data': 'Success'}, status=HTTP_200_OK)
            else:
                return Response({'error': 'User not found'}, status=HTTP_400_BAD_REQUEST)
