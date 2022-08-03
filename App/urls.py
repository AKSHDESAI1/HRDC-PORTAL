
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.login1, name='login'),
    path('home/', views.home1, name='home1'),
    path('logout/', views.logout1, name='logout'),
]
