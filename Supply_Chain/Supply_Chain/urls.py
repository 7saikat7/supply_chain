from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('dashboard/', include('dashboard.urls') ),
    path('authentication/', include('authentication.urls') ),
    path('payment/', include('payment.urls') ),
]
