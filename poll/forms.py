from django import forms
from django.forms import ModelForm
from .models import Polls


class CreateForm(ModelForm):
    class Meta:
        model=Polls
        fields=['question', 'option1', 'option2', 'option3']
        widgets={
            "question": forms.TextInput(attrs={"class": "form-control"}),
            "option1": forms.TextInput(attrs={"class": "form-control"}),
            "option2": forms.TextInput(attrs={"class": "form-control"}),
            "option3": forms.TextInput(attrs={"class": "form-control"}),
        }

