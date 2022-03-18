from pyexpat import model
from django import forms
from django.forms import fields, models
from .models import Tribute, District


class TributeForm(forms.ModelForm):

    class Meta:
        model = Tribute
        fields = ('name' , 'district', 'nature')