from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from .serializers import *
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated , AllowAny
from .filters import AlbumFilter

class ListAlbum(generics.ListAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = Album.objects.all()
    filterset_class = AlbumFilter
    serializer_class = AlbumSerializer



class CreateAlbum(generics.CreateAPIView):
    def post(self, request):
        data = request.data
        user = request.user
        try:
            data ['artist'] = Artist.objects.get(user=user).pk
        except:
            return Response("user is not registered as artist" , status=status.HTTP_403_FORBIDDEN)
        
        serializer = CreateAlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
