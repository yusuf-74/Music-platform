from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin
    
admin.site.register(User,UserAdmin)

