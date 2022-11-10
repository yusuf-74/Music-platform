1. Instead of having an explicit created_at field in the Album model, inherit from TimeStampedModel


```python
    class Album(TimeStampedModel):
```
<br/>
<br/>

2. Create a form that allows a user to create an artist (it should be available at http://localhost:8000/artists/create)

<img src = './readme elements/artist_form.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>

3. Create a form that allows a user to create an album (it should be available at https://localhost:8000/albums/create)

<img src = './readme elements/albums_form.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>

  - (bonus) can you use a user friendly date/time input widget for the release datetime field instead of a plain text
input field?

```html
<input
    type="datetime-local"
    id="releasing"
    class="form-control form-control-lg"
    style = 'border : 1px solid black'
/>
```

4. For both forms, when the validation fails, the user should see errors displayed in red text on top of the form letting the
user know what the error is

```javascript
    if (response.status === 'OK')
        {
            status.innerHTML = "created successfully"
            status.style = 'color : green;'
        }
    else 
        {
            status.innerHTML = response.massage
            status.style = 'color : red;'
        }
```

5. Create a template view that lists all the albums grouped by each artist 
(it should be available at https://localhost:8000/artists/)

<img src = './readme elements/artists_list.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>

- Fetch the queryset above in an optimized manner

```python
artists = Artist.objects.all()
albums  = Album.objects.all()
mydata = list(Artist.objects.all().values())
i = 0
for artist in artists:
    mydata[i]['albums'] = list(albums.filter(artist = artist).values())
    i+=1
context = { 'artists' : mydata}
return render(request , 'artists/artists-view.html' , context=context)
```