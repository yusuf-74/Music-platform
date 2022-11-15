from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout


class ArtistViewCreate(LoginRequiredMixin, View):
    login_url = 'login'
    # redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'artists/create-artist.html')

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)
        try:
            form = ArtistForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'OK'})
            else:
                return JsonResponse({'status': 'validation error'})
        except:
            return JsonResponse({'status': 'faild'})


class ArtistViewList(View):
    def get(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        albums = Album.objects.all()
        mydata = list(Artist.objects.all().values())
        i = 0
        for artist in artists:
            mydata[i]['albums'] = list(albums.filter(artist=artist).values())
            i += 1
        context = {'artists': mydata}
        return render(request, 'artists/artists-view.html', context=context)
