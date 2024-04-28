
from django.urls import path
from Auth_app_user import views

urlpatterns = [
    path("users/",views.user_request,name="users"),
    path('accept/<int:request_id>/', views.accept_request, name='accept_request'),
    path('reject/<int:request_id>/', views.reject_request, name='reject_request'),
    
    
]
