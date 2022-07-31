from django import views
from django.contrib import admin
from django.shortcuts import render
from django.urls import URLPattern, path
from django.urls.conf import include
from . import views

app_name='home'

urlpatterns = [
    path('',views.home,name='home'),
]