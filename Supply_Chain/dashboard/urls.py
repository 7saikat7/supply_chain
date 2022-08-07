from django.contrib import admin
from django.urls import path
from dashboard import views

# from .views import  contact_list , contact_detail , contact_create , contact_update

urlpatterns = [
    path('Contact_Us/', views.contact_info, name='contact-info')
]
#     path('get_contacts/' , contact_list),
#     path('detail_contact/' , contact_detail),
#     path('create_contact/' , contact_create),
#     path('update_contact/' , contact_update),
 
