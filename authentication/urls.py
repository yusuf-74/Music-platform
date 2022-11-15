
from django.urls import path, include
from .views import *
urlpatterns = [
    # path('', index),
    path('login/', LoginView.as_view(),name='login'),
    path('register/' , RegisterView.as_view()),
]
