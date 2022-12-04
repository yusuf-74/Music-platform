
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',ListAlbum.as_view() ),
    path('create/', CreateAlbum.as_view()),
]
