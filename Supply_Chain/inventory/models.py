from django.db import models
from uuid import uuid4

class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")

class ProductSubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE , related_name='category')

class SellingPlatform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")

class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")
    address = models.CharField(max_length= 200 , default="NULL")
    city = models.CharField(max_length= 200 , default="NULL")
    state = models.CharField(max_length= 200 , default="NULL")
    pincode = models.CharField(max_length= 20 , default="NULL")
    email = models.EmailField(max_length=200 , unique=True)
    file = models.FileField(upload_to='', max_length=200, blank=True)
    selling_through = models.ForeignKey(SellingPlatform, on_delete=models.CASCADE , related_name='selling_platform')

class ProductDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE , related_name='product_category')
    product_name =  models.CharField(max_length= 200 , default="NULL")
    delivery_address = models.CharField(max_length= 200 , default="NULL")
    pincode = models.CharField(max_length=20 , default = "NULL")
    city =  models.CharField(max_length= 200 , default="NULL")
    state =  models.CharField(max_length= 200 , default="NULL")
    region =  models.CharField(max_length= 200 , default="NULL")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE , related_name='seller_info')

class Receiver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")
    address = models.CharField(max_length= 200 , default="NULL")
    contact_number = models.CharField(max_length=200, blank=True)
    alternate_contact_number = models.CharField(max_length=200, blank=True)
    pincode = models.CharField(max_length= 20 , default="NULL")
    email = models.EmailField(max_length=200 , unique= True)
    city = models.CharField(max_length= 200 , default="NULL")
    state = models.CharField(max_length= 200 , default="NULL")
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE , related_name='product_info')

# Create your models here.
