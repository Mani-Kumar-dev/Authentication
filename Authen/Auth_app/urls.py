
from django.urls import path
from Auth_app import views

urlpatterns = [
    path("user_sign",views.Signin,name="signin"),
    path("login/",views.handleLogin,name="login"),
    path("admin_panel/",views.admin_panel,name="admin_panel"),
    path("admin_sign/",views.Adminsign,name="adminsign"),
    
    
]
