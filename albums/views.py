from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import *
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data['stageName'])
        try:
            target = Artist.objects.get(stageName = data['stageName'])
            form = AlbumForm(data)
            if form.is_valid():
                album = form.save(commit = False)
                album.artist = target
                album.save()
                return JsonResponse({'status': 'OK'})
            else:
                return JsonResponse({'status': 'validation error'})      
        except:
            return JsonResponse({'status': 'faild'})
    return render(request, 'albums/create-album.html')