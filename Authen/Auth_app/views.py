from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from Auth_app_user.models import Request_details

# Create your views here.
def Signin(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            if password !=cpassword:
                messages.error(request,"password doesnot matched")
                return redirect("/")
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect("/")
            if User.objects.filter(email=email).exists():
                messages.error(request,"email already exists")
                return redirect("/")
            myuser=User.objects.create_user(username=username,email=email,password=password)
            myuser.save()
            messages.success(request,"User Signin Successfully")
            return redirect("/login")
        return render(request,"signup.html")
    else:
        return render(request,"login.html")
def Adminsign(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            if password !=cpassword:
                messages.error(request,"password doesnot matched")
                return redirect("/")
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect("/")
            if User.objects.filter(email=email).exists():
                messages.error(request,"email already exists")
                return redirect("/")
            myuser=User.objects.create_user(username=username,email=email,password=password)
            myuser.is_staff = True
            myuser.is_superuser =True
            myuser.save()
            messages.success(request,"Admin Signin Successfully")
            return redirect("/login")
        return render(request,"signup.html")
    else:
        return render(request,"login.html")

def admin_panel(request):
    if request.user.is_authenticated:
        AllPosts=Request_details.objects.all()
        context={"AllPosts":AllPosts}
        return render(request,"adminpanel.html",context)
    else:
        return render(request,"login.html")

def handleLogin(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            myuser=authenticate(username=username,password=password)
            if myuser is not None:
                login(request,myuser)
                if myuser.is_superuser == True:
                    AllPosts=Request_details.objects.all()
                    context={"AllPosts":AllPosts}
                    return render(request,"adminpanel.html",context)
                else:
                    return redirect("/users")
            else:
                messages.error(request,'Invalid Credentials')
                return redirect("/login")
        return render(request,"login.html")
    else:
        return render(request,"login.html")