1. Change all the current views you have to class based views, from now on we'll only be creating class based views



```python
   from django.views import View

   class ListAlbum(View):
    pass

```
<br/>
<br/>

2. Add a sign in page using which a user can provide their username and password to get authenticated

-  ***Registration Form***

<img src = './readme elements/register.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>

-  ***Login Form***  

<img src = './readme elements/login.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>


3. Allow unauthenticated users to access the endpoint https://localhost:8000/artists/, but only authenticated users can
access the creation form pages

```python
from django.contrib.auth.mixins import LoginRequiredMixin


class ArtistViewCreate(LoginRequiredMixin,View):
    login_url = 'login'

```

4. We received a requirement that each album must have at least one song. In the albums app, create a song model that
consists of:

-  A name (if no name is provided, the song's name defaults to the album name)
-  An image (required)
-  An image thumbnail with JPEG format (hint: use ImageKit )

```python

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Song(models.Model):
    name = models.CharField(
        max_length=150,
        default='New Song'
    )
    image = models.ImageField(upload_to='songs/%y/%m/%d')
    
    thumbnailImage = ImageSpecField(source='image',
    processors = [ResizeToFill(100, 50)],
    format = 'JPEG',
    options = {'quality': 60})
    
    album = models.ForeignKey(  Album,
                                on_delete=models.PROTECT,
                                related_name='songs')
    
    audioFile = models.FileField(upload_to= 'audio/%y/%m/%d')
    
    def __str__(self):
        return self.name
```

4. Setup your server to serve the uploaded media files, for example, I should be able to view a song's image by
accessing its url: http://127.0.0.1:8000/YOUR_MEDIA_PATH/image.jpg

-  settings.py

```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = 'media/'
```
-  urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/' , include('artists.urls')),
    path('albums/', include('albums.urls')),
    path('auth/' , include('authentication.urls')),
    
]+static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT )
```
