from rest_framework import serializers
from .models import ContactInfo

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactInfo
		fields ='__all__'