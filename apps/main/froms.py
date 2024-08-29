from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control',
                                           'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control',
                                             'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control',
                                              'placeholder': 'Phone'}),
            'message': forms.Textarea(attrs={'class':'form-control',
                                             'placeholder': 'Your Message'}),
        }










