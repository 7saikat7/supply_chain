from django.db import models
from uuid import uuid4

class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")

class Producer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")
    address = models.CharField(max_length= 200 , default="NULL")
    city = models.CharField(max_length= 200 , default="NULL")
    state = models.CharField(max_length= 200 , default="NULL")
    pincode = models.CharField(max_length= 20 , default="NULL")
    email = models.EmailField(max_length=200 , unique=True)

class Receiver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")
    address = models.CharField(max_length= 200 , default="NULL")
    pincode = models.CharField(max_length= 20 , default="NULL")
    email = models.EmailField(max_length=200 , unique= True)
    city = models.CharField(max_length= 200 , default="NULL")
    state = models.CharField(max_length= 200 , default="NULL")

class ProductDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE , related_name='product_category')
    product_name =  models.CharField(max_length= 200 , default="NULL")
    delivery_address = models.CharField(max_length= 200 , default="NULL")
    pincode = models.CharField(max_length=20 , default = "NULL")
    city =  models.CharField(max_length= 200 , default="NULL")
    state =  models.CharField(max_length= 200 , default="NULL")
    region =  models.CharField(max_length= 200 , default="NULL")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE , related_name='producer_info')
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE , related_name='receiver_info')

# Create your models here.
