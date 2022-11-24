from knox import views as knox_views
from .views import *
from django.urls import path
urlpatterns = [
     path('login/', LoginAPI.as_view(), name='knox_login'),
     path('register/', RegisterAPI.as_view(), name='knox_signup'),
     path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
