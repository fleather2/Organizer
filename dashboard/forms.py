from django import forms
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

class IdeaForm(forms.Form):

    category = forms.CharField(label='category', max_length=100)
    content = forms.CharField(label='content', widget=forms.Textarea)

class TodoForm(forms.Form):

    category = forms.CharField(label='category', max_length=100, required=False)
    content = forms.CharField(label='content', widget=forms.Textarea)
    dateDue = forms.DateField(label='dateDue', widget=forms.SelectDateWidget, initial=timezone.now())