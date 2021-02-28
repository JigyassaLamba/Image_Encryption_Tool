from django import forms
from .models import ImageDecryption

class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageDecryption
        fields=("text","image")