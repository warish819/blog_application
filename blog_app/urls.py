from django.urls import path
from .import views


urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('about/',views.about,name='about'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('blog_dashboard/',views.blog_dashboard,name='blog_dashboard')
    
    
]