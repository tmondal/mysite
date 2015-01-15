from django import forms
from .models import blogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = blogComment
        exclude = ["blogpost"]

