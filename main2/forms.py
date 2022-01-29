from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import ClearableFileInput
from . import  models

class ExamplarForm(ModelForm):
    class Meta:
        model =models.exemplar
        exclude =[]