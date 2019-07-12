# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import *
# Create your views here.apt


def myIndex(request):
    print("get into index")
    template = loader.get_template('index.html')
    context = {"message": "welcome this is my first django application"}
    return HttpResponse(template.render(context, request))


#def home(request):
#    print("get into index")
#    template = loader.get_template('home.html')
#    context = {"message": "welcome this is my first django application"}
#    return HttpResponse(template.render(context, request))


def checklogin(request):
   username = request.POST.get('txt_username')
   password = request.POST.get('txt_password')
   LoginObj = UserData.objects.filter(userName=username, password=password).exists()
   if(LoginObj):
      template = loader.get_template('home.html')
      return HttpResponse(template.render({}, request))
   else:
      return HttpResponse('login failed')