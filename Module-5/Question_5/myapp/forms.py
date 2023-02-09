from django import forms
from .models import postmodel

class postform (forms.ModelForm) :

    class Meta :

        model = postmodel
        fields = '__all__'