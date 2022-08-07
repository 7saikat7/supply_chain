from django.db import models
from uuid import uuid4

class QueryType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200 , default="NULL")

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length= 200)
    company_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length= 200, unique = False)
    email = models.EmailField(max_length=200 , unique=True)
    type_of_query = models.ForeignKey(QueryType, on_delete=models.CASCADE , related_name='query_type')
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name+"-"+self.company_name+"-"+phone_no

