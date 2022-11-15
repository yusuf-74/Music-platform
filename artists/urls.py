
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ArtistViewList.as_view()),
    path('create/', ArtistViewCreate.as_view(),name = 'create'),
]
