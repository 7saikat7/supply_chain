from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_seller = models.BooleanField(null=True, default=False)
    is_buyer = models.BooleanField(null=True, default=False)

    is_enterprise = models.BooleanField(null=True, default=False)
    is_business = models.BooleanField(null=True, default=False)
    is_employee = models.BooleanField(null=True, default=False)
    is_customer = models.BooleanField(null=True, default=False)

    email = models.EmailField(_('email'), unique=True)
    objects = UserManager()
