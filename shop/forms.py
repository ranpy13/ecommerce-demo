from django import forms
from .models import Color, review ,clothe

class ReviewForm(forms.ModelForm):
    class Meta:
        model=review
        fields=['Your_review','name','email']


class ClotheForm(forms.ModelForm):
    class Meta:
        model=clothe
        fields='__all__' 
        exclude=('owner','slug',)


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = "__all__"
        widgets = {
            'code' : forms.TextInput(attrs={'type': 'color'})
        }