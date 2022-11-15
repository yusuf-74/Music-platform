from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

class ListAlbum(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,*args, **kwargs):
        return render(request,  'albums/create-album.html')
    
    
    def post(self,request):
        data = json.loads(request.body)
        try:
            target = Artist.objects.get(stageName=data['stageName'])
            form = AlbumForm(data)
            if form.is_valid():
                album = form.save(commit=False)
                album.artist = target
                album.save()
                return JsonResponse({'status': 'OK'})
            else:
                return JsonResponse({'status': form.errors})
        except:
            return JsonResponse({'status': {'Stage Name' : ['No such artist']}})
        

