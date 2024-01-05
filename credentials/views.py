from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email = request.POST['email']
        password=request.POST['pwd']
        cpassword=request.POST['cpwd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email alredy registered")
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
        else:
            messages.info(request,"password not matches")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')