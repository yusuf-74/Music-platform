from django.contrib import admin
from .models import *
from .forms import *

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    
admin.site.register(User , UserAdmin)


