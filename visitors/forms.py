from django import forms
from django.core.validators import RegexValidator
from .models import Visitor


class VisitorForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^\+?[\d\s\-\(\)]+$',
        message='Please enter a valid phone number.'
    )
    
    phone_number = forms.CharField(
        max_length=20,
        validators=[phone_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 (555) 123-4567'
        })
    )
    
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        })
    )
    
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'City, State/Country'
        })
    )

    class Meta:
        model = Visitor
        fields = ['name', 'phone_number', 'email', 'location']
