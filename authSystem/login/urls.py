from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('',views.login_view, name= 'index'),
    path('home',views.index, name='home'),
    path('register',views.register_view, name = 'register'),
    path('logout', views.logout_view, name= 'logout')
]
