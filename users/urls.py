from django.urls import path, include
from .views import *
from knox import views as knox_views ,urls
urlpatterns = [    
    path('<int:pk>/', GetAPI.as_view()),
]
