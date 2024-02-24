from django.contrib import admin
from django.urls import path
from .views import index, register, submit_request, about

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('submit/', submit_request, name='submit_request'),
    path('about/', about, name='about')
]
