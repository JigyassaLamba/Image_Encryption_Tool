from django import forms
from .models import ImageEncrytion

class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageEncrytion
        fields=("text","image")