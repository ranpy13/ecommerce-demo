
from django import forms
from .models import review,blog

class ReviewForm(forms.ModelForm):
    class Meta:
        model=review
        fields=['comment','name','email',"website"]




class BlogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__' 
        exclude=('owner','slug',)