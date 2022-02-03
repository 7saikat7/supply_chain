from rest_framework import serializers
from .models import ContactInfo , QueryType

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactInfo
		exclude = ('id', )
