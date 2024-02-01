from django import forms
from django.core.validators import RegexValidator
from .models import Visitor

class VisitorForm(forms.ModelForm):
    mobile_number = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10}$', message='Enter a valid 10-digit mobile number.')]
    )

    class Meta:
        model = Visitor
        fields = ['name', 'address', 'mobile_number']

