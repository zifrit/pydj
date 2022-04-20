from django import forms
from .models import Comments


class EmailPostFrom(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.CharField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')
