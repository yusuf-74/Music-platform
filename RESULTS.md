**_create some artists_**

```python
from artists.models import *
from albums.models import *
artist = Artist(stageName='ahmed metwally',socialLink='https://www.instagram.com/ahmed_metwally_74')
artist.save()
artist = Artist(stageName='yasser issa',socialLink='https://www.instagram.com/yasser_issa_74')
artist.save()
artist = Artist(stageName='yusuf ashour',socialLink='https://www.instagram.com/yusuf_ashour_74')
artist.save()
```

**_list down all artists_**

```python
artists = Artist.objects.all()
print(artists)
```

**<QuerySet [<Artist: ahmed metwally>, <Artist: yasser issa>, <Artist: yusuf ashour>]>**

<br />
<br />

**_list down all artists sorted by name_**

```python
print(Artist.objects.order_by('stageName'))
```

**<QuerySet [<Artist: ahmed metwally>, <Artist: yasser issa>, <Artist: yusuf ashour>]>**

<br />
<br />

**_list down all artists whose name starts with a_**

```python
artists = Artist.objects.filter(stageName__startswith='a')
print(artists)
```

**<QuerySet [<Artist: ahmed metwally>]>**

<br />
<br />

**_create some albums and assign them to any artists_**

```python
artist = Artist.objects.get(pk=1)
album1 = Album.objects.create(name = 'new life' , artist = artist , cost = 500.00 )
artist = Artist.objects.get(pk=2)
album1 = Album.objects.create(name = 'new life (same cost)' , artist = artist , cost = 500.00 )
artist = Artist.objects.get(pk=2)
album1 = Album.objects.create(name = 'bullet proof' , artist = artist , cost = 2500.00 )
artist = Artist.objects.get(pk=3)
album1 = Album.objects.create(name = 'under the influince' , artist = artist , cost = 1212.00 )
```

**_list down all albums_**

```python
albums = Album.objects.all()
print(albums)
```

**<QuerySet [<Album: new life>, <Album: new life (same cost)>,<Album: bullet proof>,<Album: under the infelunce>]>**

<br />
<br />

**_for each artist, list down all of his/her albums_**

```python
ahmed = Artist.objects.get(pk = 1)
print(ahmed.albums.all())
```

**<QuerySet [<Album: new life>]>**

<br />
<br />

**_list down all albums ordered by cost then by name (cost has the higher priority)_**

```python
albums = Album.objects.order_by('cost' , 'name')
print(albums)
```

**<QuerySet [<Album: new life>, <Album: new life (same cost)>, <Album: under the infelunce>, <Album: bullet proof>]>**
