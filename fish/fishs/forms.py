from django import forms
from .models import reg 

class regform(forms.ModelForm):
    class Meta:
        model=reg
        fields='__all__'
        labels={
            'email':'',
            'image':'',
        }