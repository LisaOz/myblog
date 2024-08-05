from django import forms
from .models import Comment

"""
EmailPostForm inherits from the base Form class
"""

class EmailPostForm(forms.Form): 
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

"""
Create dynamic form for comments using the ModelForm
""" 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

"""
Create form for the search
"""

class SearchForm(forms.Form):
    query = forms.CharField()

