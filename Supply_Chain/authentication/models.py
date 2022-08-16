from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    is_seller = models.BooleanField(null=True, default=False)
    is_buyer = models.BooleanField(null=True, default=False)

    is_enterprise = models.BooleanField(null=True, default=False)
    is_business = models.BooleanField(null=True, default=False)
    is_small = models.BooleanField(null=True, default=False)
    is_nano = models.BooleanField(null=True, default=False)

    is_employee = models.BooleanField(null=True, default=False)
    is_customer = models.BooleanField(null=True, default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []