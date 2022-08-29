from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.RegisterForm, name='register'),
    path('login/', views.LoginForm, name='login'),
]
