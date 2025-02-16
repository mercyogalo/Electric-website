from django import forms
from . models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_first_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'First Name'}), required=True)
    shipping_last_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Last Name'}), required=True)
    shipping_email=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Email '}), required=True)
    shipping_phone=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Phone'}), required=True)
    shipping_address1=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Address 1'}), required=True)
    shipping_address2=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Address 2'}), required=True)
    shipping_city=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'City'}), required=True)
    shipping_zipcode=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Zip Code'}), required=False)
    shipping_country=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-group col-md-6', 'placeholder':'Country'}), required=False)
    
    
    class  Meta:
        model=ShippingAddress
        fields=['shipping_first_name','shipping_last_name','shipping_email','shipping_phone','shipping_address1','shipping_address2','shipping_city','shipping_zipcode','shipping_country']
        
        exclude=['user',]