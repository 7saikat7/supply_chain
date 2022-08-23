from django.urls import path
from payment import views

urlpatterns = [
    path('pricing', views.pricing, name='pricing'),
]