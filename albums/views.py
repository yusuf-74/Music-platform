from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from .serializers import *
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListAlbum(APIView):
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
