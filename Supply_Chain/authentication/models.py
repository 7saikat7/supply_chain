from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    is_seller = models.BooleanField(null=True, default=False)
    is_buyer = models.BooleanField(null=True, default=False)

    is_enterprise = models.BooleanField(null=True, default=False)
    is_business = models.BooleanField(null=True, default=False)
    is_employee = models.BooleanField(null=True, default=False)
    is_customer = models.BooleanField(null=True, default=False)

    objects = UserManager()