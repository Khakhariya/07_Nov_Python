from django import forms
from .models import Product_mst_table


class ImageForm(forms.ModelForm):

    class Meta:
        
        model = Product_mst_table
        fields = '__all__'