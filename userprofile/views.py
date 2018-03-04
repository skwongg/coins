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
from userprofile.serializers.update_user import UserUpdateSerializer
from userprofile.mailtrap import send_mail
from pwreset.models import PasswordReset
import hashlib
import os

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


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request
        queryset = User.objects.get()


class UserTokenVerifyAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        if ('token' in request.data) and request.data['token']:
            token_key = request.data['token']
            conf_token = Token.objects.filter(key=token_key)
            if conf_token:
                confirmed_user = conf_token.first().user.userprofile
                if not confirmed_user.is_authenticated:
                    confirmed_user.is_authenticated = True
                    confirmed_user.save()
                return Response({'data': 'Success'}, status=HTTP_200_OK)
        return Response({'error': 'User not found'}, status=HTTP_400_BAD_REQUEST)


class UserResetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        validated_data = request.data
        if 'email' not in request.data:
            return Response({}, status=HTTP_400_BAD_REQUEST)

        email=validated_data['email']
        token = hashlib.sha256(bytes((email + os.environ['SALT']), 'utf-8')).hexdigest()

        self.send_pwreset(email, token)
        pwr_token = PasswordReset.objects.get_or_create(email=email, token=token)
        # print(validated_data)
        return Response({}, status=HTTP_200_OK)



    def send_pwreset(self, email, token):
        subject = "Password reset instructions"
        body = """Follow these steps to reset your password. {0} \n If you did not request for your password to be reset, please ignore this email.""".format("http://127.0.0.1:3000/reset_password/{}".format(token))
        from_email = 'from@email.com'
        to_email = email

        send_mail(subject, body, from_email, to_email)
