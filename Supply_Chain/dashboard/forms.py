from django.forms import ModelForm
from .models import ContactInfo

class Form(ModelForm):
    class Meta:
        model = ContactInfo
        fields = "__all__"
