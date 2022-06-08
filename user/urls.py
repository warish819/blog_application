from django.urls import path
from .import views

urlpatterns = [
    path('',views.registration,name='registration'),
    path('login/',views.login_request,name='login'),
    path('confirmation/',views.confirmation,name='confirmation')
  
    
]