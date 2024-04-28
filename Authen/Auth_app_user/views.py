import django.contrib
from django.shortcuts import render,redirect
from Auth_app_user.models import Request_details
from django.contrib import messages
#sending email
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def user_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id=request.POST.get("id")
            name=request.POST.get("name")
            email=request.POST.get("email")
            number=request.POST.get("number")
            myuser=Request_details(id=id,name=name,email=email,number=number,status="Pending")
            myuser.save()
            messages.success(request,"Successfully Submitted")
        return render(request,"users.html")
    else:
        return render(request,"login.html")
        

def accept_request(request, request_id):
    if request.user.is_authenticated:
        request_detail = Request_details.objects.get(id=request_id)
        request_detail.status = "Accepted"
        request_detail.save()
         # Send email to the user
        from_email = settings.EMAIL_HOST_USER
        to_email = request_detail.email
        subject = 'Request Accepted'
        message = 'Your request has been approved.'
        try:
            mail.send_mail(subject, message, from_email, [to_email])
            messages.success(request, "Request accepted successfully and email sent.")
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")

        AllPosts=Request_details.objects.all()
        context={"AllPosts":AllPosts}
        return render(request,"adminpanel.html",context)
    else:
        return render(request,"login.html")

def reject_request(request, request_id):
    if request.user.is_authenticated:
        request_detail = Request_details.objects.get(id=request_id)
        request_detail.status = "Rejected"
        request_detail.save()
        # Send email to the user
        from_email = settings.EMAIL_HOST_USER
        to_email = request_detail.email
        subject = 'Request Accepted'
        message = 'Your request has been Rejected.'
        try:
            mail.send_mail(subject, message, from_email, [to_email])
            messages.success(request, "Request Rejected successfully and email sent.")
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}") 
        AllPosts=Request_details.objects.all()
        context={"AllPosts":AllPosts}
        return render(request,"adminpanel.html",context)
    else:
        return render(request,"login.html")
    