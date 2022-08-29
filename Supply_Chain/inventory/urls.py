from django.urls import path

from inventory.views import *
from inventory.models import *

urlpatterns = [
    path('add-delivery-details/', add_delivery_details),
]