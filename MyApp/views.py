from django.core.mail import send_mail
from django.http import Http404
from CodeNicely1 import settings as em
from django.http import HttpResponse
from django.http import HttpRequest
from random import randint
from django.shortcuts import render
from .models import *

def login(request):
    rec = UpdateOTP.objects.all()
    return render(request,'login.html',{'data':rec})
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
        data = Registration.objects.filter(mobile=mobile)
        n = 6
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        otp = randint(range_start, range_end)
        return render(request,'emailpage.html',context={'rec':data,'otp':otp})

    else:
        return render(request,'registration.html',{'status':"Registration Failed...!"})

#mail process store data in database
def mail_process(request):
    otpdata = request.POST.get('otp')
    mobile = request.POST.get('otp_mobile')
    to_gmail = request.POST.get('otp_email','')
    rec = UpdateOTP.objects.filter(otp_mobile=mobile)
    send_mail("Otp Data",otpdata,em.EMAIL_HOST_USER,[to_gmail],fail_silently=False)
    request.session['session_otp']=otpdata
    if not rec:
        uotp = UpdateOTP(otp_mobile=mobile,otp=otpdata)
        uotp.save()
    else:
        pass
    return render(request,'login.html')

#Resend Otp
def resend_otp(request):
    mobile = request.POST.get('re_mobile')
    otp = request.POST.get('re_otp')
    to_gmail = request.POST.get('re_email')
    UpdateOTP.objects.filter(otp_mobile=mobile).update(otp=otp)
    send_mail("Otp Data", otp, em.EMAIL_HOST_USER, [to_gmail], fail_silently=False)
    request.session['session_otp']=otp
    return render(request,'login.html')

#  generate Rendom Number
def randomDigit(request):
    n = 6
    range_start = 10**(n-1)
    range_end = (10**n)-1
    otp = randint(range_start,range_end)
    return render(request,'info.html',{'otp':otp})
#email page
def emailpage(request):
    pass

def info(request):
    send_mail('testmail',
                'hello friend',
              'gyangee.20@gmail.com',
              ['gyanjha.20@gmail.com'],
              fail_silently=False)
    return render(request,'info.html')



    #login to server
def user_login(request):
    mobile = request.POST.get("mobile")
    password = request.POST.get("password")
    status ="Active"
    otp1 = request.POST.get("otp")
    #otpdata = request.POST.get("otpdata")
    #print(otpdata)
    #rec1 = UpdateOTP.objects.filter(otp_mobile=mobile)

    if otp1 == 12345:
    #if(otp == otp1):
        Registration.objects.filter(mobile=mobile).update(status=status)
        reg = Registration.objects.filter(mobile=mobile,password=password)
        if not reg:
            return render(request,'login.html',{'status':"Wrong ID and Password...!"})
        else:
            return render(request,'dashbord.html',context={'data':reg})


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
