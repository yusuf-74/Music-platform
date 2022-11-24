from rest_framework import generics , permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from knox.auth import TokenAuthentication
from django.http import Http404
from rest_framework import status

class GetAPI(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, pk , *args, **kwargs):
        try:
            user = User.objects.get(id=pk)
        except:
            raise Http404("not found")
        if request.user == user:
            return Response(UserSerializer(user).data)
        else :
            return Response("Not allowed", status=status.HTTP_403_FORBIDDEN)
    
    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(id=pk)
        except:
            raise Http404("not found")
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self , request,pk , *args, **kwargs):
        try:
            user = User.objects.get(id=pk)
        except:
            raise Http404("not found")
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
