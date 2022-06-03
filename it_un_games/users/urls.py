from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register', name='register'),
    path('login', name='login')
]