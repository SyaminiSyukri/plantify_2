from django import forms
from django.forms import ModelForm
from .models import Notes

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['plantname', 'description', 'image']
        