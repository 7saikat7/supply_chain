from django.db import models
from uuid import uuid4

class QueryType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")

class ContactInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")
    phone_no = models.CharField(max_length= 200 , default="NULL" , unique = False)
    email = models.EmailField(max_length=200 , unique=True)
    type_of_query = models.ForeignKey(QueryType, on_delete=models.CASCADE , related_name='query_type')
    description = models.CharField(max_length= 200 , default="NULL")

