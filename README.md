1.Add a boolean field to the album model that will help us represent whether an album is approved by an admin or not

   - tip: follow the convention for boolean field names
   - hint: what's the suitable default value for this field, ( ```True``` or ```False``` )?

```python
    isApproved = models.BooleanField(default = False , verbose_name = 'Approved')
```
<br/>
<br/>

2.Add all models you have so far to django admin

- Albums

```python
from django.contrib import admin
from .models import *
from .forms import AlbumForm

admin.site.register(Album, AlbumAdmin, form=AlbumForm)
```
- Artists

```python
from django.contrib import admin
from .models import *

admin.site.register(Artist, ArtistAdmin)
```
3.The admin shouldn't be able to modify the creation time field on the album 

```python
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creationDateTime',) <----
    list_display = ('name', "creationDateTime",
                    "releaseDateTime", "cost", "isApproved", "artist")
    fields = ['name', "artist", "creationDateTime",
                "releaseDateTime", "cost", "isApproved"]
```

4. Add a help text that would show up under the previously mentioned boolean field on the django admin form, it should
state:

```python
from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    isApproved = forms.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")

    class Meta:
        model = Album
        fields ='__all__'

```
5. When viewing the list of artists, there must be a column to show the number of approved albums for each artist

- in models.py
```python
@property
def Approved_Albums(self):
    return str(len(self.albums.filter(isApproved=True)))
    
```

- at admin.py
```python
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('Approved_Albums',)
    list_display = ('stageName', 'socialLink', 'Approved_Albums')
    fields = ['stageName', 'socialLink', 'Approved_Albums']

```