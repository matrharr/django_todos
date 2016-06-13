from django import forms
from .models import Todo

class TodoForm(forms.Form):
  todo_title = forms.CharField(label='Title', max_length=20)
  todo_body = forms.CharField(label='Info', max_length=300)