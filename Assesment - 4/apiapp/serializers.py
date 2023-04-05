from rest_framework import serializers
from .models import apimodel


class apiserializers (serializers.ModelSerializer):

    class Meta :

        model = apimodel
        fields = '__all__'