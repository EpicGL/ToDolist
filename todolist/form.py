from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Todolist

class EditForm(ModelForm):
    class Meta:
        model = Todolist
        fields = '__all__'
        exclude = {'user', 'created'}