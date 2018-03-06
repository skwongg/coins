from rest_framework.generics import (CreateAPIView, UpdateAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import serializers
from rest_framework_jwt.utils import jwt_encode_handler
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from jwtauth.jwtserialize import CoinsJWTSerializer
from jwtauth.custom_jwt import jwt_payload_handler
import json

class CoinsJWTAPIView(APIView):
    serializer_class=CoinsJWTSerializer
    renderer_classes=[JSONRenderer,]

    def post(self, request, format=None):
        token_obj = self.validate(request.data['credentials'])
        return Response(json.dumps(token_obj), status=HTTP_200_OK)


    def validate(self, attrs):
        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("email")).first() or User.objects.filter(username=attrs.get("username_or_email")).first()
        if user_obj is not None:
            credentials = {
            'username':user_obj.username,
            'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = ('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)
                    return {
                        'token': jwt_encode_handler(payload),
                        'email': user.email,
                        'confirmed': user.userprofile.is_authenticated
                    }
                else:
                    msg = ('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = ('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = ('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)
