from django.urls import path
from django.urls.conf import include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
]