from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import *


def index(request):
    artists = Artist.objects.all()
    albums  = Album.objects.all()
    mydata = list(Artist.objects.all().values())
    i = 0
    for artist in artists:
        mydata[i]['albums'] = list(albums.filter(artist = artist).values())
        i+=1
    context = { 'artists' : mydata}
    return render(request , 'artists/artists-view.html' , context=context)

def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try: 
            form = ArtistForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'OK'})
            else :
                return JsonResponse({'status': 'validation error'})
            
        except:
            return JsonResponse({'status' : 'faild'})
    return render(request, 'artists/create-artist.html')