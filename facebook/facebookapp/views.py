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


def checklogin(request):
    try:
        username = request.POST.get('txt_username')
        password = request.POST.get('txt_password')
        context = {}
        LoginObj = UserData.objects.filter(userName=username).exists()
       
        if(LoginObj):
            LoginObj1 = UserData.objects.get(userName=username)

            if(LoginObj1.password == password):
                template = loader.get_template('home.html')

            else:
                template = loader.get_template('password_error.html')

        else:
            template = loader.get_template('username_error.html')

    except Exception as e:
        print(e)
    return HttpResponse(template.render(context, request))


def userRegistration(request):
    try:
        template=loader.get_template('index.html')
        context = {}
        v_email = request.POST.get('email')
        login_obg = UserData.objects.filter(userName=v_email).exists()
        if(login_obg==False):
            flag = 0
            v_firstname = request.POST.get('firstName')
            v_surename = request.POST.get('sureName')
            v_dob = request.POST.get('date')
            v_gender = request.POST.get('gender')
            v_password = request.POST.get('rpassword')
            login_obg1 = UserData(userName=v_email, password=v_password)
            login_obg1.save()
            if(login_obg1.id>0):
                flag +=1
                user_obg = UserDetails(firstName=v_firstname, sureName=v_surename, gender=v_gender, dob=v_dob, fklogin=login_obg1)
                user_obg.save()
                if(user_obg.id>0):
                    flag+=1
            if(flag==2):
                template = loader.get_template('home.html')
                      
    except Exception as r:
        print(r)
    return HttpResponse(template.render(context,request))