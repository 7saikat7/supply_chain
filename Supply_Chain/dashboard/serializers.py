from rest_framework import serializers
from .models import ContactInfo , QueryType

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactInfo
		fields ='__all__'

class QueryTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = QueryType
		fields ='__all__'