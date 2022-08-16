from django import forms
from .models import Seller, Receiver

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('pincode',)

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ('pincode',)
