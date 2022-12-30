from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from users.serializers import *
from knox.auth import TokenAuthentication
from rest_framework.status import *


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(data={
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, status=HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        return Response(data={
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        },status=HTTP_202_ACCEPTED)