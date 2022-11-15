from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View
import json
from django.http import JsonResponse

class LoginView(View):
    def get(self,request,*args, **kwargs):
        return render(request , 'auth/log-in.html')
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = authenticate(username = data['userName'] , password = data['password'] )
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'OK'})
        else :
            return JsonResponse({'status': {'username': ['invalid username or password !']}})
    

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'auth/register.html')
    
    def post(self,request,*args, **kwargs):
        data = json.loads(request.body)
        if data['pass1'] == data['pass2']:
            try:
                if User.objects.get(username=data['userName']):
                    return JsonResponse({'status': 'exist'})
            except:
                try:
                    user = User(username=data['userName'], password=data['pass1'],
                                first_name=data['firstName'], last_name=data['lastName'])
                    user.save()
                    login(request,user)
                    return JsonResponse({'status' : 'OK'})
                except:
                    return JsonResponse({'status' : 'faild'})
        return JsonResponse({'status' : 'password'})
        
