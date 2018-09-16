from django.core.mail import send_mail
from django.http import Http404
from CodeNicely1 import settings as em
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request ,'registration.html')
def datastore(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        password = request.POST.get('pwd1')
        status = "panding"
        reg = Registration(name=name,email=email,mobile=mobile,dob=dob,password=password,status=status)
        reg.save()
        return render(request,'registration.html',{'status':'Registration Success...!'})

    else:
        return render(request,'registration.html',{'status':"Registration Failed...!"})

def info(request):
    send_mail('testmail',
              'Test Mail From Class',
              'gyangee.20@gmail.com',
              ['gyanjha.20@gmail.com'],
              fail_silently=False)
    return render(request,'info.html')



    #login to server
def user_login(request):
    mobile = request.POST.get("mobile")
    password = request.POST.get("password")
    status ="Active"
    otp = request.POST.get("otp")
    if otp == "1234":
    #if(otpdata.mob == otp):
        Registration.objects.filter(mobile=mobile).update(status=status)
        reg = Registration.objects.filter(mobile=mobile,password=password)
        if not reg:
            return render(request,'login.html',{'status':"Wrong ID and Password...!"})
        else:
            return render(request,'dashbord.html',{'data':reg})


    else:
        return render(request,'otp.html',{"status":'Wrong OTP...!'})



def update_profile(request):
    mobile = request.POST.get("mobile")
    name = request.POST.get("name")
    email = request.POST.get("email")
    dob =request.POST.get("dob")
    password = request.POST.get("password")
    Registration.objects.filter(mobile=mobile).update(name=name,email=email,dob=dob,password=password)
    return render(request,'dashbord.html',{'status':"Upsate Profile...!"})
