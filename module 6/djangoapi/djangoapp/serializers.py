from rest_framework import serializers
from .models import Book_model

class Book_serializers (serializers.ModelSerializer):

    class Meta :

        model = Book_model
        fields = '__all__'